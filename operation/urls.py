
from django.contrib import admin
from django.urls import path
from enroll1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add,name="add_and_show"),
path('delete/<int:id>/',views.delete,name="deletedata"),
path('<int:id>',views.updatedata,name="updatedata"),
]