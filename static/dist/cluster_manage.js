var VCenterManage=function(e,t){return{vmTable:null,selectedRows:[],init:function(t){var n={search:"搜索：",lengthMenu:"每页显示 _MENU_ 记录",zeroRecords:"没找到相应的数据！",info:"分页 _PAGE_ / _PAGES_",infoEmpty:"暂无数据！",infoFiltered:"(从 _MAX_ 条数据中搜索)",paginate:{first:"<<",last:">>",previous:"上一页",next:"下一页"}},a=e(t).DataTable({paging:!0,ordering:!1,info:!1,searching:!1,pageLength:5,lengthChange:!1,language:n,ajax:{url:site_url+"vmware/api/getVcenterClusterList"},columns:[{data:"name"},{data:"actionHistoryNum"},{data:"migrationHistoryNum"},{data:"drsRecommendationNum"},{data:"enabledClusterHa"}]});return this.vmTable=a,new e.fn.dataTable.Buttons(a,{buttons:[{extend:"copyHtml5",text:"拷贝表格"},{extend:"excelHtml5",text:"导出Excel"},{extend:"pdfHtml5",text:"导出PDF"},{extend:"csvHtml5",bom:"utf-8",text:"导出CVS"}]}),a.buttons().container().appendTo(a.table().container()),a}}}($,window.toastr);$(document).ready(function(){VCenterManage.init("#cluster_manage_record")});