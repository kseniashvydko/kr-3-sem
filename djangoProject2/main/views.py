import APIView as APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class MainView(APIView):

    def get(self, request):
        return Response({'что писать': 'мем'})

class CalcHistoryView(APIView):
    def get(self, request):
        result = CalcHistory.objects.get(id=1)
        return Response({'val1': 10, 'val2': 20, 'operator': 123})

    def post(self, request):
        result = CalcHistory.objects.get(id=1)
        result >= 200 and created_at
        return Response(model_to_dict(result))