from django.urls import path
from frontapp import views

urlpatterns=[
    path('index/',views.index,name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('saveregister/', views.saveregister, name="saveregister"),
    path('Loginuser/', views.Loginuser, name="Loginuser"),
    path('booking/', views.booking, name="booking"),
    path('savebook/', views.savebook, name="savebook"),
    path('contact/', views.contact, name="contact"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('servicepage/', views.servicepage, name="servicepage"),
    path('packagepage/', views.packagepage, name="packagepage"),
    path('blogpage/', views.blogpage, name="blogpage"),
    path('singpage/', views.singpage, name="singpage"),
    path('gallerypage/', views.gallerypage, name="gallerypage"),
    path('searchpage/', views.searchpage, name="searchpage"),
    path('cali/', views.cali, name="cali"),
    path('veni/', views.veni, name="veni"),
    path('thai/', views.thai, name="thai"),
    path('guidepage/', views.guidepage, name="guidepage"),
    path('destinationpage/', views.destinationpage, name="destinationpage"),
    path('testpage/', views.testpage, name="testpage"),
    path('tourpage/', views.tourpage, name="tourpage"),
    path('UserLogout/', views.UserLogout, name="UserLogout"),
    path('payment/', views.payment, name="payment"),
    path('success/', views.success, name="success"),
    path('profile/', views.profile, name="profile"),

]