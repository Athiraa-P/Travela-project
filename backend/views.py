from django.shortcuts import render,redirect
from frontapp.models import BookingDB,ContactDB

# Create your views here.
def base(request):
    return render(request,"Base.html")


def bookdetail(request):
    data = BookingDB.objects.all()
    return render(request,"book_details.html",{'data':data})


def editbook(request,bookid):
    data=BookingDB.objects.get(id=bookid)
    return render(request,"edit_booking.html",{'data':data})

def deletebook(request,bookid):
    x=BookingDB.objects.filter(id=bookid)
    x.delete()
    return redirect(bookdetail)

def updatebook(request,bookid):
    if request.method=="POST":
        p=request.POST.get('name')
        q=request.POST.get('email')
        r=request.POST.get('date')
        s=request.POST.get('des')
        t=request.POST.get('per')
        u=request.POST.get('kids')
        BookingDB.objects.filter(id=bookid).update(Name=p,Email=q,Date=r,Destination=s,Person=t,Kids=u)
        return redirect(bookdetail)


def contactdetails(request):
    data = ContactDB.objects.all()
    return render(request,"contact_details.html",{'data':data})

def deletecont(request,contid):
    x=ContactDB.objects.filter(id=contid)
    x.delete()
    return redirect(contactdetails)

