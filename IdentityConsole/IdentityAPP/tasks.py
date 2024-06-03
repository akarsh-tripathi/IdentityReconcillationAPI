from celery import shared_task
from .models import ContactModel

@shared_task(name='UpdateDatabase')
def updateDBIfIdentityExists(data):
    # check if the email exists in the database
    try:
        emailcontact = ContactModel.objects.filter(email=data['email']).order_by("createdAt")
        phonecontact = ContactModel.objects.filter(phonenumber=data['phonenumber']).order_by("createdAt")
        if emailcontact.exists() or phonecontact.exists():
            ContactModel.objects.create(
                phonenumber=data['phonenumber'],
                email=data['email'],
                linkedId=emailcontact[0].id,
                linkPrecedence='secondary'
            )
        # elif (emailcontact.exists() and phonecontact.exists()):
        #     for( i in emailcontact.len()):
                
            
    
    except ContactModel.DoesNotExist:
        pass