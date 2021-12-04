from django import forms
from django.db.models import fields
from .models import comments

class Comments_Form(forms.ModelForm):
    class Meta:
        model = comments
        fields = '__all__'