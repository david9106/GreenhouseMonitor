//AmCharts.loadFile( "https://s3-us-west-2.amazonaws.com/s.cdpn.io/t-160/22300.csv", {}, function( response ) {
AmCharts.loadFile( "http://localhost:8080/get_csv?sensor_type=Temperatura", {}, function( response ) {


  /**
   * Parse CSV
   */
  var data = AmCharts.parseCSV( response, {
    "useColumnNames": true
  } );

var chart = AmCharts.makeChart( "chartdiv", {
  "type": "serial",
  "theme": "light",
  "dataDateFormat": "YYYY-MM-DD",
  "graphs": [ {
    "id": "g1",
    "bullet": "round",
    "bulletBorderAlpha": 1,
    "bulletColor": "#FFFFFF",
    "bulletSize": 5,
    "hideBulletsCount": 50,
    "lineThickness": 2,
    "title": "red line",
    "useLineColorForBulletBorder": true,
    "valueField": "value"
  } ],
  "chartScrollbar": {
    "graph": "g1",
    "oppositeAxis": false,
    "offset": 30,
    "scrollbarHeight": 80,
    "backgroundAlpha": 0,
    "selectedBackgroundAlpha": 0.1,
    "selectedBackgroundColor": "#888888",
    "graphFillAlpha": 0,
    "graphLineAlpha": 0.5,
    "selectedGraphFillAlpha": 0,
    "selectedGraphLineAlpha": 1,
    "autoGridCount": true,
    "color": "#AAAAAA"
  },
  "chartCursor": {
    "cursorAlpha": 1,
    "cursorColor": "#258cbb"
  },
  "categoryField": "date",
  "categoryAxis": {
    "parseDates": true,
    "equalSpacing": true,
    "gridPosition": "middle",
    "dashLength": 1,
    "minorGridEnabled": true
  },
  "zoomOutOnDataUpdate": false,
  "listeners": [ {
    "event": "init",
    "method": function( e ) {

      /**
       * Pre-zoom
       */
      e.chart.zoomToIndexes( e.chart.dataProvider.length - 40, e.chart.dataProvider.length - 1 );

      /**
       * Add click event on the plot area
       */
      e.chart.chartDiv.addEventListener( "click", function() {

        // we track cursor's last known position by "changed" event
        if ( e.chart.lastCursorPosition !== undefined ) {
          // get date of the last known cursor position
          var date = e.chart.dataProvider[ e.chart.lastCursorPosition ][ e.chart.categoryField ];
          
          // require user to enter annotation text
          var text = window.prompt("Enter annotation","");

          // create a new guide
          var guide = new AmCharts.Guide();
          guide.date = date;
          guide.lineAlpha = 1;
          guide.lineColor = "#c44";
          guide.label = text;
          guide.position = "top";
          guide.inside = true;
          guide.labelRotation = 90;
          e.chart.categoryAxis.addGuide( guide );
          e.chart.validateData();
        }
      } )
    }
  }, {
    "event": "changed",
    "method": function( e ) {
      /**
       * Log cursor's last known position
       */
      e.chart.lastCursorPosition = e.index;
    }
  } ]
  
  } );
