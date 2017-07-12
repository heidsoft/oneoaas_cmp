/**
 * Created by heidsoft on 2017/6/16.
 * @description vcenter配置操作模块
 */

//vcenter 管理插件
var VCenterManage = (function ($,toastr) {
    return {
        init:function (tableId) {
            var VCenterManageRecord = $(tableId).DataTable({
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
                        'targets': 0,
                        'checkboxes': {
                            'selectRow': true
                        }
                    },
                    {
                        targets: 1,
                        data: "name",
                    },
                    {
                        targets: 2,
                        data: "vm_pathname",
                    },
                    {
                        targets: 3,
                        data: "guest_fullname",
                    },
                    {
                        targets: 4,
                        data: "power_state",
                    },
                    {
                        targets: 5,
                        data: "ipaddress",
                    },
                ],
                select: {
                    'style': 'multi'
                },
                order: [[ 1, 'asc' ]]
            });

            return VCenterManageRecord;
        },
        create:function () {
            //$('#rootwizard').show();
            var d = dialog({
                width: 600,
                title: '创建虚拟机',
                quickClose: true,
                content: $("#rootwizard"),
                ok: function() {
                    console.log(this)
                    // do something
                },
                cancelValue: '取消',
                cancel: function() {
                    console.log(this)
                    // do something
                },
                onshow: function() {
                    console.log(this)
                    // do something
                }
            });
            d.show();
        },
        clone:function () {

        },
        poweroff: function (data) {
            $.ajax({
                url: '/vmware/api/poweroff',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":83,
                },
                success: function (data) {
                    toastr.success(data.message);
                    // var d = dialog({
                    //     width: 440,
                    //     title: "提示",
                    //     content: '<div class="king-notice3 king-notice-success">'+
                    //     '<span class="king-notice-img"></span>'+
                    //     '<div class="king-notice-text">'+
                    //     '<p class="f24">创建成功</p>'+
                    //     '<p class="f12">'+
                    //     '<span class="king-notice3-color">3秒</span>后跳转至应用创建状态页面</p>'+
                    //     '</div>'+
                    //     '</div>',
                    // });
                    // d.show();
                }
            });
        },
        start: function (data) {
            $.ajax({
                url: '/vmware/api/start',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":83,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        },
        reboot: function (data) {
            $.ajax({
                url: '/vmware/api/reboot',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":83,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        },
        destroy: function (data) {
            $.ajax({
                url: '/vmware/api/destroy',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":32,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        },
        async: function (data) {
            $.ajax({
                url: '/vmware/api/asyncDemo',
                type: 'post',
                dataType: 'json',
                data: {
                    "id":32,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        }
    }
})($,window.toastr);

//扩展到jquery
//$.fn.extend(VCenterManage);
//扩展函数


$(document).ready(function(){

    //默认支持vcenter版本列表
    var vcenterVersionList = [
        {id:1,text:"5.0"},
        {id:2,text:"5.1"},
        {id:3,text:"5.5"},
        {id:4,text:"6.0"}
    ];
    $("#vcenter_version .select2_box").select2({ data: vcenterVersionList });
    $('#rootwizard').bootstrapWizard({'tabClass': 'nav nav-tabs'});
    $('#rootwizard').hide();

    VCenterManage.init('#vcenter_manage_record');
})




