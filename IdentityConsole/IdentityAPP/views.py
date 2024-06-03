from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from IdentityAPP.models import ContactModel
from IdentityAPP.serializer import ContactSerializer

# Create your views here.



@api_view(['POST'])
def IdentityView(request):
    serializer = ContactSerializer(data=request.data)



@api_view(['GET'])
def Test_getAllData(request):
    data = ContactModel.objects.all()
    serializer = ContactSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def Test_createData(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# {
# "contact":{
# "primaryContatctId": number,
# "emails": string[], // first element being email of primary contact 
# "phoneNumbers": string[], // first element being phoneNumber of primary conta
# "secondaryContactIds": number[] // Array of all Contact IDs that are "seconda
# }
# }