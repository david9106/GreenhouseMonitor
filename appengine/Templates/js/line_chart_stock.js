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

var property_symbol = "°C"; ///< Cyrrent property symbol
var property_title = "Temperatura"; ///< Current property title

var chartDataArray = []; ///< Array of DataSet type object, which will be the multiple datasets graphicated

var chartData1 = [];
var chartData2 = [];
var chartData3 = [];
var chartData4 = [];

populate_year_dropdown(2016, 5);///< Populate the year selector dropdown list
request_available_sensors();///< Request the available sensor types, this is an async task
setup_default_dropdowns(); ///< Select default values on year and sensor type dropdown lists
request_locatioon_list("Temperatura"); ///< Gets the location list of Temperatura, all the id_LiSANDRA of that kind of sensor
//generateChartData();///< Defines the first values for the graph

var greenhouse_chart = AmCharts.makeChart( "chartdiv", {
  "type": "stock",
  "theme": "ligth",
			  "dataSets": [ {			
			    "dataProvider": [],
			    "categoryField": "date",
			  } ]
} );

//Should create one object from type DataSet for each sensor type
//Then when we create all the objects, append them to a list which will be the property DataSets of greenhouse_chart

///\brief Configure the chart type as stock
///\details As direct parameter of class AmChart
/// Possible types are: serial, pie, xy, radar, funnel, gauge, map, stock.
greenhouse_chart.type = "stock";

///\brief assign a visual css theme
///\details currently it's used light, since light.js was loaded
///Also the the files related will be found on amcharts/themes/ on Templates/js folder
///example black.js, dark.js, patterns.js
///In order to make them work, they need to be loaded in the index.html, insted of the light.js
///For more information check the link below
///\see http://www.amcharts.com/kbase/working-with-themes/
greenhouse_chart.theme = "ligth";

///\brief create the main panel to hold the graph
///\details The graph is contained by a panel (StockPanel class)
///It defains most of the visual behaviors of the graph, like the horizontal axis (Category Axis) height.
///stockGraphs and stockLegend are independant classes with they're properties, but they're used as attributes of the panel
///\see StockGraph class https://docs.amcharts.com/3/javascriptstockchart/StockGraph
///\see StockLegend class https://docs.amcharts.com/3/javascriptstockchart/StockLegend
var main_panel = new AmCharts.StockPanel();
main_panel.showCategoryAxis = true;
main_panel.title = property_title;
main_panel.percentHeight = 70;
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
greenhouse_chart.valueAxesSettings.unit = property_symbol;

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

generateChartData();///< Constructs the DataSet objects and fetch the data from server

///\brief Fetches the data and put it onto the datasets to graphicate
///\details Send requests to server to get all the data from one kind of sensor
///Also puts that data into the specified DataSet objects and in the global array
///It instructs to the graph to update, only when the http requests are done
///\author Rafael Karosuo
function generateChartData() {	
	
	///\brief Polling if available_sensors is already fulfilled (each 100ms)
	interval_id = setInterval(function(){		
		if(available_sensors.length > 0 && location_list.length > 0){//IF already set the sensors and the location list, go ahead
			clearInterval(interval_id); ///< Stop interval call						
			json_cmd_year_measures.SensorType = $(".sensor").first().text();///< Asign sensor type to the command			
			json_cmd_year_measures.Year = fetch_year; ///< Assing year to command					
			
			getJSON_ByCmd(json_url, function(sensor_list){
				sensor_count = sensor_list[sensor_list.length-1].SensorCount;///< Get the sensor count
				for (dataset=0; dataset<sensor_count; dataset++){///< Create all the data sets
					chartDataArray.push(new AmCharts.DataSet());///< Create a DataSet class
					chartDataArray[dataset].dataProvider = new Array(); ///< Prepare dataProvider of each DataSet, to be able to "push" the sensor measures
					chartDataArray[dataset].title = "Sensor " + location_list[dataset];///< Add the title to the current DataSet, it's "Sensor " + current id_LiSANDRA					
					chartDataArray[dataset].fieldMappings = new Array(); ///< Assign empty array, to be able to "push" the json objects into it
					chartDataArray[dataset].fieldMappings.push({///< Push the FieldMappings inner values
							"fromField": "Valor",
							"toField": "Valor"
					});					
					chartDataArray[dataset].categoryField = "date";///< Tell the DataSet that the property "date" of the values will be the category field
				}///End for datasets				
				alert(sensor_count);
				for(id_LiSANDRA in location_list){
					alert(id_LiSANDRA);
				}	
				
				///\brief go over all the measures of this sensor
				for (element in sensor_list){					
					//~ chartData1.push({
						//~ "date":new Date(sensor_list[element].Fecha),
						//~ "value":parseFloat(sensor_list[element].Valor)
						//~ });
						
					if(!sensor_list[element].hasOwnProperty("SensorCount")){ ///< Avoid the SensorCount component
						chartData1.push({
						"date":new Date(sensor_list[element].Fecha),
						"value":parseFloat(sensor_list[element].Valor)
						});
						chartDataArray[0].dataProvider.push({
							"date":new Date(sensor_list[element].Fecha),
							"value":parseFloat(sensor_list[element].Valor)
							});																
					}///end if not SensorCount					
				}///end for element in sensor_list
				
				greenhouse_chart.categoryField = "date";
				greenhouse_chart.dataProvider = chartData1;
				
				///\brief Configure all the datasets array, attach it to chart
				//greenhouse_chart["dataSets"] = chartDataArray;				
				///\brief Update graph
				greenhouse_chart.validateData();///< Re-read the data sets
				greenhouse_chart.validateNow();///< Re-paint the graph
			
			}, error_response, json_cmd_year_measures);	
			
		}///end if data available			
		
	},100);///end setInterval
  }///end generate_chart_data function
