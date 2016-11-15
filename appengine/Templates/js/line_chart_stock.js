var property_symbol = "°C";
var property_title = "Temperatura";

var chartDataArray = [];

var chartData1 = [];
var chartData2 = [];
var chartData3 = [];
var chartData4 = [];

generateChartData();

function generateChartData() {
  var firstDate = new Date();
  //firstDate.setDate( firstDate.getDate() - 10000 );
  firstDate.setHours( 0, 0, 0, 0 );

  for ( var i = 0; i < 1000; i++ ) {
    var newDate = new Date( firstDate );
    //newDate.setDate( newDate.getDate() + i );
    newDate.setHours( newDate.getHours() + i );
    
    /*var a1 = Math.round( Math.random() * ( 40 + i ) ) + 100 + i;
    var b1 = Math.round( Math.random() * ( 1000 + i ) ) + 500 + i * 2;*/

    var a2 = Math.round( Math.random() * ( 100 + i ) ) + 200 + i;
    var b2 = Math.round( Math.random() * ( 1000 + i ) ) + 600 + i * 2;

    var a3 = Math.round( Math.random() * ( 100 + i ) ) + 200;
    var b3 = Math.round( Math.random() * ( 1000 + i ) ) + 600 + i * 2;

    var a4 = Math.round( Math.random() * ( 100 + i ) ) + 200 + i;
    var b4 = Math.round( Math.random() * ( 100 + i ) ) + 600 + i;
    
    var a1;
    var b1;
    
    if (i%2 == 0){
		a1 = i;
	}else
	{
		a1 = i*2;
	}


    chartData1.push( {
      "date": newDate,
      "value": a1,
      "volume": b1
    } );
    chartData2.push( {
      "date": newDate,
      "value": a2,
      "volume": b2
    } );
    chartData3.push( {
      "date": newDate,
      "value": a3,
      "volume": b3
    } );
    chartData4.push( {
      "date": newDate,
      "value": a4,
      "volume": b4
    } );
  }
}

var chart = AmCharts.makeChart( "chartdiv", {
  "type": "stock",
  "theme": "ligth",
  "dataSets": [ {
      "title": "Sensor1",
      "fieldMappings": [ {
        "fromField": "value",
        "toField": "value"
      }, {
        "fromField": "volume",
        "toField": "volume"
      } ],
      "dataProvider": chartData1,
      "categoryField": "date"
    }, {
      "title": "Sensor2",
      "fieldMappings": [ {
        "fromField": "value",
        "toField": "value"
      }, {
        "fromField": "volume",
        "toField": "volume"
      } ],
      "dataProvider": chartData2,
      "categoryField": "date",
		"compared": true
    }, {
      "title": "Sensor3",
      "fieldMappings": [ {
        "fromField": "value",
        "toField": "value"
      }, {
        "fromField": "volume",
        "toField": "volume"
      } ],
      "dataProvider": chartData3,
      "categoryField": "date"
    }, {
      "title": "Sensor4",
      "fieldMappings": [ {
        "fromField": "value",
        "toField": "value"
      }, {
        "fromField": "volume",
        "toField": "volume"
      } ],
      "dataProvider": chartData4,
      "categoryField": "date"
    }
  ],

  "panels": [ {
    "showCategoryAxis": true,
    "title": property_title,
    "percentHeight": 70,
    "stockGraphs": [ {
      "id": "g1",
      "valueField": "value",
      "comparable": true,
      "showBalloon": true,
      "compareField": "value",
      "balloonText": "[[title]]:<b>[[value]]</b>",
      "compareGraphBalloonText": "[[title]]:<b>[[value]]</b>"
    } ],
    "stockLegend": {
      "periodValueTextComparing": "[[value.close]]",
      "periodValueTextRegular": "[[value.close]]",
      "valueTextComparing": "[[value]]"
    }
  } ],

  "chartScrollbarSettings": {
    "graph": "g1"
  },

  "chartCursorSettings": {
    "valueBalloonsEnabled": true,
    "fullWidth": true,
    "cursorAlpha": 0.1,
    "valueLineBalloonEnabled": true,
    "valueLineEnabled": true,
    "valueLineAlpha": 0.5
  },

  "panelsSettings": {
    "recalculateToPercents": "never"
  },

  "export": {
    "enabled": true
  },
    "valueAxesSettings": {
    "unit": property_symbol,
    "unitPosition": "right"
  }
} );

//var new_catAxis = new AmCharts.CategoryAxesSettings();
//chart.categoryAxesSettings = new_catAxis;
//chart.periodValue = "High"
chart.categoryAxesSettings.parseDates = true;
chart.categoryAxesSettings.groupToPeriods = ["2hh", "DD"];
chart.categoryAxesSettings.minPeriod = "hh";
