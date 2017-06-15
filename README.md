# testframework
蓝鲸框架测试
## 配置
```
APP_ID = 'testframework'
APP_TOKEN = '497783ec-e900-4b20-ad51-b7af5ae9d999'
# 蓝鲸智云开发者中心的域名，形如：http://paas.bking.com
BK_PAAS_HOST = 'http://paas.bking.com'
```

## 启动错误
```

(dev-djdemo) ➜  testframework git:(master) ✗ python manage.py runserver
Traceback (most recent call last):
  File "manage.py", line 17, in <module>
    execute_from_command_line(sys.argv)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/management/__init__.py", line 338, in execute_from_command_line
    utility.execute()
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/management/__init__.py", line 312, in execute
    django.setup()
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/__init__.py", line 18, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/apps/registry.py", line 108, in populate
    app_config.import_models(all_models)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/apps/config.py", line 198, in import_models
    self.models_module = import_module(models_module_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/contrib/auth/models.py", line 41, in <module>
    class Permission(models.Model):
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/models/base.py", line 139, in __new__
    new_class.add_to_class('_meta', Options(meta, **kwargs))
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/models/base.py", line 324, in add_to_class
    value.contribute_to_class(cls, name)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/models/options.py", line 250, in contribute_to_class
    self.db_table = truncate_name(self.db_table, connection.ops.max_name_length())
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/__init__.py", line 36, in __getattr__
    return getattr(connections[DEFAULT_DB_ALIAS], item)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/utils.py", line 240, in __getitem__
    backend = load_backend(db['ENGINE'])
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/utils.py", line 111, in load_backend
    return import_module('%s.base' % backend_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/db/backends/mysql/base.py", line 27, in <module>
    raise ImproperlyConfigured("Error loading MySQLdb module: %s" % e)
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: dlopen(/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/_mysql.so, 2): Library not loaded: libmysqlclient.18.dylib
  Referenced from: /Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/_mysql.so
  Reason: image not found
(dev-djdemo) ➜  testframework git:(master) ✗

```

## 没有执行migrate
```
(dev-djdemo) ➜  testframework git:(master) ✗ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 14, 2017 - 11:29:01
Django version 1.8.3, using settings 'settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/contrib/staticfiles/handlers.py", line 63, in __call__
    return self.application(environ, start_response)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/handlers/wsgi.py", line 170, in __call__
    self.load_middleware()
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/handlers/base.py", line 50, in load_middleware
    mw_class = import_string(middleware_path)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/utils/module_loading.py", line 26, in import_string
    module = import_module(module_path)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/middlewares.py", line 7, in <module>
    from account.accounts import Account
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/accounts.py", line 16, in <module>
    from account.http import http_get
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/http.py", line 11, in <module>
    import requests
ImportError: No module named requests
[14/Mar/2017 11:29:19]"GET / HTTP/1.1" 500 59
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/contrib/staticfiles/handlers.py", line 63, in __call__
    return self.application(environ, start_response)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/handlers/wsgi.py", line 170, in __call__
    self.load_middleware()
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/handlers/base.py", line 50, in load_middleware
    mw_class = import_string(middleware_path)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/utils/module_loading.py", line 26, in import_string
    module = import_module(module_path)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/middlewares.py", line 7, in <module>
    from account.accounts import Account
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/accounts.py", line 16, in <module>
    from account.http import http_get
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/http.py", line 11, in <module>
    import requests
ImportError: No module named requests
[14/Mar/2017 11:29:19]"GET /favicon.ico HTTP/1.1" 500 59

```

## 没有安装request对象
```
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/wsgiref/handlers.py", line 85, in run
    self.result = application(self.environ, self.start_response)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/contrib/staticfiles/handlers.py", line 63, in __call__
    return self.application(environ, start_response)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/handlers/wsgi.py", line 170, in __call__
    self.load_middleware()
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/core/handlers/base.py", line 50, in load_middleware
    mw_class = import_string(middleware_path)
  File "/Users/heidsoft/work/dev-djdemo/lib/python2.7/site-packages/Django-1.8.3-py2.7.egg/django/utils/module_loading.py", line 26, in import_string
    module = import_module(module_path)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/middlewares.py", line 7, in <module>
    from account.accounts import Account
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/accounts.py", line 16, in <module>
    from account.http import http_get
  File "/Users/heidsoft/work/dev-djdemo/testframework/account/http.py", line 11, in <module>
    import requests
ImportError: No module named requests

```

## mysql 动态链接库
```
sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib
```

## 周期性任务执行
```
启动celery命令：
python  manage.py  celery  worker  --settings=settings

周期性任务还需要启动celery调度命令：
python  manage.py  celerybeat --settings=settings
```

# 何为任务队列？
```
任务队列是一种在线程或机器间分发任务的机制。

消息队列的输入是工作的一个单元，称为任务，独立的职程（Worker）进程持续监视队列中是否有需要处理的新任务。

Celery 用消息通信，通常使用中间人（Broker）在客户端和职程间斡旋。这个过程从客户端向队列添加消息开始，之后中间人把消息派送给职程。

```

# 数据建模
```
生成模型变更
python manage.py makemigrations

执行模型变更
python manage.py migrate

```

# 测试
```
 python manage.py test home_application.tests.SimpleTest.test_get_all_user
```
