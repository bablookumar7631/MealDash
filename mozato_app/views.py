from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileForm
from django import forms 
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from .models import*
from django.core import serializers
from django.contrib.auth.decorators import login_required


# Create your views here.
def indexPage(request):
    # data = All_Food.objects.all()
    
    foodData = All_Food.objects.all()
    paginator = Paginator(foodData, 4)
    data = paginator.get_page(1)

    data1 =  Food_category.objects.all()
    # show the number of item in the crt
    cart = request.session.get('cart',[])
    cartLength = len(cart)
    return render(request, 'index.html', {'data':data, 'data1' : data1, 'cartLength':cartLength})




def loadmorePage(request):
    pg = int(request.POST['page'])
    items = All_Food.objects.all()
    paginator = Paginator(items, 4)
    data = paginator.get_page(pg)
    items_json = serializers.serialize('json',data)
    data = {
        'items': items_json,
        'next': data.has_next()
    }
    return JsonResponse(data)



def categoryPage(request, cat_name):
    category = get_object_or_404(Food_category, category_name=cat_name)
    product = All_Food.objects.filter(food_category=category)
    # show the number of item in the crt
    cart = request.session.get('cart',[])
    cartLength = len(cart)
    return render(request, 'biryani.html', {'product': product, 'category': category, 'cartLength':cartLength})


def popupPage(request, food_id):
    food_detail = All_Food.objects.get(pk=food_id)
    # show the number of item in the crt 
    cart = request.session.get('cart',[])
    cartLength = len(cart)
    return render(request, 'popup.html',{'food_detail':food_detail, 'cartLength':cartLength})


def  searchPage(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = All_Food.objects.filter(food_name__icontains=searched)
        return render(request,'search.html',{'searched':searched, 'result':result})
    else:
        return render(request,'index.html')
    

def checkoutPage(request):
    cart = request.session.get('cart', [])
    # test for POST
    if request.method=='GET':
        # show the number of item in the crt
        cartLength = len(cart)
        return render(request, 'checkout.html',{'cartLength':cartLength, 'cart':cart })



def addToCartPage(request):
    food_id = request.POST.get('food_id')
    count = int(request.POST.get('count'))
    item = getFoodById(food_id)

    if 'cart' not in request.session:
        request.session['cart'] = []

    cart = request.session['cart']

    for food in cart:
        if str(food['food_id']) == food_id:
            food['quantity'] += count
            request.session.modified = True
            request.session.save()
            return JsonResponse({'qty':len(cart)})

    cart.append({
        'food_id': item.food_id,
        'name': item.food_name,
        'status': item.food_status,
        'price': float(item.food_price),
        'quantity': count,
    })
    request.session.modified = True
    request.session.save()
    return JsonResponse({'qty':len(cart)})


def getFoodById(foodId):
    return All_Food.objects.get(pk=int(foodId))




def signupPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'signup.html', context)
    
    # show the number of item in the crt
    cart = request.session.get('cart',[])
    cartLength = len(cart)
    context = {'form': form, 'cartLength' : cartLength}
    return render(request, 'signup.html', context)


def profilePage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated')
            return render('/')
    else:
        form = ProfileForm(instance=request.user.profile)
        context = {'form': form}
    return render(request, 'index.html', context)




def loginPage(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You are now logged in!')
            return redirect("/")
        else:
            messages.success(request, 'Invalid email and password')
            return redirect("login")
    else:
        # show the number of item in the crt
        cart = request.session.get('cart',[])
        cartLength = len(cart)
        return render(request, 'login.html', { "cartLength" : cartLength })


def logoutPage(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/')

