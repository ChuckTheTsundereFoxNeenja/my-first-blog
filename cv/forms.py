from django import forms

from .models import PersonalDetails, PersonalStatement, PersonalInterests, Education, WorkExperience

class PersonalDetailsForm(forms.ModelForm):

	class Meta:
		model = PersonalDetails
		fields = ('first_name', 'last_name', 'email', 'mobile_number',)

class PersonalStatementForm(forms.ModelForm):

    class Meta:
        model = PersonalStatement
        fields = ('text',)

class PersonalInterestsForm(forms.ModelForm):

	class Meta:
		model = PersonalInterests
		fields = ('text',)

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('establishment_name', 'establishment_address', 'started_date', 'finished_date', 'text',)

class WorkExperienceForm(forms.ModelForm):

	class Meta:
		model = WorkExperience
		fields = ('establishment_name', 'establishment_address', 'establishment_email', 'started_date', 'finished_date', 'text',)

