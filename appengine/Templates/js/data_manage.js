///\file data_manage.js
///\brief Local data manage functions, and global variables	
///\details Describes all the functions needed to fetch data from server to browser, so the needed operations between datasets on the graph locally
///ATENTION!: The idea of having today_measures, last_measures, max_measures doesn't seems a good idea, but they're there in case that we decide
///to implement those, mainly using LocalStorage
///The format for measures that are just one per sensor is a json object array
/// [{"Tipo":"<sensor_type>", "Ubicacion":"<id_lisandra>", "Valor":"<a_value>"},{"Tipo":"<sensor_type2>", "Ubicacion":"<id_lisandra2>", "Valor":"<a_value2>"}...]
///For the values that are many per sensor, is an array that holds arrays with the above format, except that each inner array hast only one sensor type
/// [[{"Tipo":"<sensor_type>",...},{"Tipo":"<sensor_type>",...},...],[{"Tipo":"<sensor_type2>",...},{"Tipo":"<sensor_type2>",...},...]..]
///In the case of the config data, they'll be in a json object array as follows
/// [{"<phone_0>":"<phone_num>"},{"phone_1":"<phone_num>"},...] ;where phone_N has 0 < N < 9
/// [{"MaxTemperatura":"<max_value>"},{"Max<sensor_type>":"<max_value>"},...]
///The available_sensors array, holds the following format:
/// ["Temperatura","Humedad",...]
///\author Rafael Karosuo

var available_sensors = []; ///<Holds the available sensor types in string format
var phones_registered = []; ///< saves all the registered phones and their state (active/not)
var limits_registered = []; ///< saves all the sms alert limits, there's always 2 limits per sensor type
var interval_id; ///< Holds the id to enable/disable interval callbacks
var location_list = [] ///< Holds the id_LiSANDRA's list related with the current selected sensor

json_url = 'http://localhost:8080/get_json' ///< URL to fetch the sensor measures
config_url = 'http://localhost:8080/get_config' ///< URL to fetch the config values

function error_response(status){
	alert('Something went wrong, HTTP response error: status'.replace("status",status));
}

function getJSON(url, successHandler, errorHandler) {
	///\brief get JSON object/list from url
	///\details Creates an AJAX asyncronous GET request to a given url asking for all the sensor measures in a given period of time and waits for a JSON object/list as response
	///\param[in] url The server URL, it must has the prefix "http://"
	///\param[in] successHandler The function name that will be triggered in case that status 200 is responded by server
	///\param[in] errorHandler The function name that will be triggered in case that an error status is responded by server
	///\author Mathias
	///\see https://mathiasbynens.be/notes/xhr-responsetype-json
	var xhr = new XMLHttpRequest();
	xhr.open('GET', url, true);
	xhr.responseType = 'json';
	xhr.onload = function() {
		var status = xhr.status;
		if (status == 200) {
			successHandler && successHandler(xhr.response);
		} else {
			errorHandler && errorHandler(status);
		}
	};
	xhr.send();
}

function getJSON_ByCmd(url, successHandler, errorHandler, json_command) {
	///\brief get JSON object/list from url by sending a command in the same format
	///\details Creates an AJAX asyncronous POST request to a given url sending a json message with the command of which
	///server information needs, the message should be "Tipo":"<command>" and waits for a JSON object/list as response	
	///\param[in] url The server URL, it must has the prefix "http://"
	///\param[in] successHandler The function name that will be triggered in case that status 200 is responded by server
	///\param[in] errorHandler The function name that will be triggered in case that an error status is responded by server
	///\param[out] json_command the json to be sent with the command
	///\author Mathias and Rafael Karosuo
	///\see https://mathiasbynens.be/notes/xhr-responsetype-json
	var xhr = new XMLHttpRequest();
	xhr.open('POST', url, true);
	xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	xhr.responseType = 'json';
	xhr.onload = function() {
		var status = xhr.status;
		if (status == 200) {		
			successHandler && successHandler(xhr.response);
		} else {
			errorHandler && errorHandler(status);
		}
	};
	xhr.send(JSON.stringify(json_command));
}

function get_year_measures(the_year){
		
		///Get last sensed value
		getJSON(json_url, function(data) {
			var limit = data.length - chartData.length; //Get how many values needs to be updated
			var i;
			if(limit != 0 && data.length > 0){ //Do it only if there's new data
				for(i=0; i<limit; i++){
					chartData.push({
						date: data[chartData.length + i].Fecha,
						sensor_property: data[chartData.length + i].Valor
					});
				}
			}
						
		}, function(status) {
			alert('Something went wrong.');
		});
}


function mergeJSON(source1,source2){
    /*
     * Properties from the Souce1 object will be copied to Source2 Object.
     * Note: This method will return a new merged object, Source1 and Source2 original values will not be replaced.
     * */
    var mergedJSON = Object.create(source2);// Copying Source2 to a new Object
	
	///Change "attrname" by date property, since it's the one that we want to ignore in case that it already exists

    for (var attrname in source1) {
        if(mergedJSON.hasOwnProperty(attrname)) {
          if ( source1[attrname]!=null && source1[attrname].constructor==Object ) {
              /*
               * Recursive call if the property is an object,
               * Iterate the object and set all properties of the inner object.
              */
              mergedJSON[attrname] = mergeJSON(source1[attrname], mergedJSON[attrname]);
          } 

        } else {//else copy the property from source1
            mergedJSON[attrname] = source1[attrname];

        }
      }

      return mergedJSON;
}

function paint_config_in_html() {	
///\brief pull from DB the registered config data, phones and limits
	///\In order to let them available to paint on html	
	///\details Uses json commands to retrieve the information
	///Tipo:Telefonos retrieve all the phones and their state
	///Tipo:Limites retrieve all the limits and their state
	
	var json_cmd_phones = {"Tipo":"Telefonos"}; //phones command
	var json_cmd_limits = {"Tipo":"Limites"}; //limits command	
	
	getJSON_ByCmd(config_url,function(json_list){		
		phones_registered.length = 0 //Clear globals	
		
		for(json_id in json_list){
			if(json_id.localeCompare("Tipo") != 0){ //get just phones, not the cmd id
				phones_registered.push([json_id, json_list["key".replace("key",json_id)]]);
				
				if(/^phone_\d/.test(json_id)){ //check if it's a phone
					document.getElementById(json_id.toString()).value = json_list[json_id];
				}else{//or a checkbox
					$(".input-group .input-group-addon #"+json_id).attr('checked',json_list[json_id]);
				}//end check regexs				
			}			
		}//end for each json id	
	},error_response,json_cmd_phones)	

	getJSON_ByCmd(config_url, function(json_list){
		limits_registered.length = 0 //clear globals
		for(json_id in json_list){
			if(json_id.localeCompare("Tipo") != 0){
				if(/^check_\w/.test(json_id)){ //check if it's a checkbox
					$("#"+json_id).attr('checked',json_list[json_id]);
				}else{//or a limit value					
					document.getElementById(json_id.toString()).value = json_list[json_id];
				}//end check regexs	
			}
		}//end for each json id
	},error_response,json_cmd_limits)
}

function setup_default_dropdowns(){
///\brief Select default year and sensor type
///\details Select the current year as default year on the year-dropdown
///\author Rafael Karosuo, Alejandro Islas	
	$("#drop-year").text($(".year").first().text()); ///<Set the first year
}

function request_available_sensors(){
///\brief Request a list of the available sensors
///\details Updates the variable available_sensors and populates the corresponding combobox
///Also selects as default the first sensor on dropdown list
///\author Rafael Karosuo, Alejandro Islas

	////The json commands sent, started with SensorType:"Temperatura", but it will be changed if needed
	var json_cmd_available_sensors = {"Tipo": "GetSensorTypes"};	
	
	getJSON_ByCmd(json_url, function(sensor_list){
		available_sensors.length = 0; ///< Clear global		
		$(".sensor").remove();///< Clear previous options
		for(element in sensor_list){						
			$(".sensor-type ul").append("<li class=\"sensor\"><a>"+sensor_list[(sensor_list.length-1) - element]+"</a></li>");///< Add current sensor type
			available_sensors.push(sensor_list[element]);///< Save the sensor types on global
		}//end for each json id
		$("#drop-sensor").text($(".sensor").first().text())///< Selects first sensor as default
		
		///\brief Reassign the listeners to the new instances
		$(".sensor").on('click',function(){
			$("#drop-sensor").text($(this).text()).append(" <span class=\"caret\"></span>");                    
			generateChartData($(this).text());///< Refresh datasets, since it will be change sensor, we just have info of the current sensor
		});
	}, error_response, json_cmd_available_sensors);	
	
}

function populate_year_dropdown(start_year, sum_years){
///\brief Fill the year dropdown list
///\param start_year Is the year where the dropdown list starts
///\param sum_years Is the amount of years that the dropdown will go
///\details with the corresponding years, starting with the current and 5 years ahead
///The years must be 4 digits and the sum_years must be 1 digit
///\author Rafael Karosuo, Alejandro Islas
	if (/\d{4}/.test(start_year) && /\d{1}/.test(sum_years)){
		$(".year").remove();///Clear previous options
		for(year_delta=0; year_delta<sum_years; year_delta++){
			$(".year-selection ul").append('<li class="year" value=\"'+(start_year+year_delta)+'\"><a>'+(start_year+year_delta)+'</a></li>'); ///Add the years
		}///end for
	}	
}


function request_locatioon_list(sensor_type){
///\brief Retrieve the id_LiSANDRA's list related with one kind of sensor
///\details The LiSANDRA's list is the location list of the sensors, since other sensor could not be part of LiSANDRA's module
///but they're gonna have an id_LiSANDRA to be able to link that id to a geographic location
///\param sensor_type Is the kind of sensor from we want to get the location list
///\author Rafael Karosuo

	///\brief The json command sent, it will retrieve the location list of sensor_type
	var json_cmd_location_list = {"Tipo": "GetLocationList"};
	json_cmd_location_list["SensorType"] = sensor_type;	
	//alert(JSON.stringify(json_cmd_location_list));
	location_list.length = 0; ///< Clear global, before send request, this makes code depending on this, waits correctly for a fullfilled array
	getJSON_ByCmd(json_url, function(sensor_list){			
		for(element in sensor_list){						
			location_list.push(sensor_list[element]);///< Save the sensor types on global
			//alert(sensor_list[element]);
		}///end for each element
	}, error_response, json_cmd_location_list);	
	
}

function day_default_configuration(){
	return true
}
