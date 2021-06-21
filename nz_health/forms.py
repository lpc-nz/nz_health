from django import forms
from django.db import models
from django.db.models.base import Model
from django.forms import fields, widgets
from .models import Person, Referral


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

        widgets = {'date_of_birth': DateInput()}

        labels = {
            'date_of_birth': 'Date Of Birth'
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].empty_label = "Select"


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referrer', 'referral_date', 'note']
        widgets = {'referral_date': DateInput()}
        labels = {
            'referrer': 'Referrer',
            'referral_date': 'Referral Date',
            'note': 'Note'
        }


class AddReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = '__all__'
        widgets = {'referral_date': DateInput()}
        labels = {
            'referrer': 'Referrer',
            'referral_date': 'Referral Date',
            'note': 'Note'
        }
