# -*- coding: utf-8 -*-
"""
用于本地开发环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 本地开发数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': 'oneoaas_cmp',                        # 数据库名 (默认与APP_ID相同)
        'USER': 'root',                         # 你的数据库user
        'PASSWORD': '1qaz@WSX',                  # 你的数据库password
        'HOST': '127.0.0.1',                    # 数据库HOST
        'PORT': '3306',
    },
}
