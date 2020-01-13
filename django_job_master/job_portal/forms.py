from django import forms

from . import models


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = models.Job
        exclude = ('user', 'created_at',)
        labels = {
            "last_date": "Last Date",
            "company_name": "Company Name",
            "company_description": "Company Description"
        }
