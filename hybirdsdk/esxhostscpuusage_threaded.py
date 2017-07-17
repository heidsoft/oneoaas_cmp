#!/usr/bin/python
"""
Written by Gaurav Dogra
Github: https://github.com/dograga

Script to extract cpu usage of esxhosts on vcenter for last 1 hour with multithreading
"""
import atexit
from pyVmomi import vim
from pyVim.connect import SmartConnectNoSSL, Disconnect
import time
import datetime
from pyVmomi import vmodl
from threading import Thread

class perfdata():
   def metricvalue(self,item,depth):
      maxdepth=10
      if hasattr(item, 'childEntity'):
         if depth > maxdepth:
             return 0
         else:
             item = item.childEntity
             item=self.metricvalue(item,depth+1)
      return item

   def run(self,content,vihost):
       output=[]
       try:
          perf_dict = {}
          perfManager = content.perfManager
          perfList = content.perfManager.perfCounter
          for counter in perfList: #build the vcenter counters for the objects
              counter_full = "{}.{}.{}".format(counter.groupInfo.key,counter.nameInfo.key,counter.rollupType)
              perf_dict[counter_full] = counter.key
          counter_name = 'cpu.usage.average'
          counterId = perf_dict[counter_name]
          metricId = vim.PerformanceManager.MetricId(counterId=counterId, instance="")
          timenow=datetime.datetime.now()
          startTime = timenow - datetime.timedelta(hours=1)
          endTime = timenow
          search_index = content.searchIndex
          host = search_index.FindByDnsName(dnsName=vihost, vmSearch=False)
          query = vim.PerformanceManager.QuerySpec(entity=host,metricId=[metricId],intervalId=20,startTime=startTime,endTime=endTime)
          stats=perfManager.QueryPerf(querySpec=[query])
          count=0
          for val in stats[0].value[0].value:
              perfinfo={}
              val=float(val/100)
              perfinfo['timestamp']=stats[0].sampleInfo[count].timestamp
              perfinfo['hostname']=vihost
              perfinfo['value']=val
              output.append(perfinfo)
              count+=1
          for out in output:
	      print "Hostname: {}  TimeStame: {} Usage: {}".format (out['hostname'],out['timestamp'],out['value'])
       except vmodl.MethodFault as e:
           print("Caught vmodl fault : " + e.msg)
           return 0
       except Exception as e:
           print("Caught exception : " + str(e))
           return 0

def main():
   user='administrator@oneoaas.com'
   passwd='Oneoaas#123'
   port=443
   vc='10.0.2.8'
   try:
       si = SmartConnectNoSSL(
               host=vc,
               user=user,
               pwd=passwd,
               port=port)
   except:
       print "Failed to connect"
   atexit.register(Disconnect, si)

   content = si.RetrieveContent()
   print content.rootFolder
   print content.rootFolder.childEntity[0]
   print content.rootFolder.childEntity[0].hostFolder
   print content.rootFolder.childEntity[0].hostFolder.childEntity[0]
   print content.rootFolder.childEntity[0].hostFolder.childEntity[0].environmentBrowser
   env = content.rootFolder.childEntity[0].hostFolder.childEntity[0].environmentBrowser
   cfgOption = env.QueryConfigOption()
   print type(cfgOption)
   print type(cfgOption.guestOSDescriptor)
   # print map(lambda x: x.id, cfgOption.guestOSDescriptor)

   #location = "vmware.host." + "10.0.2.10"
   object_view = content.viewManager.CreateContainerView(content.rootFolder,[vim.ClusterComputeResource], True)
   for cluster in object_view.view:
       clusterEnv = cluster.environmentBrowser
       clusterCfgOption = clusterEnv.QueryConfigOption()
       # print clusterCfgOption.guestOSDescriptor
       print map(lambda x: x.id, clusterCfgOption.guestOSDescriptor)
    # services = content.serviceManager.QueryServiceList(location=[location])
    # for service in services:
    #    print service



if __name__ == "__main__":
    main()

