# -*- coding: utf-8 -*-
import json

from django.db import models
from django.utils import timezone
from django.db import connection, transaction

"""
vcenter账号信息对象
"""
class VcenterAccount(models.Model):
    account_name = models.CharField(max_length=60)
    account_password = models.CharField(max_length=20)
    vcenter_host = models.CharField(max_length=30)
    vcenter_port = models.IntegerField(default=443)
    vcenter_version = models.CharField(max_length=10)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_account'

        """
数据中心,与虚拟机是一对多的关系
        与集群是一对多的关系
"""
class VcenterDatacenter(models.Model):
    #数据中心名称
    name = models.CharField(max_length=60)

    #存储节点总量
    datastoreTotal = models.IntegerField(default=0)

    #存储节点个数
    datastoreNum = models.IntegerField(default=0)

    #主机个数
    hostNum = models.IntegerField(default=0)

    #网络个数
    networkNum = models.IntegerField(default=0)

    #虚拟机个数
    vmNum = models.IntegerField(default=0)

    #集群个数
    clusterNum = models.IntegerField(default=0)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_datacenter'

"""
集群，与数据中心是一对多关系
"""
class VcenterCluster(models.Model):
    #集群所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_cluster_ref_datacenter')

    #集群名称
    name = models.CharField(max_length=60)

    #集群操作历史次数
    actionHistoryNum = models.IntegerField(default=0)

    #集群迁移历史次数
    migrationHistoryNum = models.IntegerField(default=0)

    #drs推荐次数
    drsRecommendationNum = models.IntegerField(default=0)

    #集群是否开启HA
    enabledClusterHa  = models.BooleanField(default=False)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_cluster'

"""
存储节点，与数据中心是一对多关系
"""
class VcenterDatastore(models.Model):
    #存储所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_datastore_ref_datacenter')
    #存储节点名称
    name = models.CharField(max_length=60)

    #存储挂载主机数
    mountHostNum = models.IntegerField(default=0)

    #存储节点容器id
    datastoreContainerId = models.CharField(default="",max_length=60,null=True)

    #是否可访问
    accessible = models.BooleanField(default=True)

    #容量大小
    capacity = models.IntegerField(default=0)

    #剩余空间
    freeSpace = models.IntegerField(default=0)

    #维护模式
    maintenanceMode = models.CharField(default="",max_length=20)

    #多主机访问是否开启
    multipleHostAccess = models.BooleanField(default=True,max_length=20)

    #文件系统类型
    filesystemType = models.CharField(default="",max_length=20)

    #存储节点路径
    url = models.CharField(default="",max_length=120)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_datastore'

"""
存储节点，与数据中心是一对多关系
"""
class VcenterNetwork(models.Model):
    #网络所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_network_ref_datacenter')
    #数据中心名称
    name = models.CharField(max_length=60)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_network'

"""
定义vm管理器
"""
class VmManager(models.Manager):
    pass


"""
vcenter虚拟机对象
"""
class VcenterVirtualMachine(models.Model):
    #属于哪一个vcenter 账号
    account = models.ForeignKey(VcenterAccount, related_name='vcenter_virtualmachine_ref_account')

    #虚拟机所在的数据中心
    datacenter = models.ForeignKey(VcenterDatacenter, related_name='vcenter_virtualmachine_ref_datacenter',null=True)

    #虚拟机所在集群
    cluster = models.ForeignKey(VcenterCluster, related_name='vcenter_virtualmachine_ref_cluster',null=True)

    #虚拟机名称
    name = models.CharField(max_length=60)
    #虚拟机路径名称
    vm_pathname = models.CharField(max_length=120)
    #虚拟机操作系统名称
    guest_fullname = models.CharField(max_length=60)
    #虚拟机运行状态
    power_state = models.CharField(max_length=50)
    #虚拟机IP
    ipaddress = models.CharField(max_length=30)
    #实例uuid
    instance_uuid = models.CharField(max_length=40)
    #最后启动时间
    boot_time = models.TimeField(null=True)

    #是否为模版
    template = models.BooleanField(max_length=1)

    #最大cpu使用
    maxCpuUsage = models.IntegerField(default=0)
    #最大内存使用
    maxMemoryUsage = models.IntegerField(default=0)
    #内存大小
    memorySizeMB = models.IntegerField(default=0)
    #cpu个数
    numCpu = models.IntegerField(default=0)

    numEthernetCards = models.IntegerField(default=0)

    numVirtualDisks = models.IntegerField(default=0)

    instanceUuid = models.CharField(max_length=60)

    #操作系统Id
    guestId = models.CharField(max_length=60)

    #存储信息
    storage_committed = models.IntegerField(default=0,null=True),
    storage_uncommitted = models.IntegerField(default=0,null=True),
    storage_unshared = models.IntegerField(default=0,null=True),

    overallStatus = models.CharField(max_length=10)

    #自定义表名称
    class Meta:
        db_table = 'vcenter_virtualmachine'


'''
快照数据表管理方法
'''
class VcenterVirtualMachineSnapshot_Manager(models.Manager):
    '''
    根据虚拟机id获取快照信息
    '''
    def getListByVmId(self, vmId):
        queryStr = 'SELECT vvs.id,vvs.`name`,vvs.description,date_format(vvs.create_time,"%%Y-%%m-%%d %%H:%%i:%%s") as create_time,vvs.account_id,vvs.virtualmachine_id,vvs.result FROM vcenter_virtualMachine_snapshot AS vvs WHERE vvs.virtualmachine_id = %s' % vmId
        print queryStr
        cursor = connection.cursor()
        cursor.execute(queryStr)
        column_names = [d[0] for d in cursor.description]
        return [Row(zip(column_names, row)) for row in cursor]


"""
虚拟机快照，与虚拟机是多对一的关系
"""
class VcenterVirtualMachineSnapshot(models.Model):
    #快照属于哪一个虚拟机
    virtualmachine = models.ForeignKey(VcenterVirtualMachine, related_name='vcenter_virtualMachine_napshot_ref_virtualmachine')
    # 属于哪一个vcenter 账号
    account = models.ForeignKey(VcenterAccount, related_name='vcenter_virtualMachine_napshot_ref_account')
    #快照名称
    name = models.CharField(u"快照名称", max_length=120)
    description = models.CharField(u"快照描述", max_length=500)
    create_time = models.DateTimeField(u"创建时间", default=timezone.now)
    result = models.CharField(u"创建快照结果:running表示正在创建中，success表示创建快照成功，failed表示创建失败", max_length=20, default='running')
    #自定义表名称
    class Meta:
        db_table = 'vcenter_virtualMachine_snapshot'

    objects = VcenterVirtualMachineSnapshot_Manager()


class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)