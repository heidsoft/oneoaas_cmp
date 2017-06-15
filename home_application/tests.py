# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# import from apps here


# import from lib
import django
import os

from django.test import TestCase
from django.test import Client
from blueking.component.shortcuts import get_client_by_user
from blueking.component.client import ComponentClient
from common.mymako import render_json
from settings import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


class SimpleTest(TestCase):

    c = Client()

    # def setUpTestData(cls):
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

    # def setUpClass(cls):
    #     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


    def test_basic_get_host(self):
        user = u'admin'
        client = get_client_by_user(user)
        kwargs = {u'app_id': 7}
        result = client.cc.get_app_host_list(kwargs)
        print result

    def test_get_all_user(self):

        # APP信息
        app_code = 'testframework'
        app_secret = '9bff9124-ad33-4001-a578-02260a3e4ce7'
        # 用户信息
        common_args = {'bk_token': 'XpQC3Jalk_yAxEgl0VhwjZVSRU9DrDwxHdy80RdoPdM'}
        # APP信息app_code, app_secret如未提供，从环境配置获取
        client = ComponentClient(
            app_code=app_code,
            app_secret=app_secret,
            common_args=common_args
        )

        response = client.bk_login.get_all_user()
        print response


