from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []