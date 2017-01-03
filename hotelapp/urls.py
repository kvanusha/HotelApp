"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.contrib import admin
#from . import views
from views import index,listfoods,listrooms,liststarters,listorders,login_page,signup,contact,sendSimpleEmail,logout_page,about

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^$',views.index,name='index')
    url(r'^$',index),
    url(r'foods/',listfoods),
    url(r'about/',about),
    url(r'rooms/',listrooms),
    url(r'starters/',liststarters),
    url(r'orders/',listorders),
    url(r'login/', login_page),
    url(r'signup/', signup),
    url(r'contact/', contact),
    #url(r'user/', user),
    url(r'logout/', logout_page),
    url(r'email1/',sendSimpleEmail)
    #url(r'detail/',detail),
    #url(r'sweet/',listsweets),
    #url(r'chat/',listbeverages),
    #url(r'beverage/',listchats),


]
