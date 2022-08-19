from django.urls import path

from . import views

urlpatterns = [
    path('candiinfo/',views.candidateInfo),
    path('signuppage/',views.signuppage),
    path('candidatesignup/',views.CandidateSignupAPI.as_view(),name='CandidateSignupAPI'),
    path('companysignup/',views.CompanySignupAPI.as_view(), name='CompanySignupAPI'),
]