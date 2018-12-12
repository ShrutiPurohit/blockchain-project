"""
    	stxnid= geodata['txnid']
    	ssender=geodata['sender']
    	sreceiver=geodata['receiver']
    	smessage=geodata['message']
    	Txn.objects.post(txnid=stxnid, sender = ssender, receiver= sreceiver, message= smessage)
    	#return render(request,{'txnid':geodata['txnid'],'sender':geodata['sender'],'receiver':geodata['receiver'],'message':geodata['message']})
		"""



"""
class Signup(APIView):

	def post(self,request,format= None):
		serializer = ClientListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			susername=serializer.data['username']

			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		"""

"""
class Login(APIView):

	def post(self,request,format=None):
		serializer = SignupListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			spassword=serializer.data['password']
			susername=serializer.data['username']
			ClientList.objects.filter(username=susername , password=spassword)

"""

