from django.contrib import admin
from .models import PersonalDetails, PersonalStatement, PersonalInterests, Education, WorkExperience

# Register your models here.
admin.site.register(PersonalDetails)
admin.site.register(PersonalStatement)
admin.site.register(PersonalInterests)
admin.site.register(Education)
admin.site.register(WorkExperience)
