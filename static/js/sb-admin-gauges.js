//-------------------------------------------------------------------------------------
// -------------Criando o gauge de bateria
//-------------------------------------------------------------------------------------
var slider;
window.onload = function () 
{
    //widget model
    var jsonModel = {"Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":null,"JSBindingsText":null,"Name":"Instrument","RecalculateAll":false,"Smooth":true,"Stroke":null,"Style":"","ToolTipValue":null,"Visible":true,"Elements":[{"__type":"Rectangle:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"SolidFill:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":164,"name":null,"state":1,"value":0}},"JSBindingsText":"this.setCenter(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.45),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.5)));\u000athis.setSize(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.9),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.58)));\u000a","Name":"Rectangle1","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Center":{"Height":500,"Length":672.68120235368553,"Rotation":0.83798122500839,"Width":450,"X":450,"Y":500},"Size":{"Height":580,"Length":1070.7007051459339,"Rotation":0.57245981381805111,"Width":900,"X":900,"Y":580},"Angle":0},{"__type":"Rectangle:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"SolidFill:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":35,"name":null,"state":1,"value":0}},"JSBindingsText":"this.setSize(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.84),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.4)));\u000athis.setCenter(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.45),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.43)));\u000a","Name":"Rectangle2","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":35,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Center":{"Height":430,"Length":622.41465278381747,"Rotation":0.76267480255580722,"Width":450,"X":450,"Y":430},"Size":{"Height":400,"Length":930.37626796904055,"Rotation":0.4444192099010989,"Width":840,"X":840,"Y":400},"Angle":0},{"__type":"Guide:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":null,"JSBindingsText":"this.setEndPoint(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.85),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.425)));\u000athis.setStartPoint(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.05),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.425)));\u000a","Name":"Guide1","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":35,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Elements":[{"__type":"Scale:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":null,"JSBindingsText":null,"Name":"Scale1","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":35,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Elements":[{"__type":"Slider:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":null,"JSBindingsText":null,"Name":"Slider1","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":35,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Elements":[{"__type":"RangedLevel:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"MultiGradientFill:#PerpetuumSoft.Framework.Drawing","Angle":0,"Colors":[{"__type":"GradientColor:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":0,"name":null,"state":2,"value":4294934592},"Portion":0},{"__type":"GradientColor:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":65,"name":null,"state":1,"value":0},"Portion":0.42234169653524495},{"__type":"GradientColor:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":110,"name":null,"state":1,"value":0},"Portion":0.61350059737156515},{"__type":"GradientColor:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":45,"name":null,"state":1,"value":0},"Portion":1}]},"JSBindingsText":"this.setEndWidth((this.getInstrument().getByName('Instrument') .getSize() .getY()*0.37));\u000athis.setStartWidth((this.getInstrument().getByName('Instrument') .getSize() .getY()*0.37));\u000athis.setValue(this.getInstrument().getByName('Slider1').getAnimationValue());\u000a","Name":"RangedLevel1","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Colorizer":null,"Distance":-178.66183140223322,"Dock":0,"MaxLimitWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"MinLimitWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"OriginWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"Padding":0,"ValueWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":1,"Value":100},"Colors":[],"Divisions":6,"DivisionsStroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":10,"Color":{"knownColor":164,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"EndColor":{"knownColor":84,"name":null,"state":1,"value":0},"StartColor":{"knownColor":0,"name":null,"state":2,"value":4294531855},"AlignmentMode":0,"EndWidth":370,"StartWidth":370},{"__type":"Label:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"SolidFill:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":35,"name":null,"state":1,"value":0}},"JSBindingsText":"this.setCenter(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.45),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.7)));\u000athis.setText((PerfectWidgets.Framework.Utilities.BuiltIn.oldFormat(this.getInstrument().getByName('Slider1').getAnimationValue(),\"0\")+\"%\"));\u000a","Name":"Label1","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Center":{"Height":700,"Length":832.16584885466193,"Rotation":0.99945884696126985,"Width":450,"X":450,"Y":700},"Size":{"Height":100,"Length":316.22776601683796,"Rotation":0.32175055439664219,"Width":300,"X":300,"Y":100},"Angle":0,"Font":{"Bold":0,"FamilyName":"Microsoft Sans Serif","Italic":0,"Size":10,"Strikeout":0,"Underline":0},"Margins":{},"Text":"100%","TextAlign":32},{"__type":"RangedLevel:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"EmptyFill:#PerpetuumSoft.Framework.Drawing"},"JSBindingsText":"this.setEndWidth((this.getInstrument().getByName('Instrument') .getSize() .getY()*0.14));\u000athis.setStartWidth((this.getInstrument().getByName('Instrument') .getSize() .getY()*0.14));\u000a","Name":"RangedLevel2","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Colorizer":null,"Distance":-70,"Dock":1,"MaxLimitWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"MinLimitWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"OriginWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"Padding":0,"ValueWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":1,"Value":100},"Colors":[],"Divisions":12,"DivisionsStroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":10,"Color":{"knownColor":164,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"EndColor":{"knownColor":27,"name":null,"state":1,"value":0},"StartColor":{"knownColor":27,"name":null,"state":1,"value":0},"AlignmentMode":0,"EndWidth":140,"StartWidth":140},{"__type":"RangedLevel:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"EmptyFill:#PerpetuumSoft.Framework.Drawing"},"JSBindingsText":"this.setEndWidth((this.getInstrument().getByName('Instrument') .getSize() .getY()*0.37));\u000athis.setStartWidth((this.getInstrument().getByName('Instrument') .getSize() .getY()*0.37));\u000a","Name":"RangedLevel3","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Colorizer":null,"Distance":-178.66183140223322,"Dock":0,"MaxLimitWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"MinLimitWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"OriginWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":0,"Value":0},"Padding":0,"ValueWrapper":{"__type":"SmartValueWrapper:#PerpetuumSoft.Instrumentation.Model","Kind":1,"Value":100},"Colors":[],"Divisions":6,"DivisionsStroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":10,"Color":{"knownColor":164,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"EndColor":{"knownColor":27,"name":null,"state":1,"value":0},"StartColor":{"knownColor":27,"name":null,"state":1,"value":0},"AlignmentMode":0,"EndWidth":370,"StartWidth":370}],"MaxLimit":{"Kind":0,"Value":0},"MinLimit":{"Kind":0,"Value":0},"Step":0,"Value":100}],"Colorizer":null,"Maximum":100,"Minimum":0,"Reverse":false}],"Margins":{},"Align":0,"EndPoint":{"Height":425,"Length":950.32889043741068,"Rotation":0.46364760900080609,"Width":850,"X":850,"Y":425},"GuideDirection":0,"StartPoint":{"Height":425,"Length":427.93106921559223,"Rotation":1.4536875822280324,"Width":50,"X":50,"Y":425}},{"__type":"Rectangle:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"SolidFill:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":164,"name":null,"state":1,"value":0}},"JSBindingsText":"this.setCenter(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.939),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.5)));\u000athis.setSize(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.08),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.25)));\u000a","Name":"Rectangle3","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Center":{"Height":500,"Length":1063.8237635999676,"Rotation":0.48929379303620579,"Width":939,"X":939,"Y":500},"Size":{"Height":250,"Length":262.48809496813374,"Rotation":1.2610933822524404,"Width":80,"X":80,"Y":250},"Angle":0},{"__type":"Rectangle:#PerpetuumSoft.Instrumentation.Model","Active":true,"BreakEventsBubbling":false,"CssClass":{},"Fill":{"__type":"SolidFill:#PerpetuumSoft.Framework.Drawing","Color":{"knownColor":35,"name":null,"state":1,"value":0}},"JSBindingsText":"this.setCenter(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.95),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.5)));\u000athis.setSize(new PerfectWidgets.Framework.DataObjects.Vector((this.getInstrument().getByName('Instrument') .getSize() .getX()*0.02),(this.getInstrument().getByName('Instrument') .getSize() .getY()*0.15)));\u000a","Name":"Rectangle4","RecalculateAll":false,"Smooth":true,"Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":0,"name":null,"state":2,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1},"Style":"Default","ToolTipValue":null,"Visible":true,"Center":{"Height":500,"Length":1073.5455276791945,"Rotation":0.48447792903702319,"Width":950,"X":950,"Y":500},"Size":{"Height":150,"Length":151.32745950421557,"Rotation":1.4382447944982226,"Width":20,"X":20,"Y":150},"Angle":0}],"Enabled":true,"Focused":false,"GridStep":50,"IsFixed":false,"MeasureUnit":{},"Parameters":[],"ShowGrid":true,"Size":{"Height":1000,"Length":1414.2135623730951,"Rotation":0.78539816339744828,"Width":1000,"X":1000,"Y":1000},"SnapToGrid":true,"Styles":[{"__type":"Style:#PerpetuumSoft.Instrumentation.Styles","Fill":null,"Font":{"Bold":0,"FamilyName":"Microsoft Sans Serif","Italic":0,"Size":10,"Strikeout":0,"Underline":0},"Image":null,"Name":"Default","Stroke":{"__type":"SimpleStroke:#PerpetuumSoft.Framework.Drawing","Width":1,"Color":{"knownColor":35,"name":null,"state":1,"value":0},"DashLenght":5,"DotLenght":1,"SpaceLenght":2,"Style":1}}]}
    //creating widget
    var widget = new PerfectWidgets.Widget("battery_meter", jsonModel);
    //getting slider object
    slider = widget.getByName("Slider1");
}
//
function updateVal() {
    //set new slider value
    slider.setValue(document.getElementById("valbox").value);
 }

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



