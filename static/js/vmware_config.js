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
                            'selectRow': false
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
                        title : '云厂商',
                        data: "cloud_provider",
                    },
                    {
                        title: '操作',
                        data: "id",
                        "render": function (data, type, row,meta) {
                            var syncHtml = '<button class="btn btn-xs btn-info ml10" onclick="VCenterConfig.syncVCenterAccount('+data+')"><i class="fa fa-history mr5"></i>同步</button>';
                            syncHtml+='<button class="btn btn-xs btn-info ml10" onclick="VCenterConfig.showAccountDetail('+ meta.row+')"><i class="mr5">…</i>详情</button>';
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
            var vcenterAccountName =  $("#vcenter_account_name").val();
            var vcenterAccountPassword = $("#vcenter_account_password").val();
            var vcenterHost = $("#vcenter_host").val();
            var vcenterVersion = $("#vcenter_version .select2_box").select2("val");
            var vcenterPort = $("#vcenter_port").val();
            var vmwareForm = $('#vmware_form');

            if(vcenterAccountName==="" || vcenterAccountPassword==="" || vcenterHost==="" || vcenterPort===""){
                return
            }
            if(vcenterVersion===""){
               toastr.warning("版本不能为空"); // form 那儿不能出现提示信息，此处作补充
               return
            }

            $.ajax({
              url: site_url+'vmware/api/createVCenterAccount',
              type: 'post',
              dataType: 'json',
              data: {
                  "cloudProvider":"vmware",
                  "accountName":vcenterAccountName,
                  "accountPassword":vcenterAccountPassword,
                  "vcenterHost":vcenterHost,
                  "vcenterPort":vcenterPort,
                  "vcenterVersion":vcenterVersion
               },
              success: function (data) {
                  toastr.success(data.message);
                  VCenterConfig.accountTable.ajax.reload( null, false );
                  vmwareForm.trigger("reset");
                  $("#vcenter_version .select2_box").select2("val","");
               }
            });
        },

        //创建Tencent账号
        createQcloudAccount: function () {
            var qcloudAccountName =  $("#qcloud_account_name").val();
            var qcloudSecretId = $("#qcloud_secret_id").val();
            var qcloudSecretKey = $("#qcloud_secret_key").val();
            //var qcloudVersion = $("#qcloud_version .select2_box").select2("val"); // 腾讯版本号预留字段
            var qcloudForm = $('#qcloud_form');

            if(qcloudAccountName==="" || qcloudSecretId==="" || qcloudSecretKey===""){
                return
            }
          /*  if(qcloudVersion===""){
               toastr.warning("版本不能为空");
               return
            }*/
            $.ajax({
              url: site_url+'vmware/api/createVCenterAccount',
              type: 'post',
              dataType: 'json',
              data: {
                  "cloudProvider":"qcloud",
                  "accountName":qcloudAccountName,
                  "cloudPublicKey":qcloudSecretId,
                  "cloudPrivateKey":qcloudSecretKey,
                  //"vcenterVersion":qcloudVersion
               },
              success: function (data) {
                  toastr.success(data.message);
                  VCenterConfig.accountTable.ajax.reload( null, false );
                  qcloudForm.trigger("reset");
                  // $("#qcloud_version .select2_box").select2("val","");
               }
            });
        },

        //创建Ucloud账号
        createUcloudAccount: function () {
            var accountName =  $("#ucloud_account_name").val();
            var ucloudPublicKey = $("#ucloud_public_key").val();
            var ucloudPrivateKey = $("#ucloud_private_key").val();
            var ucloudProjectId = $("#ucloud_project_id").val();
            var ucloudRegion = $("#ucloud_region .select2_box").select2("val");
            var ucloudForm = $("#ucloud_form");
            if(accountName==="" || ucloudPublicKey==="" || ucloudPrivateKey==="" || ucloudProjectId===""){
                return
            }
            if(ucloudRegion===""){
               toastr.warning("区域不能为空");
               return
            }
            $.ajax({
               url: site_url+'vmware/api/createVCenterAccount',
               type: 'post',
               dataType: 'json',
               data: {
                  "cloudProvider":"ucloud",
                  "accountName":accountName,
                  "cloudPublicKey":ucloudPublicKey,
                  "cloudPrivateKey":ucloudPrivateKey,
                  "projectId":ucloudProjectId,
                  "cloudRegion":ucloudRegion,
               },
               success: function (data) {
                  toastr.success(data.message);
                  VCenterConfig.accountTable.ajax.reload( null, false );
                  ucloudForm.trigger("reset");
                  $("#ucloud_region .select2_box").select2("val","");
               },
               error:function (err1,err2,err3) {
                  console.log(err1);
                  console.log(err2);
                  console.log(err3);
               }
            });
        },

        //同步VCenter账号
        syncVCenterAccount: function (data,cloudProvider) {
            var progressbarShow = dialog({
                cancel: false,
                padding: 0,
                width:500,
                content:'<div id="progressbar"></div>'
            });
            $( "#progressbar" ).progressbar({
                value: false
            });
            progressbarShow.showModal();
            $.ajax({
                url: site_url+'vmware/api/syncCloudAccount',
                type: 'post',
                dataType: 'json',
                data: {
                    "id":data,
                },
                success: function (data) {
                    progressbarShow.remove();
                    if(data.result){
                        toastr.success(data.message);
                    }else{
                        toastr.error(data.message);
                    }
                }
            });
        },

        beforeAction:function(){
            var rows_selected = this.accountTable.column(0).checkboxes.selected();
            if(typeof rows_selected === 'undefined' || rows_selected.length === 0){
                toastr.warning("请选择账号资源");
                return false
            }
            var rowIds = this.selectedRows ="";
            $.each(rows_selected, function(index, rowId){
                rowIds+=rowId+",";
            });
            this.selectedRows = rowIds;
            return true
        },
        //删除账号
        deleteAccount: function () {
            if(!this.beforeAction()){
                return;
            }
            var delAccount = dialog({
                width: 260,
                title: '提示',
                content: '确认删除？',
                okValue: '确定',
                ok: function() {
                    $.ajax({
                        url: site_url+'vmware/api/deleteAccount',
                        type: 'post',
                        dataType: 'json',
                        data: {
                            "id":VCenterConfig.selectedRows, //别人要删除多个怎么办？
                        },
                        success: function (data) {
                            toastr.success(data.message);
                            VCenterConfig.accountTable.ajax.reload( null, false );
                        }
                    });
                },
                cancelValue: '取消',
                cancel: function() {},
                onshow: function() {},
            });
            delAccount.show();
        },
        //清除账号下所有资源
        desctroyAccount: function () {
            toastr.warning("蓝鲸社区版暂不支持该功能,如果需要请联系OneOaaS");
        },
        //设置同步策略
        setSyncPolicy: function (data) {
            toastr.warning("蓝鲸社区版暂不支持该功能,如果需要请联系OneOaaS");
        },
        // 侧边栏详情
        showAccountDetail: function(rowIndex){
            var tableData = VCenterConfig.accountTable.rows().data();
            account_detail_vue.vcenterAccountData=tableData[rowIndex];
            account_detail_vue.showDetailSide();
        }
    }
})($,window.toastr);

var account_detail_vue = new Vue({
    el: '#vcenterDetails',
    data: {
        vcenterAccountData:{},
        passwordShow:false,
    },
    methods:{
        showDetailSide:function () {
            $("#vcenterDetailsShade").removeClass('hidden');
            $("#vcenterDetails").removeClass('animated fadeOutRight');
        }
    },
    created:function () {
        $('#close').on('click', function(event){
            $("#vcenterDetails").addClass('animated fadeOutRight');
            setTimeout(function(){
                $("#vcenterDetailsShade").addClass('hidden');
        },500)
        });
    }
});

var account_info_vue = new Vue({
    el: '#vcenter_config',
    data: {
        vcenterIsShow: true,
        qcloudIsShow: false,
        ucloudIsShow: false,
        cloudProviderSelected: '',
        vcenterVersionList: [
            {id:5.0,text:"5.0"},
            {id:5.1,text:"5.1"},
            {id:5.5,text:"5.5"},
            {id:6.0,text:"6.0"}
        ],
/* 
        qcloudVersionList: [
            {id:5.0,text:"5.0"},
            {id:5.1,text:"5.1"},
            {id:5.5,text:"5.5"},
            {id:6.0,text:"6.0"}
        ] 
*/        
        ucloudRegionList: [
            {id:"cn-bj1",text:"北京一"},
            {id:"cn-bj2",text:"北京二"},
            {id:"cn-zj",text:"浙江"},
            {id:"cn-sh1",text:"上海一"},
            {id:"cn-sh2",text:"上海二"},
            {id:"cn-gd",text:"广州"},
            {id:"hk",text:"香港"},
            {id:"us-ca",text:"洛杉矶"},
            {id:"us-ws",text:"华盛顿"},
            {id:"ge-fra",text:"法兰克福"},
            {id:"th-bkk",text:"曼谷"},
            {id:"kr-seoul",text:"首尔"},
            {id:"sg",text:"新加坡"},
            {id:"tw-kh",text:"台湾"}
        ]
    },
    methods: {
       onSubmit:function (e) {
          e.preventDefault();
       },
       watchProviderSelected:function(newValue, oldValue) {
            console.log("newVersion：");
            console.log(newValue);
            console.log("oldVersion：");
            console.log(oldValue);
        }
    },
    created: function () {
        var _self = this;
        $("#vcenter_version .select2_box").select2({
            placeholder: "请选择VCenter版本",
            allowClear: true,
            data: this.vcenterVersionList
        });
/*
        $("#qcloud_version .select2_box").select2({
            placeholder: "请选择腾讯版本",
            allowClear: true,
            data: this.qcloudVersionList
        });
*/
        $("#ucloud_region .select2_box").select2({
            placeholder: "请选择区域",
            allowClear: true,
            data: this.ucloudRegionList
        });
        VCenterConfig.init();
    },
    watch: {
        cloudProviderSelected: {
            handler:'watchProviderSelected',
            deep: true
        }
    }
})
// form 输入拦截
$(document).ready(function() {
    $('#vmware_form').validate({
        errorElement: 'div',
        errorClass: 'text-danger',
        rules: {
            vcenter_account_name: {
                required: true,
                minlength: 2
            },
            vcenter_account_password: {
                required: true,
                minlength: 6,
                equalTo: '#vcenter_account_password'
            },
            vcenter_host: {
                required: true,
            },
            vcenter_port: {
                required: true,
                minlength: 2
            }
        },
        messages: {
            vcenter_account_name: "请输入Venter账号名称(至少两位)",
            vcenter_account_password: "请输入VCenter账号密码",
            vcenter_host: "请输入VCenter主机IP",
            vcenter_port: "请输入VCenter主机Port",
        }
    });
    $('#qcloud_form').validate({
        errorElement: 'div',
        errorClass: 'text-danger',
        rules: {
            qcloud_account_name: {
                required: true,
                minlength: 2
            },
            qcloud_secret_id: {
                required: true,
                minlength: 2
            },
            qcloud_secret_key: {
                required: true,
                minlength: 2,
            }
        },
        messages: {
            qcloud_account_name: "请输入腾讯云账号名称(至少两位)",
            qcloud_secret_id: "请输入SecretId",
            qcloud_secret_key: "请输入SecretKey",
        }
    });
    $('#ucloud_form').validate({
        errorElement: 'div',
        errorClass: 'text-danger',
        rules: {
            ucloud_account_name: {
                required: true,
                minlength: 2
            },
            ucloud_public_key: {
                required: true,
                minlength: 2
            },
            ucloud_private_key: {
                required: true,
                minlength: 2
            },
            ucloud_project_id: {
                required: true,
                minlength: 2
            }
        },
        messages: {
            ucloud_account_name: "请输入Ucloud账号名称(至少两位)",
            ucloud_public_key: "请输入PublicKey",
            ucloud_private_key: "请输入PrivateKey",
            ucloud_project_id: "请输入项目ID",
        }
    });
});
