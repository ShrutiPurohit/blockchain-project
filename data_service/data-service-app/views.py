from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import ClientListSerializer
from .serializers import BlockListSerializer
from .serializers import ObjectSerializer
from .models import ClientList
from .models import BlockList
from .models import Object
from rest_framework.views import APIView
import json
from django.http import HttpResponse
from rest_framework import generics
from django.core import serializers

class CreateBlock(APIView):

	def get(self,request,format=None):
		user = BlockList.objects.all()
		serializer = BlockListSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format='json'):
		
		datadefault = {'hashofblock': 'default@hashofblock', 'blockid': 30089763, 'nooftxn': 2, 'hashprev': 'default@hashprev', 'txn': ['2018-10-04T09:55:56.437723Z','2018-10-04T09:55:56.574813Z']}

		geodata = dict(request.data)
		bbhashofblock=geodata['hashofblock'][0]
		bbblockid=geodata['blockid'][0]
		bbnooftxn=geodata['nooftxn'][0]
		bbhashprev=geodata['hashprev'][0]
		bbtxn=geodata['txn']

		datadefault['hashofblock'] = bbhashofblock
		datadefault['blockid'] = bbblockid
		datadefault['nooftxn'] = bbnooftxn
		datadefault['hashprev'] = bbhashprev
		datadefault['txn'] = bbtxn


		print(bbtxn)
		print(geodata['txn'])

		serializer = BlockListSerializer(data=datadefault)


		if serializer.is_valid():
			print("valid")
			serializer.save()
			bhashofblock = serializer.data['hashofblock']
			bblockid = serializer.data['blockid']
			txn = serializer.data['txn']
			for t in txn:
				btxnid = t
				ClientList.objects.filter(txnid = btxnid).update(blockid = bblockid, hashofblock=bhashofblock)
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ObjectCreate(APIView):

	def get(self,request,format=None):
		user = Object.objects.all()
		serializer = ObjectSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		print(request.data)
		print(type(request.data))
		#datas = json.dumps(list(request.data),default=str)
		datas = json.dumps(request.data)
		print(datas)
		#ds = dict(datas)
		serializer = ObjectSerializer(data=request.datas)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CreateView(APIView):

	def get(self,request,format=None):
		user = ClientList.objects.all()
		serializer = ClientListSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = ClientListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetailsTxnid(APIView):
	def get_object(self, pk1, pk2):
		try:
			return ClientList.objects.get(txnid=pk2, sender = pk1)
		except ClientList.DoesNotExist:
			raise Http404

	def get(self,request,pk1,pk2,format=None):
		user = self.get_object(pk1,pk2)
		serializer = ClientListSerializer(user)
		return Response(serializer.data)

	def put(self,request,pk1,pk2,format=None):
		user = self.get_object(pk1,pk2)
		serializer = ClientListSerializer(user,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self,request, pk1, pk2, format=None):
		user = self.get_object(pk1, pk2)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class DetailsSender(APIView):
	def get_object(self, pk):
		try:
			return ClientList.objects.filter(sender=pk)
		except ClientList.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		user = self.get_object(pk)
		serializer = user.values('txnid','sender','receiver','message','blockid','date_created')
		json_posts = json.dumps(list(serializer),default=str)
		return HttpResponse(json_posts, content_type='application/json')

class DetailsReceiver(APIView):
	def get_object(self, pk):
		try:
			return ClientList.objects.filter(receiver=pk)
		except ClientList.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		user = self.get_object(pk)
		serializer = user.values('txnid','sender','receiver','message','blockid','date_created')
		json_posts = json.dumps(list(serializer),default=str)
		return HttpResponse(json_posts, content_type='application/json')

class SenderReceiver(APIView):
	def get_object(self, pk1, pk2):
		try:
			return ClientList.objects.filter(sender=pk1, receiver=pk2)
		except ClientList.DoesNotExist:
			raise Http404

	def get(self,request,pk1,pk2,format=None):
		user = self.get_object(pk1,pk2)
		serializer = user.values('txnid','sender','receiver','message','blockid','date_created')
		json_posts = json.dumps(list(serializer),default=str)
		return HttpResponse(json_posts, content_type='application/json')
