"""simpleDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from simpleFirstApp import views
from simpleDjangoProject import settings

urlpatterns = [
    # Single Text
    path('', views.indexPageController, name="index_page"),
    path('firstPage', views.firstPageController, name="first_page"),

    # Loading html first page
    path('htmlPages', views.htmlPageController, name="html_page"),

    # passing data to html page
    path('htmlPagesWithData', views.htmlPageWithDataController, name="html_page_data"),

    # passing data from url to controller
    path('htmlWithDataPass/<str:url_data>', views.htmlWithDataPassController, name="html_with_data_pass"),

    path('addData', views.addData, name="add_data"),

    path('add_student', views.add_student, name="add_student"),
    path('add_teacher', views.add_teacher, name="add_teacher"),
    path('show_all_data', views.show_all_data, name="show_all_data"),

    path('update_student/<str:student_id>', views.update_student, name="update_student"),
    path('delete_student/<str:student_id>', views.delete_student, name="delete_student"),
    path('edit_student', views.edit_student, name="edit_student"),

    path('update_teacher/<str:teacher_id>', views.update_teacher, name="update_teacher"),
    path('delete_teacher/<str:teacher_id>', views.delete_teacher, name="delete_teacher"),
    path('edit_teacher', views.edit_teacher, name="edit_teacher"),

    path('register_user', views.RegisterUser, name="register_user"),
    path('save_user', views.SaveUser, name="save_user"),
    path('login_user', views.LoginUser, name="login_user"),
    path('do_login_user', views.DoLoginUser, name="do_login_user"),
    path('logout', views.Logout, name="logout"),

    path('homePage', views.HomePage, name="home_page"),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
