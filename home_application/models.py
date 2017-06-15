# -*- coding: utf-8 -*-
import json
from django.db import models

"""
用户表
"""
class NgUser(models.Model):
    name = models.CharField(max_length=127)
    age =  models.IntegerField(null=True)
    password = models.CharField(max_length=32)

    #对象序列化
    def __unicode__(self):
        #字典转为json字符串
        return json.dumps({"name":self.name,"age":self.age})

    #自定义表名称
    class Meta:
        db_table = 'ng_user'

"""
任务表
"""
class NgTask(models.Model):
    taskName = models.CharField(max_length=127)
    taskResult =  models.CharField(max_length=127)
    taskFinishTime = models.DateField()

    #对象序列化
    def __unicode__(self):
        #字典转为json字符串
        return json.dumps({"name":self.taskName,"result":self.taskResult,"time":self.taskFinishTime})

    #自定义表名称
    class Meta:
        db_table = 'ng_task'

"""
一辆汽车（Car）有一个制造商（Manufacturer） 
但是一个制造商（Manufacturer） 生产很多汽车（Car），
每一辆汽车（Car） 只能有一个制造商（Manufacturer）
"""
class Manufacturer(models.Model):
    # ...
    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    # ...
    pass
    def __str__(self):              # __unicode__ on Python 2
        return self.title

"""
一个学生有多个老师，一个老师也可以有多个学生
"""
class Student(models.Model):
    #学生类
    pass

class Teacher(models.Model):
    #老师
    students = models.ManyToManyField(Student)

"""
自关联样例子
"""
class Person(models.Model):
    friends = models.ManyToManyField("self")


"""
下面三个类用于一类场景，首先由地址数据库，后来想扩展地址数据库，想在地址上建立一个餐厅
餐厅建好后，需要有多个服务员，因而服务员与餐厅是多对一。
餐厅与地址是一对一
"""
"""
地址
"""
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the place" % self.name

"""
餐厅
"""
class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the restaurant" % self.place.name

"""
服务员
"""
class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)

    def __str__(self):              # __unicode__ on Python 2
        return "%s the waiter at %s" % (self.name, self.restaurant)