from django.urls import path

from . import views

urlpatterns = [
    path('candiinfo/',views.candidateInfo),
    path('signuppage/',views.signuppage),
    path('candidatesignup/',views.CandidateSignupAPI.as_view(),name='CandidateSignupAPI'),
    path('empsignup/',views.EmployeeSignupAPI.as_view(),name='EmployeeSignupAPI'),
    path('companysignup/',views.CompanySignupAPI.as_view(), name='CompanySignupAPI'),
    path('home/',views.home),
    path('about/',views.about),
    path('joblist/', views.joblist),
    path('jobdetail/',views.JobDetails),
    path('signup/',views.signup),
]