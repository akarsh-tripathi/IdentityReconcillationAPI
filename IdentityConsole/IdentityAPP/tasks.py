# from celery import shared_task

# from IdentityConsole.IdentityAPP.serializer import ContactSerializer
# from .models import ContactModel

# @shared_task(name='UpdateDatabase')
# def updateDBIfIdentityExists(data):
    # check if the email exists in the database
    # serializer = ContactSerializer(data)
   
    # if serializer.is_valid():
    #     try:
    #         emailRecord = ContactModel.objects.filter(email=data["email"])
    #         phoneRecord = ContactModel.objects.filter(phonenumber=data["phonenumber"])
    #         print("Here -0")
    #         #CornerCase Check 
    #         duplicateEntry = ContactModel.objects.filter(email=data['email'], phonenumber = request.data['phonenumber'])
    #         print("LOG-D ",duplicateEntry.exists())

    #         if not duplicateEntry.exists():
    #             if emailRecord.exists() or phoneRecord.exists():
    #                 print(emailRecord.first().values('phonenumber'))
    #                 #CornerCase Check 
    #                 print("Here -1")
    #                 ContactModel.objects.create(
    #                     phonenumber=request.data["phonenumber"],
    #                     email=request.data["email"],
    #                     linkedId=emailRecord[0].id if (emailRecord[0].id is not None) else phoneRecord[0].id,
    #                     linkPrecedence='secondary'
    #                 )
                    
    #                 print("THE FIRST BLOCK")
    #                 return Response([serializer.data,"THE FIRST BLOCK"], status=status.HTTP_201_CREATED)
    #             if(emailRecord.exists() and phoneRecord.exists()):
    #                 contactsMerged = (emailRecord | phoneRecord).order_by('createdAt')
    #                 print("Here -2")
    #                 if contactsMerged>1:
    #                     firstContact = contactsMerged[0]
    #                     for contactIter in contactsMerged[1:]:
    #                         contactIter.linkedId = firstContact.id
    #                         contactIter.linkPrecedence = 'secondary'
    #                         contactIter.save()
    #                 print("THE BOTH BLOCK")
    #                 return Response({serializer.data,"THE BOTH BLOCK"}, status=status.HTTP_201_CREATED)
    #             else:
    #                 print("Here -3")
    #                 serializer.save()
    #                 print("THE ELSE BLOCK")
    #                 return Response({serializer.data,"THE ELSE BLOCK"}, status=status.HTTP_201_CREATED)
    #     except: 
    #         print("Here -4")
    #         print("THE EXCEPT BLOCK")
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            
    
    # except ContactModel.DoesNotExist: