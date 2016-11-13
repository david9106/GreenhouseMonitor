///\file init_localstorage.js
///\brief Save all the important data into the LocalStorage
///\details This is an alternative solution to reduce DB access queries, but it's just an structure, is not fullfilled to function correctly
///Saves the graphing data as follows:
///One entire year of each kind of sensor
///The last value measured of each kind of sensor
///All the measures of each sensor from today
///Also has functions to operate on that data, save it, or fetch it
///It saves the phones and limits as follows:
///All the numbers and their states in json format "phone":"<phone_number>", and "active":"true/false"
///All the limits and their states in json format "<limit_type>":"<limit_value>" and "active":"true/false"
///\author Rafael Karosuo

json_url = 'http://localhost:8080/get_json'
config_url = 'http://localhost:8080/get_config'
if(typeof(Storage) !== "undefined"){	
	//update_year_values();//Updates if it's necessary the year measures on LocalStorage	
	//update_last_measures();//Updates the last measures on all the available sensors	
	//update_today_measures(); //Updates the measures from today, then it'll be able to get the max of them and print it in the header of main page	
	update_phones();
	//update_limits(); //Updates all the registered limits and teir states
}
else{	
	var browser_version;
	if(isOpera)
		browser_version = "Opera";
	else if(isFirefox)
		browser_version = "FireFox";
	else if(isSafari)
		browser_version = "Safari";
	else if(isIE)
		browser_version = "IE";
	else if(isEdge)
		browser_version = "Edge";
	else if(isChrome)
		browser_version = "Chrome";
	else if(isBlink)
		browser_version = "Blink";
		
	alert("Local Storage not supported, in order to be able to use this site, you need to upgrade your browser. Supported versions are Chrome 4.0+, IE 8.0+, Firefox 3.5+, Safari 4.0+, Opera 11.5+");	
	
	window.location.replace("https://www.google.com.mx/#q=Update+browser+version".replace("version",browser_version));
}	

function error_response(status){
	alert('Something went wrong, error: status'.replace("status",status));
}

function update_last_measures(){
	//getJSON_ByCmd(json_url, update_last_measures, error_response); 
}

function update_today_measures(){
	//getJSON_ByCmd(json_url, update_today_measures, error_response); 
}

function update_limits(){
	//getJSON_ByCmd(json_url, update_limits, error_response);
}

function update_phones(){
	///\brief Updates all the registered phones and their states	
	var json_cmd = {"Tipo":"Telefonos"}; //command
	getJSON_ByCmd(config_url,function(json_list){		
		var current_local_value;
		for (json_id in json_list){
			current_local_value = localStorage.getItem("string".replace("string",json_id));
			
			if (current_local_value == null) {//If no current data saved, acces DB and save it
				if(json_id.localeCompare("Tipo") != 0){
					(json_list["key".replace("key",json_id)]):
					//localStorage.setItem("Telefonos", phone_list);
				}
			}else{
				//alert();
				//json_list["key".replace("key",json_id)]
			}
			
			//alert();
		}
	},error_response,json_cmd)
}

function update_year_values(){
	//getJSON_ByCmd(json_url, update_year_values, error_response); 
}
