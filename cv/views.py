from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import PersonalDetails, PersonalStatement, PersonalInterests, Education, WorkExperience
from .forms import PersonalDetailsForm, PersonalStatementForm, PersonalInterestsForm, EducationForm, WorkExperienceForm

# Create your views here.

def cv_list(request):
	personalDetails = PersonalDetails.objects.order_by('email')
	personalStatements = PersonalStatement.objects.order_by('author')
	personalInterests = PersonalInterests.objects.order_by('author')
	educations = Education.objects.order_by('-started_date')
	workExperiences = WorkExperience.objects.order_by('-started_date')
	return render(request, 'cv/cv_list.html', {'personalDetails': personalDetails, 'personalStatements': personalStatements, 'personalInterests': personalInterests, 'educations': educations, 'workExperiences': workExperiences})

@login_required
def personal_detail_new(request):
	if request.method == "POST":
		form = PersonalDetailsForm(request.POST)
		if form.is_valid():
			personalDetail = form.save(commit=False)
			personalDetail.save()
			return redirect('cv_list')
	else:
		form = PersonalDetailsForm()
	return render(request, 'cv/personal_detail_edit.html', {'form': form})
	
@login_required
def personal_detail_edit(request, pk):
    personalDetail = get_object_or_404(PersonalDetails, pk=pk)
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST, instance=personalDetail)
        if form.is_valid():
            personalDetail = form.save(commit=False)
            personalDetail.save()
            return redirect('cv_list')
    else:
        form = PersonalDetailsForm(instance=personalDetail)
    return render(request, 'cv/personal_detail_edit.html', {'form': form})
	
@login_required
def personal_detail_remove(request, pk):
	personalDetail = get_object_or_404(PersonalDetails, pk=pk)
	personalDetail.delete()
	return redirect('cv_list')

@login_required
def personal_statement_new(request):
	if request.method == "POST":
		form = PersonalStatementForm(request.POST)
		if form.is_valid():
			personalStatement = form.save(commit=False)
			personalStatement.save()
			return redirect('cv_list')
	else:
		form = PersonalStatementForm()
	return render(request, 'cv/personal_statement_edit.html', {'form': form})
	
@login_required
def personal_statement_edit(request, pk):
    personalStatement = get_object_or_404(PersonalStatement, pk=pk)
    if request.method == "POST":
        form = PersonalStatementForm(request.POST, instance=personalStatement)
        if form.is_valid():
            personalStatement = form.save(commit=False)
            personalStatement.save()
            return redirect('cv_list')
    else:
        form = PersonalStatementForm(instance=personalStatement)
    return render(request, 'cv/personal_statement_edit.html', {'form': form})
	
@login_required
def personal_statement_remove(request, pk):
	personalStatement = get_object_or_404(PersonalStatement, pk=pk)
	personalStatement.delete()
	return redirect('cv_list')
	
@login_required
def education_new(request):
	if request.method == "POST":
		form = EducationForm(request.POST)
		if form.is_valid():
			education = form.save(commit=False)
			education.save()
			return redirect('cv_list')
	else:
		form = EducationForm()
	return render(request, 'cv/education_edit.html', {'form': form})
	
@login_required
def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('cv_list')
    else:
        form = EducationForm(instance=education)
    return render(request, 'cv/education_edit.html', {'form': form})
	
@login_required
def education_remove(request, pk):
	education = get_object_or_404(Education, pk=pk)
	education.delete()
	return redirect('cv_list')
	
@login_required
def work_experience_new(request):
	if request.method == "POST":
		form = WorkExperienceForm(request.POST)
		if form.is_valid():
			workExperience = form.save(commit=False)
			workExperience.save()
			return redirect('cv_list')
	else:
		form = WorkExperienceForm()
	return render(request, 'cv/work_experience_edit.html', {'form': form})
	
@login_required
def work_experience_edit(request, pk):
    workExperience = get_object_or_404(WorkExperience, pk=pk)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, instance=workExperience)
        if form.is_valid():
            workExperience = form.save(commit=False)
            workExperience.save()
            return redirect('cv_list')
    else:
        form = WorkExperienceForm(instance=workExperience)
    return render(request, 'cv/work_experience_edit.html', {'form': form})
	
@login_required
def work_experience_remove(request, pk):
	workExperience = get_object_or_404(WorkExperience, pk=pk)
	workExperience.delete()
	return redirect('cv_list')
	
@login_required
def personal_interest_new(request):
	if request.method == "POST":
		form = PersonalInterestsForm(request.POST)
		if form.is_valid():
			personalInterest = form.save(commit=False)
			personalInterest.save()
			return redirect('cv_list')
	else:
		form = PersonalInterestsForm()
	return render(request, 'cv/personal_interest_edit.html', {'form': form})
	
@login_required
def personal_interest_edit(request, pk):
    personalInterest = get_object_or_404(PersonalInterests, pk=pk)
    if request.method == "POST":
        form = PersonalInterestsForm(request.POST, instance=personalInterest)
        if form.is_valid():
            personalInterest = form.save(commit=False)
            personalInterest.save()
            return redirect('cv_list')
    else:
        form = PersonalInterestsForm(instance=personalInterest)
    return render(request, 'cv/personal_interest_edit.html', {'form': form})
	
@login_required
def personal_interest_remove(request, pk):
	personalInterest = get_object_or_404(PersonalInterests, pk=pk)
	personalInterest.delete()
	return redirect('cv_list')