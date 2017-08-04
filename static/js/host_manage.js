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
    var sideContent = $('#vm_side');
    sideContent.removeClass('hidden');
    getComputedStyle(document.querySelector('body')).display;
    sideContent.find('#close').addClass('open');
    sideContent.find('.shield-edit').addClass('open');
    sideContent.find('#shield-detail').removeClass('hidden');

    $('article.shield-content').css('overflow', 'hidden');
}

function close_vm_side(){
    var sideContent = $('#vm_side');
    sideContent.find('.shield-edit').removeClass('open').children('#shield-detail').addClass('hidden');
    sideContent.find('#close').removeClass('open');
    setTimeout(function(){
        sideContent.addClass('hidden');
        $('article.shield-content').css('overflow', 'auto');
    }, 300);

}



$(document).ready(function(){

    VCenterManage.init('#host_manage_record');

    $('#host_manage_record').on( 'click', 'tr', function () {
        var currentHost = VCenterManage.vmTable.row( this ).data();

        //基于vue实例,使用单向数据绑定
        vm_view = new Vue({
            el: '#host_side',
            data: {
                disk_data:[],//磁盘数据
                network_data:[],//网卡数据
                snapshot_data:[], //快照数据,
                vminfo:{}
            },
            created:function () {
                // var _self=this;
                // $.ajax({
                //     url: site_url+'vmware/api/getVMSnapshotList',
                //     type: 'get',
                //     dataType:'json',
                //     data: {
                //         "vmId":currentVm.id,
                //     },
                //     success: function (data) {
                //         console.log(data);
                //         var tmp = [{"id":1,"name":"vm-snaphost01","time":"2017-07-21","description":"调试jvm快照","is_enabled":true},
                //             {"id":2,"name":"vm-snaphost02","time":"2017-07-21","description":"调试jvm快照","is_enabled":true},
                //             {"id":3,"name":"vm-snaphost03","time":"2017-07-21","description":"调试jvm快照","is_enabled":true}]
                //         _self.snapshot_data = tmp;
                //         console.log(_self.snapshot_data);
                //         _self.vminfo = currentVm;
                //     }
                // });
            },
            mounted: function () {

            },
            watch: {

            },
            methods: {

            }
        });

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




