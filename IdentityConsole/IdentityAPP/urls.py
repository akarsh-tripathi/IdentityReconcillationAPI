from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('identity/',views.IdentityView),
    path('test/getAllData/',views.Test_getAllData),
    path('test/createData/',views.Test_createData),
]
