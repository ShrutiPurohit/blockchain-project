from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializer import ClientRequestSerializer
from .models import ClientRequest
from .models import TxnList
from rest_framework.views import APIView
import json
from django.http import HttpResponse
from rest_framework import generics
from django.core import serializers
from .serializer import TxnListSerializer
import ast
import requests

class CreateView(APIView):

	def get(self,request,format=None):
		user = ClientRequest.objects.all()
		serializer = ClientRequestSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		url = "http://localhost:8001/storelist/show/"
		serializer = ClientRequestSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			print(serializer.data)
			geodata = serializer.data
			ds = geodata
			r = requests.post(url = url, data = ds)
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RequestedTxn(APIView):

	def get(self,request,format=None):
		user = TxnList.objects.all()
		serializer = TxnListSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		#url = "http://localhost:8001/storelist/show/"
		serializer = TxnListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GetTxns(APIView):

	def get(self,request,pk1,pk2,format=None):
		#user = self.get_object(pk1,pk2)
		print("in get")
		response = requests.get('http://localhost:8002/clientlist/sender/'+pk1+'/txnid/'+pk2+'/')
		geodata = response.json()
		#serializer = TxnListSerializer(user)
		return Response(geodata)

class GetSenderTxn(APIView):

	def get(self,request,pk1,format=None):
		response = requests.get('http://localhost:8002/clientlist/sender/'+pk1+'/')
		geodata = response.json()
		return Response(geodata)

class GetReceiverTxn(APIView):

	def get(self,request,pk1,format=None):
		response = requests.get('http://localhost:8002/clientlist/receiver/'+pk1+'/')
		geodata = response.json()
		return Response(geodata)





