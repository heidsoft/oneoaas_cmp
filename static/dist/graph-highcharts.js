function get_line_chart_opt(t,e){var r={colors:["#27C24C","#CAE1FF","#CDCDB4","#FE0000","#C3017C"],title:{text:null},subtitle:{text:null},chart:{type:t.data.data.chart_type,zoomType:"x"},plotOptions:{spline:{marker:{threshold:0,symbol:"circle",radius:1,enabled:!0}},line:{marker:{symbol:"circle",radius:1}},series:{}},credits:{enabled:!0,text:"",href:"###"},xAxis:t.data.data.x_axis,yAxis:[{title:{enabled:!1},min:0,gridLineDashStyle:"LongDash",allowDecimals:!0,plotLines:[],opposite:!1}],tooltip:{xDateFormat:"%Y-%m-%d %H:%M:%S",followPointer:!0,followTouchMove:!0,crosshairs:{width:1,color:"#e2e2e2"},shared:!0,useHTML:!0,headerFormat:"<small>{point.key}</small><table>",pointFormatter:function(){var t="";if(this.series.data.data.zoneAxis){var e=this.x/1e3;this.series.userOptions.delay_info[e]&&(t='<font color="#f3b760">(数据延时)</font>')}return'<tr><td style="color: '+this.series.color+'">'+this.series.name+': </td><td style="color: #FFFFFF;"><b>'+this.y+t+"</b></td></tr>"},footerFormat:"</table>"},series:t.data.data.series[0].data};if(r.plotOptions.pointInterval=t.pointInterval,r.plotOptions.pointStart=t.pointStart,36e5==t.pointInterval&&(r.xAxis.labels={formatter:function(){return Highcharts.dateFormat("%m/%d",this.value)}}),r.rangeSelector={buttons:[{count:1,type:"minute",text:"1M"},{count:5,type:"minute",text:"5M"},{type:"all",text:"All"}],inputEnabled:!1,selected:0},t.plot_line_range){var o=t.plot_line_range.split("-"),i=""==o[0]?0:parseInt(o[0]),a=""==o[1]?0:parseInt(o[1]);a?(r.yAxis[0].max=a+a/10>t.max_y?a+a/10:t.max_y,r.yAxis[0].plotLines=[{value:i,color:"green",dashStyle:"shortdash",width:2,label:{text:i}},{value:a,color:"red",dashStyle:"shortdash",width:2,label:{text:a}}]):(r.yAxis[0].max=i+i/10>t.max_y?i+i/10:t.max_y,r.yAxis[0].plotLines=[{value:i,color:"red",dashStyle:"shortdash",width:2,label:{text:i}}])}if(t.yaxis_range){var l=t.yaxis_range.split(":"),s=isNaN(parseInt(l[0]))?"":parseInt(l[0]),n=isNaN(parseInt(l[1]))?"":parseInt(l[1]);s&&(r.yAxis[0].min=s),n&&(r.yAxis[0].max=n)}return t.unit&&(r.yAxis[0].labels={format:"{value}"+t.unit},r.tooltip.pointFormatter=function(){var e="";if(this.series.zoneAxis){var r=this.x/1e3;this.series.userOptions.delay_info[r]&&(e='<font color="#f3b760">(数据延时)</font>')}return'<tr><td style="color: '+this.series.color+'">'+this.series.name+': </td><td style="color: #FFFFFF;"><b>'+this.y+t.unit+e+"</b></td></tr>"}),t.show_label||(r.labels={enabled:!1}),e&&(ready_info[e]=!1,r.plotOptions.spline.animation={complete:function(){ready_info[e]=!0}}),r}function get_line_chart_monitor_opt(t,e){return{colors:["#f45b5b","#8085e9","#8d4654","#7798BF","#aaeeee","#ff0066","#eeaaee","#55BF3B","#DF5353","#7798BF","#aaeeee"],title:{text:null},subtitle:{text:null},credits:{enabled:!0,text:"",href:"###"},chart:{backgroundColor:null,style:{fontFamily:"Signika, serif"}},tooltip:{xDateFormat:"%Y-%m-%d %H:%M:%S",followPointer:!0,followTouchMove:!0,crosshairs:{width:1,color:"#e2e2e2"},shared:!0,useHTML:!0,headerFormat:"<small>{point.key}</small><table>",pointFormatter:function(){return'<tr><td style="color: #FFFFFF;"><b>'+this.y+"%</b></td></tr>"},footerFormat:"</table>"},legend:{itemStyle:{fontWeight:"bold",fontSize:"13px"}},xAxis:t.x_axis,yAxis:{min:0,title:{text:"利用率"},labels:{formatter:function(){return this.value+"%"}},plotLines:[{value:0,width:1,color:"#808080"}]},plotOptions:{spline:{marker:{threshold:0,symbol:"circle",radius:1,enabled:!0}},line:{marker:{symbol:"circle",radius:1}},series:{}},tooltip:{xDateFormat:"%Y-%m-%d %H:%M:%S",valueDecimals:2},navigator:{xAxis:{gridLineColor:"#D0D0D8"}},rangeSelector:{buttonTheme:{fill:"white",stroke:"#C0C0C8","stroke-width":1,states:{select:{fill:"#D0D0D8"}}}},scrollbar:{trackBorderColor:"#C0C0C8"},background2:"#E0E0E8",series:t.series}}Highcharts.theme_default={lang:{resetZoom:"重置",resetZoomTitle:"重置缩放"},colors:["#f6bb42","#4a89dc","#3bafda","#fc695e","#967adc","#64c256"],chart:{style:{fontFamily:"Arial, sans-serif, SimSun"}},title:{text:""},credits:{enabled:!1},xAxis:{gridLineColor:"#ebebeb",gridLineWidth:0,tickWidth:0,lineColor:"#ebebeb"},yAxis:{floor:"",ceiling:"",gridLineColor:"#ebebeb"},tooltip:{borderWidth:0,backgroundColor:"rgba(0,0,0,0.7)",shadow:!1,style:{color:"#ffffff"}},plotOptions:{line:{marker:{symbol:"circle",radius:2}}},series:{cropThreshold:1500}};var Hchart={make_graph:function(t,e,r){$(this).attr(t.chart_type)(t,e,r),Hchart.after_graphed(t,e)},after_graphed:function(t,e){$(e).highcharts()},line:function(t,e,r){$(e).highcharts(get_line_chart_monitor_opt(t,r))},spline:function(t,e,r){Hchart.line(t,e,r)}};ready_info={};