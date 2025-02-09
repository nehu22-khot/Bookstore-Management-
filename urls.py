"""
URL configuration for bookstore_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import include, path

from bookstore_management import settings
from django.conf.urls.static import static
from store import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
    path('order/create/<int:book_id>/', views.create_order, name='create_order'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('book-list/', views.book_list, name='book_list'),
    path('', views.home, name='home'), 
    path('books/', views.book_list, name='books'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_books, name='search_books'),
    path('order/payment/<int:order_id>/', views.order_payment, name='order_payment'),
   
    path('update_order_status/', views.update_order_status, name='update_order_status'),
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    path('payment-details/<int:id>/', views.payment_details, name='payment_details'),
    path('process-payment/<int:order_id>/', views.process_payment, name='process_payment'),
    path('order-confirmation/<int:id>/', views.order_confirmation, name='order_confirmation'),
    path('cash-on-delivery/<int:order_id>/', views.cash_on_delivery, name='cash_on_delivery'),
    path('debit-card-payment/<int:order_id>/', views.debit_card_payment, name='debit_card_payment'),
    path('phonepay-payment/<int:order_id>/', views.phonepay_payment, name='phonepay_payment'),
    
   
     

  
     
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
