# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from common.mymako import render_mako_context
from form.form import NameForm
from django.template.context_processors import csrf

from home_application.models import NgUser


def type(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/event_type.html'
    )

def manage(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/event_manage.html'
    )

def workflow(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/event_workflow.html'
    )

def eventTypeAdd(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/event_type_add.html'
    )

def eventConfig(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。

    # for num in  range(1,51,1):
    #     demo = NgUser(name="jake",age=num,password='123456')
    #     demo.save()

    user_list = NgUser.objects.all()

    paginator = Paginator(user_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    print  page
    print "page is %s" % page

    if page is None:
        page = 1

    try:
        intPage = int(page)+1
        users = paginator.page(intPage)
        #print contacts.count(2)
        print users.previous_page_number()
        print users.next_page_number()
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)



    return render_mako_context(
        request, '/home_application/event/event_config.html',{'users': users}
    )

def eventUserManage(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/event_user_manage.html'
    )

def alarmCompression(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/alarm_compression_configuration.html'
    )

def alarmMerge(request):
    # 这里开始触发缓存数据，确保后续页面访问流畅。
    return render_mako_context(
        request, '/home_application/event/alarm_merge_configuration.html'
    )

def addEventSource(request):
    c = {}
    c.update(csrf(request))
    print 'is_valid .................1111'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        print form.is_valid()

        """
        不管表单提交的是什么数据，一旦通过调用is_valid() 成功验证（is_valid() 返回True），
        验证后的表单数据将位于form.cleaned_data 字典中。
        这些数据已经为你转换好为Python 的类型。
        """
        if form.is_valid():
            print 'is_valid .................2222'
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #user_password = form.cleaned_data['user_password']
            # user_account = form.cleaned_data['user_account']
            # event_role = form.cleaned_data['event_role']
            # optionsRadios = form.cleaned_data['optionsRadios']
            # user_email = form.cleaned_data['user_email']
            # print user_account
            # #print user_password
            # print event_role
            # print optionsRadios
            # print user_email
            print form.cleaned_data



            return HttpResponseRedirect('/overview/')

    # if a GET (or any other method) we'll create a blank form
    else:
        print 'is_valid .................3333'
        form = NameForm()


    return render_mako_context(
        request, '/home_application/event/alarm_merge_configuration.html',{'form': form}
    )





