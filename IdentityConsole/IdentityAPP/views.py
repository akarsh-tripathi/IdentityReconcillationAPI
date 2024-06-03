from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from rest_framework import status

from IdentityAPP.models import ContactModel
from IdentityAPP.serializer import ContactSerializer
from IdentityAPP.tasks import updateDBIfIdentityExists

# Create your views here.



@api_view(['POST'])
def IdentityView(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        try:
            emailRecord = ContactModel.objects.filter(email=request.data["email"])
            phoneRecord = ContactModel.objects.filter(phonenumber=request.data["phonenumber"])
            if emailRecord.exists() or phoneRecord.exists():
                ContactModel.objects.create(
                    phonenumber=request.data["phonenumber"],
                    email=request.data["email"],
                    linkedId=emailRecord[0].id if (emailRecord[0].id is not None) else phoneRecord[0].id,
                    linkPrecedence='secondary'
                )
                print("THE FIRST BLOCK")
                return Response([serializer.data,"THE FIRST BLOCK"], status=status.HTTP_201_CREATED)
            if(emailRecord.exists() and phoneRecord.exists()):
                contactsMerged = (emailRecord | phoneRecord).order_by('createdAt')
                if contactsMerged>1:
                    firstContact = contactsMerged[0]
                    for contactIter in contactsMerged[1:]:
                        contactIter.linkedId = firstContact.id
                        contactIter.linkPrecedence = 'secondary'
                        contactIter.save()
                print("THE BOTH BLOCK")
                return Response({serializer.data,"THE BOTH BLOCK"}, status=status.HTTP_201_CREATED)
            else:
                serializer.save()
                print("THE ELSE BLOCK")
                return Response({serializer.data,"THE ELSE BLOCK"}, status=status.HTTP_201_CREATED)
        except: 
            print("THE EXCEPT BLOCK")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        

    else:
        print("The Else Serializer Block")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['GET'])
def Test_getAllData(request):
    data = ContactModel.objects.all()
    serializer = ContactSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def Test_createData(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        print(request.data["phonenumber"],"  ", request.data["email"])
        #Shared Task todo 
        # updateDBIfIdentityExists(request.data)
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