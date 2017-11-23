//-------------------------------------------------------------------------------------
// -------------Criando do grafico de spline dinamico
//-------------------------------------------------------------------------------------

var chartingOptions = {
    chart: {
        renderTo: 'container-grafico-dinamico',
        type: 'spline',
              animation: Highcharts.svg,
    },
    xAxis: {
              tickAmount: 10,
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
        name: 'Tensao do Barramento',
        data: []

      },
      {
        name: 'Corrente consumida',
        data: []

      },
      {
        name: 'Temperatura',
        data: []

      }]

};
var chart = new Highcharts.Chart(chartingOptions);
//----------------------------------------------------------------------------------------
// ---------Fim do primeiro grafico
//----------------------------------------------------------------------------------------

//----------------------------------------------------------------------------------------
// ---------Criando do grafico de colunas
//----------------------------------------------------------------------------------------
var chartingOptions2 = {
 
            chart: {
                type: 'column',
                renderTo: 'container-grafico-colunas'
            },
            title: {
                text: 'Monthly Average Rainfall'
            },
            subtitle: {
                text: 'Source: WorldClimate.com'
            },
            xAxis: {
            type: 'category'
                
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Rainfall (mm)'
                }
            },
            
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                        name: 'Tokyo',
                        data: [
                                [1511409351721, 23.7],
                                [1511409387288, 16.1]
                              ]
            
                    }]
        };
var chart2 = new Highcharts.Chart(chartingOptions2);

//----------------------------------------------------------------------------------------
// ---------Fim do grafico de colunas
//----------------------------------------------------------------------------------------

$('#button2').click(function() 
{

            chart2.series[0].setData([[ 1511409422991,5],[1511409437340,50]]); //Atualiza colunas do grafic0
        });


   
function update_test_grafico() 
{
    $.get("/graficos/1",{},   //Solicita get ao servidor e aguarda a ultima lina do BD
        function(data)
        {
            var series = chart.series[0];

            Xt = new Date(data[0][4].replace(' ', 'T')).getTime();    //Converte de data para formato calendario Unix
            Y1 = parseInt(data[0][1]);        //Garante que os valores sejam inteiros
            Y2 = parseInt(data[0][2]);        //Garante que os valores sejam inteiros
            Y3 = parseInt(data[0][3]);        //Garante que os valores sejam inteiros

            chart.series[0].addPoint({x: Xt, y: Y1}, false);
            chart.series[1].addPoint({x: Xt, y: Y2}, false);
            chart.series[2].addPoint({x: Xt, y: Y3}, false);
            chart.redraw();

            if(series.data.length > 20)              //Se a quandidade de plotagens for maior que 20
            {
              chart.series[0].data[0].remove();      //Remove data 0 da plotagem 0
              chart.series[1].data[0].remove();      //Remove data 0 da plotagem 1
              chart.series[2].data[0].remove();      //Remove data 0 da plotagem 2
            }

            $('#test-tabela').text(Xt);
        });          
}

function update_20_grafico() 
{
    $.get("/graficos/20",{},
        function(data)
        {
          var tebela = new Array();
          tebela = data;
          $('#test-tabela').text(tebela[3][3]);


        });          
}



