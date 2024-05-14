from django.urls import path
from backend import views


urlpatterns=[
    path('base/', views.base, name="base"),
    path('bookdetail/', views.bookdetail, name="bookdetail"),
    path('editbook/<int:bookid>',views.editbook,name="editbook"),

    path('updatebook/<int:bookid>', views.updatebook, name="updatebook"),
    path('deletebook/<int:bookid>', views.deletebook, name="deletebook"),
    path('contactdetails/', views.contactdetails, name="contactdetails"),
    path('deletecont/<int:contid>', views.deletecont, name="deletecont"),

]