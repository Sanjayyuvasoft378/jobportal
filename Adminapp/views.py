from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from Adminapp.serializers import AboutUsSerializer, CandidateInfoSerializer, CompanyInfoSerializer
from .models import AboutUs, CandidateInfo
from rest_framework.views import APIView

# Create your views here.
def candidateInfo(request):
    return render(request, 'index.html')
    # return HttpResponse("this is a home page for the testing")

def signuppage(request):
    return render(request, 'signup.html')


class CandidateSignupAPI(APIView):
    def post(self,request,*args, **kwargs):
        try:
            Data = request.data
            print(Data)
            userserializer = CandidateInfoSerializer(data=Data)
            if userserializer.is_valid():
                userserializer.save()
            return JsonResponse({"message":"User Registration successfully"}, safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)


class CompanySignupAPI(APIView):
    def post(self,request,*args, **kwargs):
        try:
            Data = request.data
            companySerializer = CompanyInfoSerializer(data = Data)
            if companySerializer.is_valid():
                companySerializer.save()
            return JsonResponse({"message":"company registered successfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)


    
class AboutUsAPI(APIView):
    def post(self,request, *args, **kwargs):
        try:
            Data = request.data
            serializers = AboutUsSerializer(data=Data)
            if serializers.is_valid():
                serializers.save()
            return JsonResponse({"message":"Data added successfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

    def get(self, request, *args , **kwargs):
        try:
            data = AboutUs.objects.all()
            return JsonResponse({"result":data},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":" Internal server error {}".format(e)},safe=False, status=500)

            