from django.shortcuts import render,redirect
from django.http import HttpResponse
from frontapp.models import RegisterDb,BookingDB,ContactDB,SearchDB
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"Register.html")

def login(request):
    return render(request,"Login.html")

def saveregister(request):
    if request.method=="POST":
        p=request.POST.get('name')
        q=request.POST.get('email')
        r=request.POST.get('pass1')
        s=request.POST.get('pass2')
        obj=RegisterDb(Name=p,Email=q,Password=r,ConfirmPassword=s)
        obj.save()
        return redirect(login)

def Loginuser(request):
    if request.method=="POST":
        un=request.POST.get('name')
        pwd=request.POST.get('pass')
        if RegisterDb.objects.filter(Name=un,Password=pwd).exists():
            request.session['Name']=un
            request.session['Password']=pwd
            messages.success(request,"Welcome")
            return redirect(index)
        else:
            messages.error(request, "Invaild username or password")
            return redirect(login)
    else:
        messages.error(request, "Invaild username or password")
        return redirect(login)

def UserLogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(Loginuser)

def booking(request):
    return render(request,"Booking.html")
def savebook(request):
    if request.method=="POST":
        p=request.POST.get('name')
        q=request.POST.get('email')
        r=request.POST.get('date')
        s=request.POST.get('des')
        t=request.POST.get('per')
        u=request.POST.get('kids')
        title = "Notification From Travela"
        msg=("Booking successfully you're Time will be Inform soon")
        send_mail(
            title,
            msg,
            'settings.EMAIL_HOST_USER',
            [q],
            fail_silently=False
        )
        obj=BookingDB(Name=p,Email=q,Date=r,Destination=s,Person=t,Kids=u)
        obj.save()
        messages.success(request, "Booking successfully....!")
        return redirect(booking)


def contact(request):
    return render(request,"contact.html")

def savecontact(request):
    if request.method=="POST":
        p = request.POST.get('name')
        q = request.POST.get('email')
        r = request.POST.get('sub')
        msg = request.POST.get('msg')
        title="Notification From Traveller"
        send_mail(
            title,
            msg,
            'settings.EMAIL_HOST_USER',
            [q],
            fail_silently=False
        )
        obj = ContactDB(Name=p,Email=q,Subject=r,Message=msg)
        obj.save()
        messages.success(request,"Message send....!")
        return redirect(contact)




def aboutpage(request):
    return render(request,"about.html")

def servicepage(request):
    return render(request,"service.html")

def packagepage(request):
    return render(request,"packages.html")
def blogpage(request):
    return render(request,"blog.html")

def singpage(request):
    return render(request,"singlepro.html")

def cali(request):
    return render(request,"singlecali.html")

def veni(request):
    return render(request,"singleveni.html")


def thai(request):
    return render(request,"singlethai.html")



def gallerypage(request):
    return render(request,"gallery.html")

def guidepage(request):
    return render(request,"guides.html")

def destinationpage(request):
    return render(request,"destination.html")

def testpage(request):
    return render(request,"testimonial.html")
def tourpage(request):
    return render(request,"tour.html")

def searchpage(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        post=SearchDB.objects.all().filter(California=search)
        return render(request,'packages.html',{'post':post})

def payment(request):
    return render(request,"payment.html")

@csrf_exempt
def success(request):
    return render(request,"success.html")

def profile(request):
    data = BookingDB.objects.all()
    return render(request,"Myprofile.html",{'data':data})
