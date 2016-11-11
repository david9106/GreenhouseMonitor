///\file init_localstorage.js
///\brief Save all the important data into the LocalStorage
///\details Saves the graphing data as follows:
///One entire year of each kind of sensor
///The last value measured of each kind of sensor
///All the measures of each sensor from today
///Also has functions to operate on that data, save it, or fetch it
///It saves the phones and limits as follows:
///All the numbers and their states in json format "phone":"<phone_number>", and "active":"true/false"
///All the limits and their states in json format "<limit_type>":"<limit_value>" and "active":"true/false"
///\author Rafael Karosuo

json_url = 'http://localhost:8080/get_json'
if(typeof(Storage) !== "undefined"){
	getJSON(json_url, update_year_values, error_response); //Updates if it's necessary the year measures on LocalStorage
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

function update_last_measures(json_list){
	
}

function update_today_values(json_list){
	
}

function update_limits(json_list){
	
}

function update_phones(json_list){
	
}

function update_year_values(json_list){
	
}
