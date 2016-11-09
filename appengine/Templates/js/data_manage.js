/** @file data_manage.js
 *  @brief Local data manage functions
 * 	
 * 	Describes all the functions needed to fetch data from server to browser and save in LocalStorate.
 * 	@author Rafael Karosuo
 * */
 
/** @fn getJSON
 * 	@brief get JSON object/list from url
 * 	
 * 	Creates an AJAX asyncronous GET request to a given url asking for all the sensor measures in a given period of time and waits for a
 * 	JSON object/list as response
 * 	@param[in] url The server URL, it must has the prefix "http://"
 * 	@param[in] successHandler The function name that will be triggered in case that status 200 is responded by server
 * 	@param[in] errorHandler The function name that will be triggered in case that an error status is responded by server
 * 	@param[out] sensor_type The measure's sensor type required
 * 	@param[out] date1 The start of the date range, must be string date format
 * 	@param[out] date2 The end of the date range, must be string date format
 *	@author Mathias
 *	at https://mathiasbynens.be/notes/xhr-responsetype-json*/
function getJSON(url, successHandler, errorHandler) {
	var xhr = new XMLHttpRequest();
	xhr.open('get', url, true);
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
