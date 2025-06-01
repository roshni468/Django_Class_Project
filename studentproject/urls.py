"""
URL configuration for studentproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentproject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('addstudent/',addstudent,name="addstudent"),
    path('list/',list,name="list"),
    path('add_tech/',addtecher,name="addtecher"),
    path('tech_list/',techerlist,name="techerlist"),
    path('course/',addcourse,name="addcourse"),
    path('course_list/',course_list,name="course_list"),
    path('deletstudent/<str:myid>',deletstudent,name="deletstudent"),
    path('deletteacher/<str:myid>',deletteacher,name="deletteacher"),
    path('deletcourse/<str:myid>',deletcourse,name="deletcourses"),
    path('editcourse/<str:myid>',editcourse,name="editcourses"),
    path('edit_file/<str:myid>',editcourse,name="editcourses"),
    path('edit_student/<str:myid>',editstudent,name="editstudent"),

    



]
