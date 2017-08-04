/**
 * Created by heidsoft on 2017/6/16.
 * @description vcenter配置操作模块
 */


//vcenter 管理插件
var VCenterManage = (function ($,toastr) {
    return {
        //初始化虚拟机表格对象
        vmTable:null,
        //被选择记录ID
        selectedRows:[],
        //初始化虚拟机表格
        init:function (tableId) {

            var language = {
                search: '搜索：',
                lengthMenu: "每页显示 _MENU_ 记录",
                zeroRecords: "没找到相应的数据！",
                info: "分页 _PAGE_ / _PAGES_",
                infoEmpty: "暂无数据！",
                infoFiltered: "(从 _MAX_ 条数据中搜索)",
                paginate: {
                    first: '<<',
                    last: '>>',
                    previous: '上一页',
                    next: '下一页',
                }
            }

            var VCenterManageRecord = $(tableId).DataTable({
                paging: true, //隐藏分页
                ordering: false, //关闭排序
                info: false, //隐藏左下角分页信息
                searching: false, //关闭搜索
                pageLength : 5, //每页显示几条数据
                lengthChange: false, //不允许用户改变表格每页显示的记录数
                language: language, //汉化
                ajax: {
                    url: site_url+'vmware/api/getVcenterHostList',
                },
                columns: [
                    {
                        data: "name",
                        title:"主机名称"
                    },
                    {
                        data: "api_type",
                        title:"API类型"
                    },
                    {
                        data: "api_version",
                        title:"API版本"
                    },
                    {
                        data: "build",
                        title:"构建时间"
                    },
                    {
                        data: "full_name",
                        title:"全称"
                    },
                    {
                        data: "instance_uuid",
                        title:"uuid"
                    },
                    {
                        data: "license_product_name",
                        title:"证书产品名称"
                    },
                    {
                        data: "license_product_version",
                        title:"证书产品版本"
                    },
                    {
                        data: "locale_version",
                        title:"本地版本"
                    },
                    {
                        data: "os_type",
                        title:"操作系统类型"
                    },
                    {
                        data: "vendor",
                        title:"厂商"
                    },
                    {
                        data: "version",
                        title:"版本"
                    },
                ],
            });

            this.vmTable = VCenterManageRecord;

            //设置button
            new $.fn.dataTable.Buttons( VCenterManageRecord, {
                buttons: [
                    {
                        extend: 'copyHtml5',
                        text: '拷贝表格'
                    },
                    {
                        extend: 'excelHtml5',
                        text: '导出Excel'
                    },
                    {
                        extend: 'pdfHtml5',
                        text: '导出PDF'
                    },
                    {
                        extend: 'csvHtml5',
                        text: '导出CVS'
                    },
                ],
            } );

            //将button放置到底部
            var tableContainer = VCenterManageRecord.buttons().container();
            tableContainer.appendTo(
                VCenterManageRecord.table().container()
            );

            return VCenterManageRecord;
        }
    }
})($,window.toastr);

//扩展到jquery
//$.fn.extend(VCenterManage);
//扩展函数

function open_host_side(){
    var sideContent = $('#host_side');
    sideContent.removeClass('hidden');
    getComputedStyle(document.querySelector('body')).display;
    sideContent.find('#close').addClass('open');
    sideContent.find('.shield-edit').addClass('open');
    sideContent.find('#shield-detail').removeClass('hidden');

    $('article.shield-content').css('overflow', 'hidden');
}

function close_host_side(){
    var sideContent = $('#host_side');
    sideContent.find('.shield-edit').removeClass('open').children('#shield-detail').addClass('hidden');
    sideContent.find('#close').removeClass('open');
    setTimeout(function(){
        sideContent.addClass('hidden');
        $('article.shield-content').css('overflow', 'auto');
    }, 300);

}

function make_single_graphs(){
    $(".single-contain").each(function(){
        console.log("aaaaaaaaaaaaaaa");
        make_contain_graph($(this));
    });
}

function make_contain_graph(contain, _type){
    var chart_div = contain.find(".line-chart");
    var host_id = chart_div.attr("data-host_id");
    if (!host_id){
        host_id = hosts_view.checked_host_index_table.id;
    }
    var params = {
        graph_date: _type?$("#multiple_graph_date").val():$("#single_graph_date").val(),
        host_id: host_id,
        index_id: chart_div.attr("data-index_id"),
        dimension_field_value: chart_div.attr("data-dimension_field_value")
    };

    chart_div.html('<img class="graph-loading" alt="loadding" src="'+static_url+'img/hourglass_36.gif" style="margin-top: 75px;margin-left:45%;">');

    $.get(site_url+'vmware/api/getVcenterAccountList', params, function(res){
        chart_div.html("");

        var  resp ={
            "msg": "",
            "message": "",
            "data": {
                "echo_sql": "",
                "data": {
                    "min_y": 0,
                    "pointStart": 1501804800000,
                    "series": [
                        {
                            "count": [
                                1.46,
                                0.87,
                                0.26,
                                0.19,
                                0.18
                            ],
                            "x_axis_list": [
                                "2017-08-04 00:00:00",
                                "2017-08-04 00:01:00",
                                "2017-08-04 00:02:00",
                                "2017-08-04 00:03:00",
                                "2017-08-04 00:04:00"
                            ],
                            "name": "cpu总使用率",
                            "type": "spline",
                            "delay_info": {
                                "1501806600": true,
                                "1501808640": true,
                                "1501814820": true,
                                "1501816860": true,
                                "1501818900": true
                            },
                            "zones": [],
                            "zoneAxis": "x",
                            "data": [
                                [
                                    1501804800000,
                                    1.46
                                ],
                                [
                                    1501804860000,
                                    0.87
                                ],
                                [
                                    1501804920000,
                                    0.26
                                ],
                                [
                                    1501804980000,
                                    0.19
                                ],
                                [
                                    1501805040000,
                                    0.18
                                ]
                            ]
                        }
                    ],
                    "x_axis": {
                        "minRange": 3600000,
                        "type": "datetime"
                    },
                    "pointInterval": 300000,
                    "show_percent": false,
                    "series_name_list": [
                        "cpu总使用率"
                    ],
                    "chart_type": "spline",
                    "color_list": "",
                    "unit": "%",
                    "max_y": 5.93
                },
                "update_time": "2017-08-04 17:06:06"
            },
            "result": true
        }
        if(resp.result){
            var chart_data =resp.data.data;
            console.log(chart_data);
            var series_info = {};
            for (var i = 0; i < chart_data.series.length; i++) {
                series_info[chart_data.series[i].name] = chart_data.series[i];
            }
            Hchart.spline(chart_data, chart_div[0], series_info);
        }else{
            var error_tips_html = '<div class="chart-error">' +
                '<span class="error-mark">' +
                '<i class="fa fa-exclamation"></i>' +
                '</span><span class="error-text">'+
                res.message + '</span></div>';
            //chart_div.html(error_tips_html);
            chart_div.html(res.message);
        }
    }, 'json');
}


//基于vue实例,使用单向数据绑定
var hosts_view = new Vue({
    el: '#host_side',
    data: {
        checked_host_index_table:{},//选择主机
    },
    created:function () {

    },
    methods: {

    },
    watch: {
        'checked_host_index_table.length': {
            handler: function(newVal,oldVal) {
                if (this.checked_host_index_table.name !=='' ){
                    console.log(checked_host_index_table);
                    make_single_graphs();
                }
            },
            deep: true,
        },
    }

});



$(document).ready(function(){

    VCenterManage.init('#host_manage_record');

    $('#host_manage_record').on( 'click', 'tr', function () {
        var currentHost = VCenterManage.vmTable.row( this ).data();
        hosts_view.checked_host_index_table=currentHost;
        open_host_side();
    });

    $("#host_side").find("#cancel").click(function(){
        close_host_side();
    });


    $('#close, #sideContent').on('click', function(event){
        if($(event.target).attr('data-type') == 'close') {
            close_host_side();
        }
    });

})




