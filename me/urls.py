from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns =[
	path("", views.index,name="index"),
	path('login/', LoginView.as_view(template_name='me/login.html'),name='logiin'),
	path('afterlogin/', views.afterlogin_view,name='afterlogin'),
	path('customersignup/', views.customer_signup_view, name='customersignup'),
	path('view-customer/', views.view_customer_view,name='view-customer'),
	path('download-invoice/<int:id>', views.download_invoice_view,name='download-invoice'),
	path('rd',views.reportt,name='rdd'),
	path("deleingg/<id>", views.deletedata,name="deleingg"),
	path("bill/", views.addbl,name="bill"),
	path("bill2/", views.addview,name="bill2"),
	path('edit-profile/<id>', views.edit_profile_view,name='edit-profile'),
]