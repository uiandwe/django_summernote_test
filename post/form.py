__author__ = 'uiandwe'

from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields
from .models import summer_note_model


class FormFromSomeModel(forms.ModelForm):

     fields = summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
     class Meta:
           model = summer_note_model
           fields = ('fields',)
           widgets= {
                'foo' : SummernoteWidget(),
                'bar' : SummernoteInplaceWidget(),
           }