from django.urls import path
from . import views

urlpatterns = [
	path('cv/', views.cv_list, name='cv_list'),
	path('cv/personal_detail/new', views.personal_detail_new, name='personal_detail_new'),
	path('cv/personal_detail/<int:pk>/edit/', views.personal_detail_edit, name='personal_detail_edit'),
	path('cv/personal_detail/<int:pk>/remove/', views.personal_detail_remove, name='personal_detail_remove'),
	path('cv/personal_statement/new', views.personal_statement_new, name='personal_statement_new'),
	path('cv/personal_statement/<int:pk>/edit/', views.personal_statement_edit, name='personal_statement_edit'),
	path('cv/personal_statement/<int:pk>/remove/', views.personal_statement_remove, name='personal_statement_remove'),
	path('cv/education/new', views.education_new, name='education_new'),
	path('cv/education/<int:pk>/edit/', views.education_edit, name='education_edit'),
	path('cv/education/<int:pk>/remove/', views.education_remove, name='education_remove'),
	path('cv/work_experience/new', views.work_experience_new, name='work_experience_new'),
	path('cv/work_experience/<int:pk>/edit/', views.work_experience_edit, name='work_experience_edit'),
	path('cv/work_experience/<int:pk>/remove/', views.work_experience_remove, name='work_experience_remove'),
	path('cv/personal_interest/new', views.personal_interest_new, name='personal_interest_new'),
	path('cv/personal_interest/<int:pk>/edit/', views.personal_interest_edit, name='personal_interest_edit'),
	path('cv/personal_interest/<int:pk>/remove/', views.personal_interest_remove, name='personal_interest_remove'),
]

