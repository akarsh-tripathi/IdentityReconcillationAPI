from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from rest_framework import status

from IdentityAPP.models import ContactModel
from IdentityAPP.serializer import ContactSerializer


@api_view(['POST'])   
def IdentityView(request):

      
    #Checking For Duplicates as we have to Insert New Contacts if not present
    duplicateEntry = ContactModel.objects.filter(email=request.data['email'], phonenumber = request.data['phonenumber'])

    if(duplicateEntry.count()==0):
        #Mapping the contacts based on requiremnets
        mapNewContacts({'email':request.data["email"],'phonenumber':request.data["phonenumber"]})
    
    FindRecord = ContactModel.objects.filter(Q(email=request.data["email"])| Q(phonenumber=request.data["phonenumber"])).order_by('createdAt')
    return Response({"Contact":
                    {
                        "primaryContatctId":FindRecord[0].id if(FindRecord.count()>0) else None,
                        "emails": FindRecord.values_list('email', flat=True).distinct(),
                        "phoneNumbers": FindRecord.values_list('phonenumber', flat=True).distinct(),
                        "secondaryContactIds":[contact.id for contact in FindRecord[1:]] if FindRecord.count() > 1 else []
                    }}, status=status.HTTP_200_OK)
    


@api_view(['GET'])
def Test_getAllData(request):
    data = ContactModel.objects.all()
    serializer = ContactSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def Test_createData(request):
    serializer = ContactSerializer(data=request.data)
    print("LOG-D ", request.data)
    if serializer.is_valid():
       
        #If Duplicate Entry Exists
        duplicateEntry = ContactModel.objects.filter(email=request.data['email'], phonenumber = request.data['phonenumber'])
        print("LOG-D ",not duplicateEntry.exists())
        if(duplicateEntry.exists()):
            return Response({"message":"Duplicate Entry"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
                response = mapNewContacts({'email':request.data["email"],'phonenumber':request.data["phonenumber"]})
                if response == "Error Occured":
                    return Response({"message":"Error Occured"}, status=status.HTTP_400_BAD_REQUEST)
                return Response({"data":"Done","message":"Contact Created"}, status=status.HTTP_201_CREATED)
        except: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def mapNewContacts(data):
    print(data["email"],data["phonenumber"])
    try:
        # Filtering records bsased on Email & Phonenumbers 
        emailRecord = ContactModel.objects.filter(email=data["email"])
        phoneRecord = ContactModel.objects.filter(phonenumber=data["phonenumber"])
        
        # Case1: If Email or Phone Exists
        if emailRecord.exists() or phoneRecord.exists():
            print(emailRecord.values_list('phonenumber'))
            print(phoneRecord.values_list('phonenumber'))

            ContactModel.objects.create(
                phonenumber=data["phonenumber"],
                email=data["email"],
                linkedId=emailRecord[0].id if (emailRecord.count()!=0) else phoneRecord[0].id,
                linkPrecedence="secondary"
            )
        # Case2 : If Both Email & Phone Exists
        if(emailRecord.exists() and phoneRecord.exists()):
            contactsMerged = (emailRecord | phoneRecord).order_by('createdAt')
            print("Here -2")
            if contactsMerged.count()>1:
                firstContact = contactsMerged[0]
                for contactIter in contactsMerged[1:]:
                    contactIter.linkedId = firstContact.id
                    contactIter.linkPrecedence = "secondary"
                    contactIter.save()
        else:
            # Case 3: It none exists we need new methods
            ContactModel.objects.create(
                phonenumber=data["phonenumber"],
                email=data["email"]
            )
    except: 
        # Exception Block
        return "Error Occured"