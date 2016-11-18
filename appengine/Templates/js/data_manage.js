///\file data_manage.js
///\brief Local data manage functions, and global variables	
///\details Describes all the functions needed to fetch data from server to browser and save in LocalStorate if necesary
///All the global variables saves in json format to ease the relation between the sensor type and it's measures
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

var last_measures = [];///< saves the most recent measures of each kind of sensor
var max_measures = []; ///< saves the MAX values measures obteined until now
					///< these are taken from the today_measures
var available_sensors = []; ///<Holds the available sensor types in string format
var today_measures = []; ///< saves all measures got until now since 12am of today
var phones_registered = []; ///< saves all the registered phones and their state (active/not)
var limits_registered = []; ///< saves all the sms alert limits, there's always 2 limits per sensor type
//var globals_init_flag = false; ///< Polling variable to check if the graph data is already available on the global variables
var interval_id; ///< Holds the id to enable/disable interval callbacks

var set_lisandra_globals = function (obj, new_value){
	obj.value = new_value;
}

json_url = 'http://localhost:8080/get_json' ///< URL to fetch the sensor measures
config_url = 'http://localhost:8080/get_config' ///< URL to fetch the config values

function error_response(status){
	alert('Something went wrong, error: status'.replace("status",status));
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

function request_available_sensors(){
///\brief Request a list of the available sensors
///\details Updates the variable available_sensors
///\author Rafael Karosuo

	////The json commands sent, started with SensorType:"Temperatura", but it will be changed if needed
	var json_cmd_available_sensors = {"Tipo": "GetSensorTypes"};
	var json_cmd_year_measures = {"Tipo": "GetSensorYearMeasures","SensorType": "Temperatura","Year": year};
	var json_cmd_today_measures = {Tipo: "GetSensorTodayMeasures",SensorType: "Temperatura"};
	var json_cmd_last_measur = {"Tipo": "GetLastMeasure","SensorType": "Temperatura"};	
	
	getJSON_ByCmd(json_url, function(sensor_list){
		available_sensors.length = 0; //Clear global		
		for(element in sensor_list){
			available_sensors.push(sensor_list[element]);
		}//end for each json id
	}, error_response, json_cmd_available_sensors);	
	
}

function day_default_configuration(){
	return true
}
