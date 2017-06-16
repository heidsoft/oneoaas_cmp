/**
 * Created by heidsoft on 2017/6/16.
 */

var VCenterConfig = (function ($) {
    return {
        //创建vcenter账号
        createVCenterAccount: function () {
            var accountName =  $("#account_name").val();
            var accountPassword = $("#account_password").val();
            var vcenterHost = $("#vcenter_host").val();
            var vcenterVersion = $("#vcenter_version").val();
            console.log("VCenterConfig.createVCenterAccount....");
            $.ajax({
                url: '/vmware/api/createVCenterAccount',
                type: 'post',
                dataType: 'json',
                data: {
                    "accountName":accountName,
                    "accountPassword":accountPassword,
                    "vcenterHost":vcenterHost,
                    "vcenterVersion":vcenterVersion
                },
                success: function (data) {
                    console.log(data);
                },

            });

        },

    }
})($);

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
        url: '/vmware/api/getVcenterAccountList',
    },
    columnDefs: [
        {
            targets: 0,
            data: "test1",
        },
        {
            targets: 1,
            data: "test2",
        },
        {
            targets: 2,
            data: "test3",
        },
    ]

});

