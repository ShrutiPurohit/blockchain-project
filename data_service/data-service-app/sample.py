from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import ClientListSerializer
from .serializers import BlockListSerializer
from .models import ClientList
from Crypto.PublicKey import RSA

# Create your views here.


class Registration(APIView):

	def get(self,request,format=None):
		user = ClientList.objects.all()
		serializer = ClientListSerializer(user,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = ClientListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			bclientid = serializer.data['clientid']
			bclientname = serializer.data['clientname']
			bemailid = serializer.data['emailid']
			key_pair = RSA.generate(1024)
			private_key = open("privatekey.pem", "w")
			private_key.write(key_pair.exportKey())
			private_key.close()
			public_key = open("public_key.pem", "w")
			public_key.write(key_pair.publickey().exportKey())
			public_key.close()
			ClientList.object.post(clientid=bclientid, clientname=bclientname, emailid=bemailid, publickey=public_key, privatekey=private_key)
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)









		
		"""
		for i in range(len(da)):
			#print(da[0])
			ds = ast.literal_eval(da[i])
			print("list")
			#print(ds)
			r = requests.post(url = url, data = ds)
		"""