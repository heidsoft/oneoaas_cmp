/**
 * Created by heidsoft on 2017/6/16.
 * @description vcenter配置操作模块
 */

var VCenterConfig = (function ($,toastr) {
    return {
        //创建vcenter账号
        createVCenterAccount: function () {
            var accountName =  $("#account_name").val();
            var accountPassword = $("#account_password").val();
            var vcenterHost = $("#vcenter_host").val();
            var vcenterVersion = $("#vcenter_version .select2_box").select2("val");
            var vcenterPort = $("#vcenter_port").val();
            $.ajax({
                url: site_url+'vmware/api/createVCenterAccount',
                type: 'post',
                dataType: 'json',
                data: {
                    "accountName":accountName,
                    "accountPassword":accountPassword,
                    "vcenterHost":vcenterHost,
                    "vcenterPort":vcenterPort,
                    "vcenterVersion":vcenterVersion
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        },
        //同步vcenter账号
        syncVCenterAccount: function (data) {
            $.ajax({
                url: site_url+'vmware/api/syncVCenterAccount',
                type: 'post',
                dataType: 'json',
                data: {
                    "id":data,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        }
    }
})($,window.toastr);

$(document).ready(function(){

    //默认支持vcenter版本列表
    var vcenterVersionList =[
        {id:5.0,text:"5.0"},
        {id:5.1,text:"5.1"},
        {id:5.5,text:"5.5"},
        {id:6.0,text:"6.0"}
    ];
    $("#vcenter_version .select2_box").select2({ data: vcenterVersionList });

    var VCenterConfigRecord = $('#vcenter_config_record').DataTable({
        "bProcessing": true,                    //加载数据时显示正在加载信息
        "bServerSide": true,                    //指定从服务器端获取数据
        "bFilter": false,                       //不使用过滤功能
        "bLengthChange": false,                 //用户不可改变每页显示数量
        "iDisplayLength": 4,                    //每页显示8条数据
        "sPaginationType": "full_numbers",      //翻页界面类型
        "oLanguage": {                          //汉化
            "sLengthMenu": "每页显示 _MENU_ 条记录",
            "sZeroRecords": "没有检索到数据",
            "sInfo": "当前数据为从第 _START_ 到第 _END_ 条数据；总共有 _TOTAL_ 条记录",
            "sInfoEmtpy": "没有数据",
            "sProcessing": "正在加载数据...",
            "oPaginate": {
                "sFirst": "首页",
                "sPrevious": "上一页",
                "sNext": "下一页",
                "sLast": "尾页"
            }
        },
        "bInfo":false,//隐藏左下角分页显示信息
        "bServerSide": true,
        ajax: {
            url: site_url+'vmware/api/getVcenterAccountList',
        },
        columnDefs: [
            {
                targets: 0,
                data: "account_name",
            },
            {
                targets: 1,
                data: "account_password",
            },
            {
                targets: 2,
                data: "vcenter_host",
            },
            {
                targets: 3,
                data: "vcenter_port",
            },
            {
                targets: 4,
                data: "vcenter_version",
            },
            {
                targets: 5,
                data: "id",
                "render": function ( data, type, row ) {
                    var syncHtml = '<button class="btn btn-xs btn-info" ' ;
                    syncHtml+= ' onclick="VCenterConfig.syncVCenterAccount('+data+')" ';
                    syncHtml+= ' >同步</button> ';
                    return syncHtml;
                }
            }
        ]

    });
})




