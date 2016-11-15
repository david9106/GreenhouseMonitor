///\file line_chart_stock.js
///\brief Configure and generate the amcharts stock graph of the sensor measures in different time groups
///\details We're using Line graph type to show the sensor measures
///The graphication library is AmCharts, the group of Stock Charts
///All the access to the properties, most of times will be through json object id's and property values, few are based on classes from AmCharts
///\see https://docs.amcharts.com/3/javascriptstockchart
///\author Rafael Karosuo


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

var greenhouse_chart = AmCharts.makeChart( "chartdiv", {
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

  "chartCursorSettings": {
    "valueBalloonsEnabled": true,
    "fullWidth": true,
    "cursorAlpha": 0.1,
    "valueLineBalloonEnabled": true,
    "valueLineEnabled": true,
    "valueLineAlpha": 0.5,
    "categoryBalloonDateFormats": [{
			            "period": "DD",
			            "format": "MMM DD"
			        }, {
			            "period": "hh",
			            "format": "MMM DD (HH hrs)"
			        }]
  },
  
  "export": {
    "enabled": true
  }
} );



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

///\brief Defines the date groups
///\details It will be 2 main groups, day groups and hour groups, both showing the max of each one
///The hour grups are used by the day visualization and the day group by the rest of the graph periods, which are:
///monthly
///weekly
///and year seasons
greenhouse_chart.categoryAxesSettings.groupToPeriods = ["hh", "DD"];

///\brief Defines the smaller group, which is hourly
///\details The smaller useful grop is max per hour
greenhouse_chart.categoryAxesSettings.minPeriod = "hh";
