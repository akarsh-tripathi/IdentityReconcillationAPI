from django.db import models
from django.utils import timezone

# Create your models here.

class ContactModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    phonenumber = models.CharField(null=True, max_length=10)
    email = models.EmailField()
    linkedId = models.IntegerField(null=True)
    linkPrecedence = models.CharField(max_length=10, default="primary")
    createdAt = models.DateTimeField(default=timezone.now())
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    


# {
# id Int 
#  phoneNumber String?
#  email String?
#  linkedId Int? // the ID of another Contact linked to this one
#  linkPrecedence "secondary"|"primary" // "primary" if it's the first Contact in th
#  createdAt DateTime 
# Bitespeed Backend Task: Identity Reconciliation 2
#  updatedAt DateTime 
#  deletedAt DateTime?
# }