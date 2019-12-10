"""myrestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from website.views import changeQuantity,register,user_login,user_logout,productlist_view,index,about,navbar,removefromcart,menu,blog,contact,checkout,payment_process,cartpage, mycart

from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',register),
    path('user_login/',user_login),
    path('user_logout/',user_logout),
    path('product_list/',productlist_view),
    path('',index),
    path('about/', about),
    path('navbar/', navbar),
    path('removefromcart/',removefromcart),
    path('menu/', menu),
    path('blog/', blog),
    path('contact/', contact),
    path('checkout/', payment_process),path('cartpage/', cartpage),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^payment_process/$', payment_process, name='payment_process'),
    url('changeQuantity/',changeQuantity),
    path('mycart/', mycart)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
