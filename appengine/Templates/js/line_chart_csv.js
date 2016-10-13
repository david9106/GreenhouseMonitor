//AmCharts.loadFile( "https://s3-us-west-2.amazonaws.com/s.cdpn.io/t-160/22300.csv", {}, function( response ) {
//AmCharts.loadFile( "http://localhost:8080/get_csv?sensor_type=Temperatura", {}, function( response ) {
/**
 * Init some variables for demo purposes
 */
var day = 0;
var firstDate = new Date();
firstDate.setDate( firstDate.getDate() - 500 );

/**
 * Function that generates random data
 */
function generateChartData() {
  var chartData = [];
  /*for ( day = 0; day < 50; day++ ) {
    var newDate = new Date( firstDate );
    newDate.setDate( newDate.getDate() + day );

    var visits = Math.round( Math.random() * 40 ) - 20;

    chartData.push( {
      "date": newDate,
      "visits": visits
    } );
  }*/
  var myBlob;
	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://localhost:8080/get_csv?sensor_type=Temperatura', true);
	xhr.responseType = 'blob';
	xhr.onload = function(e) {
		if (this.status == 200) {
			myBlob = this.response;
			//alert(myBlob);
		// myBlob is now the blob that the object URL pointed to.
			return myBlobl;
		}
	};
	xhr.send();
 

  return chartData;
}

/**
 * Create the chart
 */
var chart = AmCharts.makeChart( "chartdiv", {
  "type": "serial",
  "dataLoader":{
			"url": "http://localhost:8080/get_csv?sensor_type=Temperatura",
			"format":"csv",
			"delimiter":",",
			"useColumnNames": true,
			"skip":1
			},
  "theme": "light",
  "zoomOutButton": {
    "backgroundColor": '#000000',
    "backgroundAlpha": 0.15
  },
  "categoryField": "Fecha",
  "categoryAxis": {
    "parseDates": true,
    "minPeriod": "mm",
    "dashLength": 1,
    "gridAlpha": 0.15,
    "axisColor": "#DADADA"
  },
  "graphs": [ {
    "id": "g1",
    "valueField": "Valor",
    "bullet": "round",
    "bulletBorderColor": "#FFFFFF",
    "bulletBorderThickness": 2,
    "lineThickness": 2,
    "lineColor": "#b5030d",
    "negativeLineColor": "#0352b5",
    "hideBulletsCount": 50
  } ],
  "chartCursor": {
    "cursorPosition": "mouse"
  },
  "chartScrollbar": {
    "graph": "g1",
    "scrollbarHeight": 40,
    "color": "#FFFFFF",
    "autoGridCount": true
  }
} )

chart.categoryAxis.dateFormats = [{
    period: 'fff',
    format: 'JJ:NN:SS'
}, {
    period: 'ss',
    format: 'JJ:NN:SS'
}, {
    period: 'mm',
    format: 'JJ:NN'
}, {
    period: 'hh',
    format: 'JJ:NN'
}, {
    period: 'DD',
    format: 'MMM DD'
}, {
    period: 'WW',
    format: 'MMM DD'
}, {
    period: 'MM',
    format: 'MMM YYYY'
}, {
    period: 'YYYY',
    format: 'MMM YYYY'
}];

chart.dataProvider = [{lineColor: "#b7e021"}];
