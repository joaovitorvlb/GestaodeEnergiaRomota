
$(document).ready(function() 
{
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
      });

      Highcharts.chart('container-grafico-dinamico', {
          chart: {
              type: 'spline',
              animation: Highcharts.svg, // don't animate in old IE
              marginRight: 10,
              events: {
                  load: function () {

                      // set up the updating of the chart each second
                      var series = this.series[0];
                      setInterval(function () 
                      {    
                          var x = (new Date()).getTime(), // current time
                              y = Math.random();
                          series.addPoint([x, y], true, true);
                      }, 1000);
                  }
              }
          },
          title: {
              text: 'Grafico de plotagem dinamica'
          },
          xAxis: {
              type: 'datetime',
              tickPixelInterval: 150
          },
          yAxis: {
              title: {
                  text: 'Potencia(W)'
              },
              plotLines: [{
                  value: 0,
                  width: 1,
                  color: '#808080'
              }]
          },
          tooltip: {
              formatter: function () {
                  return '<b>' + this.series.name + '</b><br/>' +
                      Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                      Highcharts.numberFormat(this.y, 2);
              }
          },
          legend: {
              enabled: false
          },
          exporting: {
              enabled: false
          },
          series: [{
              name: 'Random data',
              data: (function () {
                  // generate an array of random data
                  var data = [],
                      time = (new Date()).getTime(),
                      i;

                  for (i = -19; i <= 0; i += 1) {
                      data.push({
                          x: time + i * 1000,
                          y: Math.random()
                      });
                  }
                  return data;
              }())
          }]
      });
  });

  var chart = Highcharts.chart('container-grafico-colunas', {

  chart: {
    type: 'column'
  },

  title: {
    text: ''
  },

  subtitle: {
    text: ''
  },

  legend: {
    align: 'right',
    verticalAlign: 'middle',
    layout: 'vertical'
  },

  xAxis: {
    categories: ['dom','seg','ter','qua','qui','sex','sab',],
    labels: {
      x: -10
    }
  },

  yAxis: {
    allowDecimals: false,
    title: {
      text: 'Potencia Durante a Semana'
    }
  },
  

  series: [{
    name: 'Semana',
    data: [8, 5, 4, 7, 5, 3, 1]
  }],

  responsive: {
    rules: [{
      condition: {
        maxWidth: 500
      },
      chartOptions: {
        legend: {
          align: 'center',
          verticalAlign: 'bottom',
          layout: 'horizontal'
        },
        yAxis: {
          labels: {
            align: 'left',
            x: 0,
            y: -5
          },
          title: {
            text: null
          }
        },
        subtitle: {
          text: null
        },
        credits: {
          enabled: false
        }
      }
    }]
  }
});

$('#small').click(function() {
  chart.setSize(400, 300);
});

$('#large').click(function() {
  chart.setSize(600, 300);
});

var chartingOptions = {
    chart: {
        renderTo: 'container-teste-grafico',
        type: 'scatter'
    },
    xAxis: {
              type: 'datetime',
              tickPixelInterval: 150


          },
          tooltip: {
              formatter: function () {
                  return '<b>' + this.series.name + '</b><br/>' +
                      Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                      Highcharts.numberFormat(this.y, 2);
              }
          },
    series: [{
        name: 'Plot',
        data: []

      },
      {
        name: 'Plot2',
        data: []

      },
      {
        name: 'Plot3',
        data: []

      }]

};
var chart = new Highcharts.Chart(chartingOptions);

function update_test_grafico() 
{
    $.get("/graficos/1",{},
        function(data)
        {
            console.log(data);
            var temp = new Array();
            var str = new Array();
            str = String(data);
            temp = str.split(",");           
            $('#test-grafico').text(data);
            $('#test-str1').text(temp[0]);
            $('#test-str2').text(temp[1]);
            $('#test-str3').text(temp[2]);
            $('#test-str4').text(temp[3]);
            $('#test-str5').text(temp[4]);


            est = String(temp[4]);
            Xt = new Date(est.replace(' ', 'T')).getTime();
            Y1 = parseInt(temp[1]);
            Y2 = parseInt(temp[2]);
            Y3 = parseInt(temp[3]);



            chart.series[0].addPoint({x: Xt, y: Y1}, false);
            chart.series[1].addPoint({x: Xt, y: Y2}, false);
            chart.series[2].addPoint({x: Xt, y: Y3}, false);
            chart.redraw(); 

           var dat = (new Date()).getTime();
           $('#test-dat').text(dat);
           $('#test-dat-unx').text(Xt);
        });          
}

