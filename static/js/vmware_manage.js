/**
 * Created by heidsoft on 2017/6/16.
 * @description vcenter配置操作模块
 */

var VCenterManage = (function ($) {
    return {
        //同步vcenter账号
        poweroff: function (data) {
            $.ajax({
                url: '/vmware/api/poweroff',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":32,
                },
                success: function (data) {
                    console.log(data);
                    alert(data.message);
                }
            });
        },
        start: function (data) {
            $.ajax({
                url: '/vmware/api/start',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":32,
                },
                success: function (data) {
                    console.log(data);
                    alert(data.message);
                }
            });
        },
        reboot: function (data) {
            $.ajax({
                url: '/vmware/api/reboot',
                type: 'post',
                dataType: 'json',
                data: {
                    "vmId":32,
                },
                success: function (data) {
                    console.log(data);
                    alert(data.message);
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
                    console.log(data);
                    alert(data.message);
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

    $('#select_all_vm').click(function () {
        var state = this.checked;
        var cols = VCenterManageRecord.column(0).nodes();

    })
})




