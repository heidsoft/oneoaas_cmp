# -*- coding: utf-8 -*-
from django import forms

class NameForm(forms.Form):
    event_role = forms.CharField(label=u'事件源A', max_length=100)
    user_account = forms.CharField(label=u'事件源账号A', max_length=100)
    user_password = forms.CharField()
    optionsRadios = forms.IntegerField()
    user_email = forms.EmailField()

