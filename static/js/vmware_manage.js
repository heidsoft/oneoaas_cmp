/**
 * Created by heidsoft on 2017/6/16.
 * @description vcenter配置操作模块
 */

var VCenterConfig = (function ($) {
    return {
        //创建vcenter账号
        createVCenterAccount: function () {
            var accountName =  $("#account_name").val();
            var accountPassword = $("#account_password").val();
            var vcenterHost = $("#vcenter_host").val();
            var vcenterVersion = $("#vcenter_version .select2_box").select2("val");
            var vcenterPort = $("#vcenter_port").val();
            $.ajax({
                url: '/vmware/api/createVCenterAccount',
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
                    console.log(data);
                }
            });
        },
        //同步vcenter账号
        syncVCenterAccount: function (data) {

            $.ajax({
                url: '/vmware/api/syncVCenterAccount',
                type: 'post',
                dataType: 'json',
                data: {
                    "id":data,
                },
                success: function (data) {
                    console.log(data);
                }
            });
        }
    }
})($);

$(document).ready(function(){

    //默认支持vcenter版本列表
    var vcenterVersionList =[
        {id:1,text:"5.0"},
        {id:2,text:"5.1"},
        {id:3,text:"5.5"},
        {id:4,text:"6.0"}
    ];
    $("#vcenter_version .select2_box").select2({ data: vcenterVersionList });

    var VCenterManageRecord = $('#vcenter_manage_record').DataTable({
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
            url: '/vmware/api/getVcenterVirtualMachineList',
        },
        columnDefs: [
            {
                targets: 0,
                className: 'select-checkbox',
                data: "name",
            },
            {
                targets: 1,
                className: 'select-checkbox',
                data: "vm_pathname",
            },
            {
                targets: 2,
                className: 'select-checkbox',
                data: "guest_fullname",
            },
            {
                targets: 3,
                className: 'select-checkbox',
                data: "power_state",
            },
            {
                targets: 4,
                className: 'select-checkbox',
                data: "ipaddress",
            },
        ]

    });
})




