  var chartData;
// DATA GENERATOR; FULFILLS GIVE DATASET
function generateChartData( data, field ) {
  chartData = data ? data : [];
  var firstDate = new Date();

  firstDate.setHours( 0, 0, 0, 0 );
  firstDate.setDate( firstDate.getDate() - 2000 );

  for ( var i = 0; i < 2000; i++ ) {
    var value = Math.round( Math.random() * ( 30 ) + 100 );

    // ADD NEW FIELD TO PASSED DATASET
    if ( data ) {
      chartData[ i ][ field ] = value;

      // CREATE NEW ONE
    } else {
      var newDate = new Date( firstDate );
      newDate.setDate( newDate.getDate() + i );

      chartData.push( {
        date: newDate,
        value: value
      } );
    }
  }
  return chartData;
}

// JUST SOME VISUAL FEEDBACK
function growl( type, msg ) {
  var alert = jQuery( "<div>" ).addClass( "alert alert-" + type ).on( "click", function() {
    jQuery( this ).remove();
  } ).prependTo( ".growl" );
  jQuery( "<p>" ).text( msg ).appendTo( alert );
  jQuery( alert ).animate( {
    "opacity": 0
  }, 3000, function() {
    jQuery( this ).remove();
  } );
}

// CREATE CHART
var chart = AmCharts.makeChart( "chartdiv", {
  "type": "stock",
  "dataSets": [ {
    "title": "Dataset 1",
    "fieldMappings": [ {
      "fromField": "value",
      "toField": "value"
    } ],
    "dataProvider": generateChartData(),
    "categoryField": "date"
  }, {
    "title": "Dataset 2",
    "fieldMappings": [ {
      "fromField": "value",
      "toField": "value"
    } ],
    "dataProvider": generateChartData(),
    "categoryField": "date"
  } ],
  "panels": [ {
    "title": "Panel 1",
    "stockGraphs": [ {
      "valueField": "value",
      "comparable": true
    } ],
    "stockLegend": {}
  } ],
  "chartCursorSettings": {
    "valueLineEnabled": true,
    "valueLineBalloonEnabled": true
  },
  "dataSetSelector": {
    "position": "left"
  },
  "periodSelector": {
    "position": "left",
    "inputFieldsEnabled": false,
    "periods": [ {
      "period": "DD",
      "count": 10,
      "label": "10 days"
    }, {
      "period": "MM",
      "count": 1,
      "label": "1 month"
    }, {
      "period": "YYYY",
      "count": 1,
      "label": "1 year",
      "selected": true
    }, {
      "period": "YTD",
      "label": "YTD"
    }, {
      "period": "MAX",
      "label": "MAX"
    } ]
  }
} );

// WAIT UNTIL DOCUMENT IS READY TO BIND BUTTONS
jQuery( document ).ready( function() {
  // REMOVE DATASET
  jQuery( ".btn-dataset-remove" ).on( "click", function() {
    if ( chart.dataSets.length > 1 ) {
      // REMOVE LATEST DATASET AND VALIDATE
      var dataset = chart.dataSets.pop();
      chart.validateNow();

      // GROWL
      growl( "danger", dataset.title );
    } else {

      // GROWL
      growl( "info", "Kept latest" );
    }
  } );

  // ADD DATASET
  jQuery( ".btn-dataset-add" ).on( "click", function() {
    var tmp = [];

    // CREATE DATASET
    var dataset = new AmCharts.DataSet();
    dataset.title = "Dataset " + ( chart.dataSets.length + 1 );
    dataset.dataProvider = generateChartData();
    dataset.categoryField = "date";

    // LOOP THROUGH PANELS
    // TO GENERATE DATA AND CREATE FIELDMAPPINGS FOR EACH GRAPH
    for ( i1 in chart.panels ) {
      // LOOP THROUGH PANEL GRAPHS
      for ( i2 in chart.panels[ i1 ].stockGraphs ) {
        var valueField = chart.panels[ i1 ].stockGraphs[ i2 ].valueField;
        // GENERATE NEW GRAPH DATA
        dataset.dataProvider = generateChartData( dataset.dataProvider, valueField );

        // ADD FIELDMAPPING
        dataset.fieldMappings.push( {
          "fromField": valueField,
          "toField": valueField
        } );
      }
      tmp.push( chart.panels[ i1 ].title );
    }

    // ADD NEW DATASET AND VALIDATE
    chart.dataSets.push( dataset );
    chart.validateNow();

    // GROWL
    growl( "success", dataset.title + " fulfilled " + tmp.join( "," ) );
  } );

  // REMOVE PANEL
  jQuery( ".btn-panel-remove" ).on( "click", function() {
    if ( chart.panels.length ) {
      // REMOVE LATEST PANEL AND VALIDATE
      var panel = chart.panels.pop();
      chart.removePanel( panel );
      chart.validateNow();

      // GROWL
      growl( "danger", panel.title );
    } else {
      growl( "info", "No panels" );
    }
  } );

  // ADD PANEL
  jQuery( ".btn-panel-add" ).on( "click", function() {
    var id = ( chart.panels.length + 1 );
    var valueField = "p" + id;

    // MAIN DATASET (CURRENT SELECTION)
    var dataSet = chart.mainDataSet;
    dataSet.fieldMappings.push( {
      "fromField": valueField,
      "toField": valueField
    } );
    dataSet.dataProvider = generateChartData( dataSet.dataProvider, valueField );

    // NEW PANEL
    var panel = new AmCharts.StockPanel();
    panel.showCategoryAxis = chart.panels.length == 0;
    panel.title = "Panel " + id;
    panel.stockLegend = {};

    // NEW GRAPH
    var graph = new AmCharts.StockGraph();
    graph.valueField = valueField;
    graph.comparable = true;
    panel.addStockGraph( graph );

    // ADD AND VALIDATE
    chart.addPanel( panel );
    chart.validateNow();
    chart.validateData();

    // GROWL
    growl( "success", panel.title + " append to " + chart.mainDataSet.title );
  } );
} );
