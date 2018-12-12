from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .serializers import StorelistSerializer
from .serializers import BlockListSerializer
from .models import Txn
from .models import BlockList
import ast
import requests


class Show(APIView):

	def get(self,request):
		user = Txn.objects.all()
		serializer = StorelistSerializer(user,many=True)
		return Response(serializer.data)


	def post(self,request,format=None):
		url="http://localhost:8002/clientlist/"
		url1 = "http://localhost:8000/txndetails/"

		serializer = StorelistSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			last_ten = Txn.objects.all().order_by('-txnid')[:2]
			print(last_ten)
			llten = list(last_ten)
			print(llten[0])
			print(len(llten))
			#Block(list(last_ten)) # call createBlock Fucntion with 10 records
			geodata = serializer.data
			ds = geodata
			r = requests.post(url = url, data = ds)
			r1 = requests.post(url = url1, data = ds)
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CreateBlock(APIView):

	def get(self,request,format=None):
		user = BlockList.objects.all()
		serializer = BlockListSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		url = "http://localhost:8002/blocklist/"
		serializer = BlockListSerializer(data=request.data)
		#r = requests.post(url = url, data = request.data)
		if serializer.is_valid():
			serializer.save() # creaation of block in CS
			geodata = serializer.data
			print(type(serializer.data))
			ds = geodata
			print("type")
			print(type(ds))
			r = requests.post(url = url, data = ds)
			print("block")
			print(r)
			bhashofblock = serializer.data['hashofblock']
			bblockid = serializer.data['blockid']
			txn = serializer.data['txn']
			for t in txn:
				btxnid = t
				Txn.objects.filter(txnid = btxnid).update(blockid = bblockid, hashofblock=bhashofblock)
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
