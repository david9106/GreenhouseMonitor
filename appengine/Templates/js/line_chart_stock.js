///\file line_chart_stock.js
///\brief Configure and generate the amcharts stock graph of the sensor measures in different time groups
///\details We're using Line graph type to show the sensor measures
///The graphication library is AmCharts, the group of Stock Charts
///All the access to the properties, most of times will be through json object id's and property values, few are based on classes from AmCharts
///\see https://docs.amcharts.com/3/javascriptstockchart
///\author Rafael Karosuo
var fetch_year = 2016; ///< The year that will be fetched from DB
var json_cmd_year_measures = {"Tipo": "GetSensorYearMeasures","SensorType": "Temperatura","Year": "2016"};///< Command to retrieve all the year measures
var json_cmd_today_measures = {Tipo: "GetSensorTodayMeasures",SensorType: "Temperatura"};
var json_cmd_last_measur = {"Tipo": "GetLastMeasure","SensorType": "Temperatura"};	

populate_year_dropdown(2016, 5);///< Populate the year selector dropdown list
setup_default_dropdowns(); ///< Select default values on year and sensor type dropdown lists

//~ Start of the loading GIF
$('#loading').removeClass("hide").addClass("show");
//~ -------------------------
request_available_sensors();///< Request the available sensor types, this is an async task

var property_symbol_hash = {"Temperatura":" °C", "Humedad":" %", "CO2":" ppm", "Iluminacion":" lx"};///< Hash list to retrieve the property symbol depending on type


var spring_guides = summer_guides = fall_guides = winter_guides = [];///< Spring color block define and date ranges for it
//~ var summer_guides = [];///< Summer color block define and date ranges for it
//~ var fall_guides = [];///< Autumn color block define and date ranges for it
//~ var winter_guides = [];///< Winter color block define and date ranges for it


///\brief Defines the color, alpha and dates for season color blocks
spring_guides.push({
	date: new Date("March 21, year 00:00:00".replace("year",fetch_year)),
	toDate: new Date("June 20, year 23:59:59".replace("year",fetch_year)),
	lineAlpha: 0.1,
	fillAlpha: 0.25,
	//~ fillColor: "#2dc86f",
	fillColor: "#1b7e07",
	expand: true
});

summer_guides.push({
	date: new Date("June 21, year 00:00:00".replace("year",fetch_year)),
	toDate: new Date("September 22, year 23:59:59".replace("year",fetch_year)),
	lineAlpha: 0.1,
	fillAlpha: 0.25,
	//~ fillColor: "#f1c40f",
	fillColor: "#ffb400",
	expand: true
});

fall_guides.push({
	date: new Date("September 23, year 00:00:00".replace("year",fetch_year)),
	toDate: new Date("December 20, year 23:59:59".replace("year",fetch_year)),
	lineAlpha: 0.1,
	fillAlpha: 0.25,
	//~ fillColor: "#e67e22",	
	fillColor: "#ff4400",
	expand: true
});

winter_guides.push({
	date: new Date("December 21, year 00:00:00".replace("year",fetch_year)),
	toDate: new Date("March 20, year 23:59:59".replace("year",fetch_year)),
	lineAlpha: 0.1,
	fillAlpha: 0.25,
	//~ fillColor: "#bdc3c7",
	fillColor: "#9bfff0",
	expand: true
});



///\brief Initialize an AmCharts, select stock type and light theme
///\details Generates an instance of AmStockChart and put basic config, since we're going to need dynamic config
///it's not a good idea to use json config object
///\param "chartdiv" is the id of the container html div
///\param {...} is a json object, that could hold the entire config of the graph
///\see https://docs.amcharts.com/3/javascriptstockchart/AmChart
///\see https://docs.amcharts.com/3/javascriptstockchart/AmCharts
///\see https://docs.amcharts.com/3/javascriptstockchart/AmStockChart
var greenhouse_chart = AmCharts.makeChart( "chartdiv", {
  "type": "stock",
  "theme": "ligth"
  } );




///\brief Configure the chart type as stock
///\details As direct parameter of class AmChart
/// Possible types are: serial, pie, xy, radar, funnel, gauge, map, stock.
//greenhouse_chart.type = "stock";

///\brief assign a visual css theme
///\details currently it's used light, since light.js was loaded
///Also the the files related will be found on amcharts/themes/ on Templates/js folder
///example black.js, dark.js, patterns.js
///In order to make them work, they need to be loaded in the index.html, insted of the light.js
///For more information check the link below
///\see http://www.amcharts.com/kbase/working-with-themes/
//greenhouse_chart.theme = "ligth";

///\brief create the main panel to hold the graph
///\details The graph is contained by a panel (StockPanel class)
///It defains most of the visual behaviors of the graph, like the horizontal axis (Category Axis) height.
///stockGraphs and stockLegend are independant classes with they're properties, but they're used as attributes of the panel
///\see StockGraph class https://docs.amcharts.com/3/javascriptstockchart/StockGraph
///\see StockLegend class https://docs.amcharts.com/3/javascriptstockchart/StockLegend
var main_panel = new AmCharts.StockPanel();
main_panel.showCategoryAxis = true;
main_panel.title = "Temperatura";
main_panel.percentHeight = 70;

///\brief binds the spring color block arrays to the panel
main_panel.categoryAxis.guides = spring_guides,summer_guides,fall_guides,winter_guides;
main_panel.valueAxes.push(
	{
	  guides: [{
		lineAlpha: 1,
		lineColor: "#000",
		}]
	}
);

///\brief Creates the main graph
///\details This is the one that literally holds all the data points
var main_graph = new AmCharts.StockGraph();
main_graph.valueField = "value";
main_graph.comparable = true;
main_graph.showBalloon = true;
main_graph.compareField = "value";
///\brief How the exact data point balloon will display which text
main_graph.balloonText = "[[title]]:<b>[[value]]</b>";
main_graph.compareGraphBalloonText = "[[title]]:<b>[[value]]</b>";
///\brief Define grouping with the SUM criteria
main_graph.periodValue = "High";
///\brief binds the graph with the panel
main_panel.addStockGraph(main_graph);
///\brief Creates the main Stock legend
///\details This defines the sorounding text tags, like the ones changing on the top besides the color squares
var main_stock_legend = new AmCharts.StockLegend();
main_stock_legend.periodValueTextComparing = "[[value.close]]";
main_stock_legend.periodValueTextRegular = "[[value.close]]";
main_stock_legend.valueTextComparing = "[[value]]";
///\brief binds Legend to panel
main_panel.stockLegend = main_stock_legend;
///\brief binds the whole panel with the chart
greenhouse_chart.addPanelAt( main_panel, 0 );


///\brief Defines the propertys of ChartCursorSettings class, configuring the mouse cursor
///\details To see the description of each parameter, check the class components on the link bellow:
///\see https://docs.amcharts.com/3/javascriptstockchart/ChartCursorSettings
greenhouse_chart.chartCursorSettings.valueBalloonsEnabled = true;
greenhouse_chart.chartCursorSettings.fullWidth = true;
greenhouse_chart.chartCursorSettings.cursorAlpha = 0.1;
greenhouse_chart.chartCursorSettings.valueLineBalloonEnabled = true;
greenhouse_chart.chartCursorSettings.valueLineEnabled = true;
greenhouse_chart.chartCursorSettings.valueLineAlpha = 0.5;
///\brief Defines a different date ballon on vertical cursor for each group
///\details Just remember that MM's are months, DD days and HH hours
greenhouse_chart.chartCursorSettings.categoryBalloonDateFormats = [{
			            "period": "DD",
			            "format": "MMM DD"
			        }, {
			            "period": "hh",
			            "format": "MMM DD (HH hrs)"
			        }];

///\brief Enables the export options of the current graph
///\details The export option depends on a separete export.js file and a export.css file
///The export options work on the current shown graph segment only
greenhouse_chart.export = {"enabled":"true"};

///\brief Avoid calculate difference porcentage between datasets
///\details Since the datasets are being compared in this kind of graph, where we can have more than one dataset at a time,
///then typically shows the difference in porcentage, but in this case is disabled to let the user see the actual values of each dataset
greenhouse_chart.panelsSettings.recalculateToPercents = "never";

///\brief Define the measured property unit, like Celcius grades
///\details The available string symbols are defined in the global variable (in this file and below) property_symbol
///\Available symbols could be incremented pushing the strings to that global
greenhouse_chart.valueAxesSettings.unit = "°C";

///\brief Define the position where the symbol will go in respect to the measure value
///\details Could be right or left, it doesn't include a space
greenhouse_chart.valueAxesSettings.unitPosition = "righ";

///\brief Disable the horizontal zoom scrollbar
///\details Since the graph periods are clearly defined, the zoom scrollbar won't be needed, and could represent confusion for the user
greenhouse_chart.chartScrollbarSettings.enabled = false;

///\brief Enable the date grouping
greenhouse_chart.categoryAxesSettings.parseDates = true;

///\brief Always try to group datasets
///\details It need groupToPeriods and minPeriod available
///to work properly
greenhouse_chart.categoryAxesSettings.alwaysGroup = true;

///\brief Maximum series shown at a time.
///\details In case there are more data points in the selection than maxSeries, the chart will group data to longer periods
///Means more than 288 series, it's a bigger view than a day, so max per day groups will be used
///Each day has 288 series, since they're each 5 minutes
greenhouse_chart.categoryAxesSettings.maxSeries = 288;

///\brief Defines the date groups
///\details It will be 2 main groups, day groups and hour groups, both showing the max of each one
///The hour grups are used by the day visualization and the day group by the rest of the graph periods, which are:
///monthly
///weekly
///and year seasons
greenhouse_chart.categoryAxesSettings.groupToPeriods = ["hh", "DD"];

///\brief Defines seconds as the smaller group available on datasets
///\details The datasets has data that contains difference in seconds
///Neverthless the smaller useful grop is max per hour, this option refers to the raw data min period
///How will it be shown is other story
greenhouse_chart.categoryAxesSettings.minPeriod = "ss";

///\brief Enable show of data selector box, and defines it to left side
///\details Here shows all the available datasets to pick and show on the graph
greenhouse_chart["dataSetSelector"] = {"position":"left"};

generateChartData("Temperatura");///< Constructs the DataSet objects and fetch the data from server, initially  the Temperature

///\brief Fetches the data and put it onto the datasets to graphicate
///\param sensor_type Is the kind of sensor that will be showed up, used to get the id's related, the measures and print the graph title
///\details Send requests to server to get all the data from one kind of sensor
///Also puts that data into the specified DataSet objects and in the global array
///It instructs to the graph to update, only when the http requests are done
///\author Rafael Karosuo
function generateChartData(sensor_type) {	
		
	request_locatioon_list(sensor_type); ///< Gets the location list of sensor_type, all the id_LiSANDRA of that kind of sensor
	
	///\brief Polling if available_sensors is already fulfilled (each 100ms)
	interval_id = setInterval(function(){		
			
		if(available_sensors.length > 0 && location_list.length > 0){//IF already set the sensors and the location list, go ahead
			clearInterval(interval_id); ///< Stop interval call						
			json_cmd_year_measures.SensorType = sensor_type;///< Asign sensor type to the command			
			json_cmd_year_measures.Year = fetch_year; ///< Assing year to command
			greenhouse_chart.panels[0].title = sensor_type;	///< Assign the new sensor_type tittle to the property axis
			greenhouse_chart.valueAxesSettings.unit = property_symbol_hash[sensor_type]; ///< Assign the text symbol to the propertiy values on the vertical axis
			greenhouse_chart.dataSets.length = 0///< Clear previous location list			
			getJSON_ByCmd(json_url, function(sensor_list){				
				for(id_LiSANDRA in location_list){///< Go for all the id groups, how many sensors of this kind needs to be created
					var dataset = new AmCharts.DataSet(); ///<Create the new DataSet
					dataset.title = "Sensor " + location_list[id_LiSANDRA]; ///< Asign the id_lisandra as sensor title
					dataset.dataProvider = get_filled_array(sensor_list, location_list[id_LiSANDRA]); ///< Push all the data related with that id, onto one dataProvider array
					dataset.categoryField = "date";///< Asign the field that will be the category axis value, from the json objects in dataProviders
					dataset.fieldMappings.push( {///< Add field mappings, using the properties of the json objects, "value" holds the "Valor" from sensor measures
					  "fromField": "value",
					  "toField": "value"
					} );;				
					greenhouse_chart.dataSets.push(dataset); ///< Bind the dataset with the current chart
					greenhouse_chart.validateNow(); ///< Repaint graph, no need to validateDate() since it's a new DataSet object
				}
				
				//~ END of the loading GIF								
				$('#loading').removeClass("show").addClass("hide");
				$('#chartdiv').removeClass("hide").addClass("show");
				//~ ------------------------- 			
			
			}, error_response, json_cmd_year_measures);	
			
		}///end if data available			
		
	},100);///end setInterval
  }///end generate_chart_data function
  
  
function get_filled_array(sensor_list, id_LiSANDRA){
///\brief  return an array as DataProvider, that correspond with some id_LiSANDRA
///\details It goes over all the list and check which of those measures go for the param id_Lisandra and push them
///into an array
///\param sensor_list All the measures of one kind of sensor, with all the sub gorups lisandra
///\param id_LiSANDRA The id lisandra that will be used to group the array that will be returned
///\return an array with the data of the specified id_LiSANDRA
	var chartData = [];
	for (element in sensor_list){										
		if(!sensor_list[element].hasOwnProperty("SensorCount")){ ///< Avoid the SensorCount component
			if(sensor_list[element].Ubicacion.localeCompare(id_LiSANDRA) == 0){///< If it has the same ID, push it
				chartData.push({
				"date": new Date(sensor_list[element].Fecha),
				"value":parseFloat(sensor_list[element].Valor)
				});					
			}///end if same id					
		}///end if not SensorCount					
	}///end for element in sensor_list
	
	return chartData;
}
