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
                    url: '/vmware/api/getVcenterVirtualMachineList',
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
                // select: {
                //     style:    'os',
                //     selector: 'td:first-child'
                // },
                //多选
                'select': {
                    'style': 'multi'
                },
                columns: [
                    {
                        data: "id",
                    },
                    {
                        title : '名称',
                        data: "name",
                    },
                    {
                        title : '内存',
                        data: "name",
                        render: function ( data, type, row ) {
                            var opHTML='<div>'+data+'<button class="btn btn-xs btn-danger">减小内存</button>';
                            opHTML+='<button class="btn btn-xs btn-danger">增加内存</button></div>';
                            return opHTML;
                        },
                    },
                    {
                        title : 'CPU',
                        data: "name",
                        render: function ( data, type, row ) {
                            var opHTML=data+'<button class="btn btn-xs btn-danger">减小CPU</button>';
                            opHTML+='<button class="btn btn-xs btn-danger">增加CPU</button>';
                            return opHTML;
                        },
                    },
                    {
                        title : '操作系统',
                        data: "guest_fullname",
                    },
                    {
                        title : '运行状态',
                        data: "power_state",
                    },
                    {
                        title : 'IP',
                        data: "ipaddress",
                    },
                    {
                        title : '操作',
                        data: "name",
                        render: function ( data, type, row ) {
                            var opHTML='<button class="btn btn-xs btn-danger">执行快照</button>';
                            return opHTML;
                        },
                    },
                ],
            });

            return this.vmTable = VCenterManageRecord;
        },
        //操作动作前置条件
        beforeAction:function(){
            var rows_selected = this.vmTable.column(0).checkboxes.selected();
            if(typeof rows_selected === 'undefined' || rows_selected.length === 0){
                toastr.warning("请选择虚拟机资源");
                return false
            }
            var rowIds = this.selectedRows =[];
            $.each(rows_selected, function(index, rowId){
                rowIds.push(rowId);
            });
            this.selectedRows = rowIds;
            return true
        },
        //创建虚拟机
        create:function () {
            $.ajax({
                url: '/vmware/api/create',
                type: 'post',
                dataType:'json',
                data: {
                    "vmId":this.selectedRows,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
            $('#createVmWizard').modal('show');
        },
        //克隆虚拟机
        clone:function () {
            if(!this.beforeAction()){
                return
            }
            if(this.selectedRows.length>1){
                toastr.warning("克隆只能选择一台虚拟机");
                return
            }

            $('#cloneVmWizard').modal('show');

        },
        //执行克隆
        executeClone:function () {
            var cloneVmName = $("#cloneVmName").val();
            var select_datacenter = $("#select_datacenter .select2_box").select2("val");
            var select_cluster = $("#select_cluster .select2_box").select2("val");
            var select_datastore = $("#select_datastore .select2_box").select2("val");

            $.ajax({
                url: '/vmware/api/clone',
                type: 'post',
                dataType:'json',
                data: {
                    "vmId":this.selectedRows[0],
                    "vmName":cloneVmName,
                    "vmDatacenter":select_datacenter,
                    "vmCluster":select_cluster,
                    "vmDatastore":select_datastore,
                },
                success: function (data) {
                    toastr.success(data.message);
                }
            });
        },
        //关闭虚拟机
        poweroff: function (data) {
            if(!this.beforeAction()){
                return
            }
            $.ajax({
                url: '/vmware/api/poweroff',
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
        //开启虚拟机
        start: function (data) {
            if(!this.beforeAction()){
                return
            }
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
        //重启虚拟机
        reboot: function (data) {
            if(!this.beforeAction()){
                return
            }
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
        //销毁虚拟机
        destroy: function (data) {
            if(!this.beforeAction()){
                return
            }
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
        //同步虚拟机
        async: function (data) {
            if(!this.beforeAction()){
                return
            }
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
        },
        //webssh控制台
        webssh:function () {
            if(!this.beforeAction()){
                return
            }
        }
    }
})($,window.toastr);

//扩展到jquery
//$.fn.extend(VCenterManage);
//扩展函数


$(document).ready(function(){

    $("#ccAppList .select2_box").select2({
        ajax: {
            url: "/vmware/api/getAppList",
            cache: false,
            //对返回的数据进行处理
            results: function(data){
                console.log(data);
                return data;
            }
        }
    })

    $("#select_datacenter .select2_box").select2({
        ajax: {
            url: "/vmware/api/getAllDatacenter",
            cache: false,
            //对返回的数据进行处理
            results: function(data){
                console.log(data);
                return data;
            }
        }
    })

    $("#select_cluster .select2_box").select2({
        ajax: {
            url: "/vmware/api/getAllCluster",
            cache: false,
            //对返回的数据进行处理
            results: function(data){
                console.log(data);
                return data;
            }
        }
    })

    $("#select_datastore .select2_box").select2({
        ajax: {
            url: "/vmware/api/getAllDatastore",
            cache: false,
            //对返回的数据进行处理
            results: function(data){
                console.log(data);
                return data;
            }
        }
    })


    $('#createVmWizard').bootstrapWizard(
        {
            tabClass: 'nav nav-pills',
            onNext: function(tab, navigation, index) {
                console.log("onNext:"+index);
                console.log(navigation);
                console.log(tab);
                if(index==4){
                    //$('#rootwizard').bootstrapWizard('display', $('#stepid').val());
                }
            },
            onPrevious:function(tab, navigation, index) {
                console.log("onPrevious"+index);
                console.log("onPrevious"+index);
            }
        }
    );

    $('#rootwizard .finish').click(function() {
        alert('Finished!, Starting over!');
        //$('#rootwizard').find("a[href*='tab1']").trigger('click');
    });

    VCenterManage.init('#vcenter_manage_record');

})




