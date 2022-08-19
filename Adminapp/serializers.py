from dataclasses import field, fields
from rest_framework import serializers
from .models import *

class CandidateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateInfo
        fields = '__all__'

class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

        