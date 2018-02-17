//----------------------------------------------------------------------------------------
// ---------Controle do painel
//----------------------------------------------------------------------------------------

function a1_onclick(id) {
    $.get( "/servo/" + id, function( data ) {  });  
}
//----------------------------------------------------------------------------------------
// ---------Update geral e dos gauges
//----------------------------------------------------------------------------------------
$(document).ready(
    function()
    {
        autoupdate_geral();
        update_grafico();
    })


function update()
{
    $.get("/update",{},
    function(data)
    {
        console.log(data);

        $('#p_disc').text(data[5].toFixed(2) + ' %');
        $('#cpu_perc').text(data[3].toFixed(2) + ' %');
        $('#p_mem').text(data[4].toFixed(2) + ' %');
        

        slider.setValue(data[4].toFixed(2));

        vr = parseInt(data[6]) / 1000;
        point =gauges1.series[0].points[0];
        point.update(vr);

        vr = parseInt(data[7]) / 1000;
        point =gauges2.series[0].points[0];
        point.update(vr);

        vr = parseInt(data[8]) / 1000;
        point =gauges3.series[0].points[0];
        point.update(vr);     
        
        vr = parseInt(data[0]) / 1000;
        point =gauges4.series[0].points[0];
        point.update(vr);

        vr = parseInt(data[1]) / 1000;
        point =gauges5.series[0].points[0];
        point.update(vr);

        vr = parseInt(data[2]) / 1000;
        point =gauges6.series[0].points[0];
        point.update(vr);

        vr = parseInt(data[9])
        point =gauges7.series[0].points[0];
        point.update(vr);

        vr = parseInt(data[10])
        point =gauges8.series[0].points[0];
        point.update(vr);
    });
}


function autoupdate_geral()
{
    update();
    setTimeout(function(){autoupdate_geral();}, 300);
}

function update_grafico()
{
    update_test_grafico();
    setTimeout(function(){update_grafico();}, 5000);
}

//----------------------------------------------------------------------------------------
// ---------Inicio dos eventos dos graficos
//----------------------------------------------------------------------------------------

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
                var x7 = new Date(data[6][3].replace(' ', 'T')).getTime();
                var x8 = new Date(data[7][3].replace(' ', 'T')).getTime();

                var y1 = parseInt(data[0][1]);
                var y2 = parseInt(data[1][1]);
                var y3 = parseInt(data[2][1]);
                var y4 = parseInt(data[3][1]);
                var y5 = parseInt(data[4][1]);
                var y6 = parseInt(data[5][1]);
                var y7 = parseInt(data[6][1]);
                var y8 = parseInt(data[7][1]);

              
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


var v_data = new Array();

function update_test_grafico() 
{
    $.get("/graficos/1",{},   //Solicita get ao servidor e aguarda a ultima lina do BD
        function(data)
        {
            var series = chart.series[0];

            Xt = new Date(data[0][5].replace(' ', 'T')).getTime();    //Converte de data para formato calendario Unix
            Y1 = parseFloat(data[0][1]);        //Garante que os valores sejam inteiros
         

            if(v_data != Xt)
            {
                chart.series[0].addPoint({x: Xt, y: Y1}, false);
                chart.redraw();
                v_data = Xt;
            }


            if(series.data.length > 20)              //Se a quandidade de plotagens for maior que 20
            {
              chart.series[0].data[0].remove();      //Remove data 0 da plotagem 0
              chart.series[1].data[0].remove();      //Remove data 0 da plotagem 1
              chart.series[2].data[0].remove();      //Remove data 0 da plotagem 2
            }

            $('#test-str1').text(series.data.length);
            $('#test-str2').text(teste);
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
