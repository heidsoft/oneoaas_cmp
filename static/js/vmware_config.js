/**
 * Created by heidsoft on 2017/6/16.
 * @description vcenter配置操作模块
 */

var VCenterConfig = (function ($,toastr) {
    return {
        accountTable:null,
        selectedRows:[],
        init:function () {
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

            var VCenterConfigRecord = $('#vcenter_config_record').DataTable({
                paging: true, //隐藏分页
                ordering: false, //关闭排序
                info: false, //隐藏左下角分页信息
                searching: false, //关闭搜索
                pageLength : 5, //每页显示几条数据
                lengthChange: false, //不允许用户改变表格每页显示的记录数
                language: language, //汉化
                sLoadingRecords:true,
                ajax: {
                    url: site_url+'vmware/api/getVcenterAccountList',
                },
                'columnDefs': [
                    {
                        'targets': 0,
                        'className': 'dt-head-center dt-body-center',
                        'checkboxes': {
                            'selectRow': true
                        }
                    }
                ],
                'select': {
                    'style': 'multi'
                },
                columns: [
                    {
                        data:'id',
                    },
                    {
                        title : '账号名称',
                        data: "account_name",
                    },
                    {
                        title : 'VCenter主机',
                        data: "vcenter_host",
                    },
                    {
                        title : 'VCenter版本',
                        data: "vcenter_port",
                    },
                    {
                        title : 'VCenter版本',
                        data: "vcenter_version",
                    },
                    {
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

            this.accountTable = VCenterConfigRecord;
            return VCenterConfigRecord;
        },
        //创建vcenter账号
        createVCenterAccount: function () {
            var accountName =  $("#account_name").val();
            var accountPassword = $("#account_password").val();
            var vcenterHost = $("#vcenter_host").val();
            var vcenterVersion = $("#vcenter_version .select2_box").select2("val");
            var vcenterPort = $("#vcenter_port").val();
            if(accountName===""){
                toastr.warning("VCenter账号不能为空");
                return
            }

            if(accountPassword===""){
                toastr.warning("VCenter账号密码不能为空");
                return
            }

            if(vcenterHost===""){
                toastr.warning("VCenter主机不能为空");
                return
            }

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
                    VCenterConfig.accountTable.ajax.reload( null, false );
                }
            });
        },
        beforeAction:function(){
            var rows_selected = this.accountTable.column(0).checkboxes.selected();
            if(typeof rows_selected === 'undefined' || rows_selected.length === 0){
                toastr.warning("请选择账号资源");
                return false
            }
            var rowIds = this.selectedRows =[];
            $.each(rows_selected, function(index, rowId){
                rowIds.push(rowId);
            });
            this.selectedRows = rowIds;
            return true
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
        },
        //删除账号
        deleteAccount: function () {
            if(!this.beforeAction()){
                return;
            }
            $.ajax({
                url: site_url+'vmware/api/deleteAccount',
                type: 'post',
                dataType: 'json',
                data: {
                    "id":this.selectedRows[0],
                },
                success: function (data) {
                    toastr.success(data.message);
                    VCenterConfig.accountTable.ajax.reload( null, false );
                }
            });
        },
        //清除账号下所有资源
        desctroyAccount: function () {
            toastr.warning("蓝鲸社区版暂不支持该功能,如果需要请联系OneOaaS");
        },
        //设置同步策略
        setSyncPolicy: function (data) {
            toastr.warning("蓝鲸社区版暂不支持该功能,如果需要请联系OneOaaS");
        }
    }
})($,window.toastr);

var account_info_vue = new Vue({
    el: '#account_info',
    data: {
        cloudProviderList:{
            data:[
                {id:'qcloud',text:"腾讯云"},
                {id:'ucloud',text:"UCLOUD"},
                {id:'vcenter',text:"VMware"},
                // {id:'aliyun',text:"阿里云"}
            ],
            cloudProviderSelected:'vcenter',
        },
        vcenterVersionList: [
            {id:5.0,text:"5.0"},
            {id:5.1,text:"5.1"},
            {id:5.5,text:"5.5"},
            {id:6.0,text:"6.0"}
        ]
    },
    created: function () {
        var _self = this;
        $("#cloud_provider .select2_box").select2({
            placeholder: "请选择云提供商",
            allowClear: true,
            data: this.cloudProviderList.data
        });
        $("#vcenter_version .select2_box").select2({
            placeholder: "请选择VCenter版本",
            allowClear: true,
            data: this.vcenterVersionList
        });


        $("#cloud_provider .select2_box").on("change", function (e) {
            _self.cloudProviderList.cloudProviderSelected = $("#cloud_provider .select2_box").select2("val");
        });

        VCenterConfig.init();
    },
    watch: {
        cloudProviderSelected: {
            handler(newValue, oldValue) {
                console.log("aaaaaaaaaaaaa");
                console.log(newValue);
                console.log("bbbbbbbbbbbbb");
                console.log(oldValue);
            },
            deep: true
        }
    },
    ready:{
        
    }
})

// $(document).ready(function(){
//     $("#cloud_provider .select2_box").on("change", function (e) { console.log("change"); });
// })




