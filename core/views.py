from django.shortcuts import render,redirect ,get_object_or_404
from .forms import Userprofile , Userform
from django.contrib.auth import login as auth_login
from .models import Item , OrderItem , person
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def redir(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username , password)
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request , 'registration/login.html' ,{})

def signup(request):
    if request.method == 'POST':
        userprofile=Userprofile(data=request.POST)
        userform=Userform(data=request.POST)
        if userform.is_valid() and userprofile.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            profile = userprofile.save(commit = False)
            profile.user = user
            profile.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username , password = password)
            if user:
                auth_login(request,user)
            return redirect('home')

    else:
        userprofile = Userprofile()
        userform = Userform()
    return render(request, 'registration/signup.html', {'user_form': userform , 'profile_form':userprofile})

@login_required(login_url='login')
def homepage(request):
    return render(request,'home.html')

def more(request , name):
    data = Item.objects.filter(category =name)
    if request.method =='POST':
        pk = request.POST['pk']
        quan = request.POST['quantity']
        item = get_object_or_404(Item, id=pk)
        size = request.POST['size']
        print(size)
        # print(quan)
        ordered = OrderItem(title=item.title, price=item.price, description=item.description, category=item.category,
                            image=item.image, user=request.user.username, ordered='False', quantity=quan ,
                            size = size)
        ordered.save()
        messages.success(request , 'Your Item has been added to cart.')
        return redirect('../{0}/more'.format(item.category))

    return render(request , 'more.html' , {'data':data})

def added(request , pk):

    item = get_object_or_404(Item , id = pk)
    quan = request.POST['quantity']
    # print(quan)
    ordered = OrderItem(title = item.title , price = item.price , description = item.description , category = item.category,
                        image = item.image , user = request.user.username , ordered ='False' , quantity = 1)
    ordered.save()
    return redirect('../{0}/more'.format(item.category))

def mycart(request):
    ordered = OrderItem.objects.filter(user = request.user.username , ordered = 'False')
    return render(request , 'cart.html' ,{'ordered':ordered})

def delordered(request ,pk):
    item = get_object_or_404(OrderItem , id=pk)
    item.delete()
    return  redirect('mycart')

def buyitem(request):
    item = OrderItem.objects.filter(user = request.user.username , ordered = 'False')
    for i in item:
        i.ordered ='True'
        i.save()
    messages.success(request , 'Your Order has been placed ! ')
    return  redirect('home')

def myorders(request):
    ordered = OrderItem.objects.filter(user = request.user.username , ordered = 'True')
    return render(request , 'myorders.html' ,{'ordered':ordered})

def profile(request):
    return render(request,'profile.html')

def editprofile(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        address= request.POST['address']
        city= request.POST['city']
        phone = request.POST['phone']
        per = person.objects.filter(user = request.user ).update(name = name ,gender = gender ,
                                                                                         address = address ,city =city,
                                                                                         phone= phone)

        return redirect('profile')
    return render(request,'editprofile.html')
