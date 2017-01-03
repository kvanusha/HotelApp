from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Room,Menu,Food,Order,Sweets,Beverages,Chats,User
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="login/")
def index(request):
    return render(request,'hotelapp/index.html',{})


def about(request):
    return render(request,'hotelapp/about.html',{})

def signup(request):
    if request.method=='GET':
        users = User.objects.all()
        return render(request, 'hotelapp/signup.html', {users:'users'})

    if request.method=='POST':
        emailid= request.POST['email']
        username1=request.POST['username']
        password1=request.POST['password']
        newuser=User.objects.create_user(email=emailid,username=username1,password=password1)
        newuser.save()
        #users = User.objects.all()
        return render(request,'hotelapp/signup.html',{})


@login_required(login_url="login/")
def contact(request):
    return render(request,'hotelapp/contact.html',{})

@login_required
def listfoods(request):
    foods=Food.objects.all()
    return render(request,'hotelapp/food2.html',{'foods':foods})

@login_required
def listrooms(request):
    rooms=Room.objects.all()
    return render(request,'hotelapp/rooms.html',{'rooms':rooms})

@login_required
def liststarters(request):
    sweet=Sweets.objects.all()
    beverage = Beverages.objects.all()
    chat = Chats.objects.all()

    return render(request,'hotelapp/starters.html',{'sweet':sweet,'beverage':beverage,'chat':chat})

@login_required
def listorders(request):
    if request.method=='GET':
        foods = Food.objects.all()
        rooms = Room.objects.all()
        return render(request,'hotelapp/orders.html',{'foods':foods,'rooms':rooms,'ordercomplete':False})
    elif request.method=='POST':
        foodid=request.POST['foods']
        fooditem=Food.objects.get(pk=foodid)
        roomid=request.POST['rooms']
        roomitem=Room.objects.get(pk=roomid)

        now=datetime.now()
        #user_id=1
        print request.user
        user_id=request.user.id
        print user_id
        neworder=Order(food_item=fooditem,room_type=roomitem,user_id=user_id,order_timestamp=now,status='In Progress')
        neworder.save()
        #newid=neworder.id
        #print newid
        print neworder.id
        # send and email with order id to customer
        message = 'Order has been placed with order id: ' + str(neworder.id)
        emailcustomers('order', 'vidya.s099@gmail.com', [request.user.email], 'Order Placed', message)

        #newid.save()
        #send_mail('Subject here', 'Here is the message.', 'kva.anusha@gmail.com', ['kva.anusha@gmail.com'], fail_silently=False)
        orders = Order.objects.all()
        items = Order.objects.get(pk__in=id).order_by('date')
        #orderid = request.POST['orders']
        #orderitem = Order.objects.get(pk=Order.id)
        return render(request, 'hotelapp/orders.html',{'orders':orders,'ordercomplete':True,'items':items})

        #return HttpResponse('YOu called the post method with food id'+str(foodid))

'''def placeorder(request):
    #orders = Order.objects.all()
    #order=request.POST['orders']
    return HttpResponseRedirect('/hotel/orders')'''
#This function creates te user

def user(request):
    user1 = User.objects.create_user(email='vidhya2@gmail.com', username='test2', password='test@12345')
    user1.save()
    # user1.password = 'test'
    # user1.save()
    return HttpResponse('user created succcessfully')

#this function is to send the email
def emailcustomers(emailtype,fromemail,to,subject,message):
    res = send_mail(subject,message,fromemail,to,fail_silently=False)
    return True


def sendSimpleEmail(request):
   res = send_mail('Subject here', 'Here is the message.', 'kva.anusha@gmail.com', ['kva.anusha@gmail.com'], fail_silently=False)
   return HttpResponse('%s'%res)

#This function defines the how to login inito a particuar page

def login_page(request):
    if request.method=='GET':
        return render(request,'hotelapp/login.html',{})

    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            #print 'login success'
            #Login is successful
            if user.is_active:
                login(request, user)
            else:
                print 'Non active user'
            return render(request, 'hotelapp/index.html', {})
        else:
            print 'login failure'
            #Login Fail Send some message
            return render(request, 'hotelapp/login.html', {'error':'Username or password Wrong'})

#Thsi function defines how to logout from the page

def logout_page(request):
    logout(request)
    return render(request, 'hotelapp/index.html', {})
    #return HttpResponseRedirect('hotel/signup/')
    #return HttpResponse("i am in logout page")