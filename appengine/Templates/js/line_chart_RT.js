var chart; //The chart object
var chartData = []; //all the data displayed
var chartCursor; //Visually marks where the mouse is on the graph
var json_url = 'http://localhost:8080/get_json?sensor_type=Temperatura'; //The URL from the JSON is loaded
var reload_interval = 10000; //Sets how often must to be reloaded the info from server


/**By Mathias
 * at https://mathiasbynens.be/notes/xhr-responsetype-json*/
var getJSON = function(url, successHandler, errorHandler) {
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
};

// Gets all data untill now on the DB
function generateChartData() {    
    getJSON(json_url, function(data) {
		for (i in data){
			chartData.push({
				date: data[i].Fecha,
				sensor_property: data[i].Valor
			});
		}		
	}, function(status) {
		alert('Something went wrong.');
	});
}

//Configure Month names in spanish
AmCharts.monthNames = [
  'Enero',
  'Febrero',
  'Marzo',
  'Abril',
  'Mayo',
  'Junio',
  'Julio',
  'Agosto',
  'Septiembre',
  'Octubre',
  'Noviembre',
  'Diciembre'];

// create chart
AmCharts.ready(function() {
    // generate some data first
    generateChartData();

    // SERIAL CHART    
    chart = new AmCharts.AmSerialChart();
    chart.pathToImages = "http://www.amcharts.com/lib/images/";
    chart.marginTop = 0;
    chart.marginRight = 10;
    chart.autoMarginOffset = 5;
    chart.zoomOutButton = {
        backgroundColor: '#000000',
        backgroundAlpha: 0.15
    };
    chart.dataProvider = chartData;
    chart.categoryField = "date";

    // AXES
    // category
    var categoryAxis = chart.categoryAxis;
    categoryAxis.parseDates = true; // as our data is date-based, we set parseDates to true
    categoryAxis.minPeriod = "DD"; // our data is daily, so we set minPeriod to DD
    categoryAxis.dashLength = 1;
    categoryAxis.gridAlpha = 0.15;
    categoryAxis.axisColor = "#DADADA";

    // value                
    var valueAxis = new AmCharts.ValueAxis();
    valueAxis.axisAlpha = 0.2;
    valueAxis.dashLength = 1;
    chart.addValueAxis(valueAxis);

    // GRAPH
    var graph = new AmCharts.AmGraph();
    graph.title = "red line";
    graph.valueField = "sensor_property";
    graph.bullet = "round";
    graph.bulletBorderColor = "#FFFFFF";
    graph.bulletBorderThickness = 2;
    graph.lineThickness = 2;
    graph.lineColor = "#b5030d";
    graph.negativeLineColor = "#0352b5";
    graph.hideBulletsCount = 50; // this makes the chart to hide bullets when there are more than 50 series in selection
    chart.addGraph(graph);

    // CURSOR
    chartCursor = new AmCharts.ChartCursor();
    chartCursor.cursorPosition = "mouse";
    chart.addChartCursor(chartCursor);

    // SCROLLBAR
    var chartScrollbar = new AmCharts.ChartScrollbar();
    chartScrollbar.graph = graph;
    chartScrollbar.scrollbarHeight = 40;
    chartScrollbar.color = "#FFFFFF";
    chartScrollbar.autoGridCount = true;
    chart.addChartScrollbar(chartScrollbar);

    // WRITE
    chart.write("chartdiv");
    
    // set up the chart to update every second
    setInterval(function () {
        // normally you would load new datapoints here,
        // but we will just generate some random values
        // and remove the value from the beginning so that
        // we get nice sliding graph feeling
        
        // remove datapoint from the beginning
        chart.dataProvider.shift();
		
		///Get last sensed value
		getJSON(json_url, function(data) {
			chartData.push({
				date: data[data.length-1].Fecha,
				sensor_property: data[data.length-1].Valor
			});
		}, function(status) {
			alert('Something went wrong.');
		});
        
        //Update graph
        chart.validateData();
    }, reload_interval);
});


