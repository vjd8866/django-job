from django.contrib import admin

from . import models
myModels = [models.Job, models.Applicant]
admin.site.register(myModels)
