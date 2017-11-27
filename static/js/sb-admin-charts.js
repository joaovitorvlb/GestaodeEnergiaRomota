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
                text: 'Relatorio de Media diaria '
            },
            subtitle: {
                text: 'enargia captada nos ultimas 7 dias'
            },
            xAxis: {
            type: 'datetime'
                
            },
            
          tooltip: {
              formatter: function () {
                  return '<b>' + this.series.name + '</b><br/>' +
                      Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                      Highcharts.numberFormat(this.y, 2);
              }
          },
            yAxis: {
                min: 0,
                title: {
                    text: 'Potencia (W)'
                }
            },
            
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                        name: 'Potencia (W)',
                        data: [ ]
            
                    }]
        };
var chart2 = new Highcharts.Chart(chartingOptions2);

//----------------------------------------------------------------------------------------
// ---------Fim do grafico de colunas
//----------------------------------------------------------------------------------------

$('#button2').click(function() 
{

            chart2.series[0].setData([
                                        [ 1511411609545 ,5 ],
                                        [ 1511411625470 ,50],
                                        [ 1511411635870 ,3 ],
                                        [ 1511411646270 ,45],
                                        [ 1511411656695 ,56],
                                        [ 1511411661895 ,22]
                                      ]); //Atualiza colunas do grafic0
        });

$(document).ready(
        function()
        {
            $.get("/media/8",{},
            function(data)
            {
                var x1 = new Date(data[0][3].replace(' ', 'T')).getTime();
                var x2 = new Date(data[1][3].replace(' ', 'T')).getTime();
                var x3 = new Date(data[2][3].replace(' ', 'T')).getTime();
                var x4 = new Date(data[3][3].replace(' ', 'T')).getTime();
                var x5 = new Date(data[4][3].replace(' ', 'T')).getTime();
                var x6 = new Date(data[5][3].replace(' ', 'T')).getTime();
                var x7 = new Date(data[7][3].replace(' ', 'T')).getTime();
                var x8 = new Date(data[7][3].replace(' ', 'T')).getTime();

                var y1 = parseInt(data[0][1]);
                var y2 = parseInt(data[1][1]);
                var y3 = parseInt(data[2][1]);
                var y4 = parseInt(data[3][1]);
                var y5 = parseInt(data[4][1]);
                var y6 = parseInt(data[5][1]);
                var y7 = parseInt(data[6][1]);
                var y8 = parseInt(data[7][1]);

                  
                $('#test-col').text("tchau");
              
              chart2.series[0].setData([
                                          [ x1 , y1 ],
                                          [ x2 , y2 ],
                                          [ x3 , y3 ],
                                          [ x4 , y4 ],
                                          [ x5 , y5 ],
                                          [ x6 , y6 ],
                                          [ x7 , y7 ],
                                          [ x8 , y8 ]
                                        ]); //Atualiza colunas do grafic0
              });
        })


   
function update_test_grafico() 
{
    $.get("/graficos/1",{},   //Solicita get ao servidor e aguarda a ultima lina do BD
        function(data)
        {
            var series = chart.series[0];

            Xt = new Date(data[0][3].replace(' ', 'T')).getTime();    //Converte de data para formato calendario Unix
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

            $('#test-str1').text(series.data.length);
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



