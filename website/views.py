from django.shortcuts import render,redirect
from .models import dish,UserProfileInfo,CartObject, onlineorderform
from .forms import UserForm,UserProfileInfoForm, onlinefoodorderform
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.http import JsonResponse




# Create your views here.

def dish_view(request):
    did=request.POST.get('id')
    dtitle = request.POST.get('title')
    ddescription = request.POST.get('description')
    dimg1 = request.POST.get('img1')
    dimg2 = request.POST.get('img2')
    dprice = request.POST.get('price')
    dPcategory=request.POST.get('Pcategory')
    dScategory = request.POST.get('Scategory')
    davailable = request.POST.get('available')
    dvalue_for_two = request.POST.get('value_for_two')

    if did is not None and dtitle is not None and ddescription is not None and dimg1 is not None and dimg2 is not None and dprice is not None and dPcategory is not None and dScategory is not None and davailable is not None and dvalue_for_two is not None:
        row = dish(id=did, title = dtitle, description=ddescription, img1=dimg1, img2=dimg2, price=dprice,Pcategory=dPcategory, Scategory = dScategory,available=davailable,value_for_two=dvalue_for_two )
        row.save()

    obj=dish.objects.all()


    return render(request, 'dish.html', {'row1':obj})


@login_required
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect (("http://localhost:8000/"))


def register(request):

    registered = False

    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() :
            user=user_form.save()
            user.set_password(user.password)
            user.save()

        registered = True
        return redirect("http:localhost:8000/user_login/")

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered} )




def user_login(request):

    if request.method=='POST':
        usernme = request.POST.get('username')
        passwrd= request.POST.get('password')

        user = authenticate(username=usernme, password=passwrd)

        if user:
            if user.is_active:
                login(request,user)
                return redirect(("http://localhost:8000/"))



        else:
            return redirect(("http://localhost:8000/user_login/"))
            #print("Username: {} and password {}". format(username,password))
            #return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'login.html',{})


def productlist_view(request):
    x= request.GET.get("type")
    request.session["flag"] = "0"
    appetizer = dish.objects.filter(Scategory="Appetizer", Pcategory = x)
    entree = dish.objects.filter(Scategory = "EN", Pcategory = x)
    return render(request, "product_list_page.html", {'appetizer': appetizer, 'entree':entree})


@login_required(login_url="http://localhost:8000/user_login/")
def cartpage(request):

    pid = request.POST.get("id")
    cid = request.GET.get("cartid")
    fname = request.POST.get("name")
    faddress = request.POST.get("address")
    fcity = request.POST.get("city")
    fzipcode = request.POST.get("zipcode")
    fstate = request.POST.get("state")
    fphonenumber = request.POST.get("phoneno")
    femail = request.POST.get("email")

    if fname is not None and faddress is not None and fcity is not None and fzipcode is not None and fstate is not None and fphonenumber is not None and femail is not None:
        row2 = onlineorderform(name=fname, address=faddress, city = fcity,zipcode=fzipcode, state=fstate, phoneno = fphonenumber, email=femail)
        row2.save()

    foodform = onlinefoodorderform()


    x = 0

    if pid is not None and request.session.get("flag")=="0" :
        request.session["flag"] = 1

        f = CartObject.objects.filter(productid=pid, userid = request.user)

        if len(f)>0:
            x=int(f[0].quantity)
            CartObject.objects.filter(productid=pid, userid = request.user).delete()



        obj = dish.objects.filter(id=pid)
        protitle=obj[0].title
        proprice=obj[0].price

        obj1 = CartObject(productid=pid,producttitle=protitle,price=proprice,quantity=x+1, userid=request.user)
        obj1.save()


    obj = CartObject.objects.filter(userid=request.user)

    Amount = []
    for i in obj:
        Amount.append ((float(i.price)) * (int(i.quantity)))

    total = sum(Amount)
    request.session["total"]=total
    pos=[]
    for i in range(0,len(Amount)):
        pos.append(i)



    return render(request, "cartpage.html", {'cartobjects': zip(obj,Amount,pos),"total":total, 'foodform':foodform})



def index(request):

    return render (request,"index.html", None)

def menu(request):
    return render(request, "menu.html", None)


def about(request):


    return render (request, "about.html", None)

def navbar(request):
    return render (request, "navbar.html", None)

def blog(request):
    return render (request, "blog.html", None)

def contact(request):
    return render (request, "contact.html", None)



def removefromcart(request):
    pid = request.GET.get("cartid")

    CartObject.objects.filter(cartid = pid).delete()
    return redirect("http://localhost:8000/cartpage/")



def payment_process(request):
	host = request.get_host()
	paypal_dict = {
       'business': "niteshdsharma44@gmail.com" ,
       'amount': '1',
       'item_name': 'Item_Name_xyz',
       'invoice': ' Test Payment Invoice',
       'currency_code': 'USD',
       'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
      # 'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
       #'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
       }
	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'payment_process.html', {'form': form })


@login_required()
def checkout(request):



    if 'isuserloggedin' in request.session:

        base = request.POST.get("price")

        return render(request, "payment_process.html",{ 'baseprice': base,  'cartid': request.session['cartitd']})
    else:
        return redirect("http://localhost:8000/")



def  changeQuantity(request):
    mode = request.GET.get("mode")
    id =  request.GET.get("cartid")
   # price = request.GET.get("price")

    if mode is  not None:
        quant =CartObject.objects.filter(cartid=id)[0].quantity
        price=CartObject.objects.filter(cartid=id)[0].price
        if mode =="1":
            CartObject.objects.filter(cartid=id).update(quantity=int(quant)+1)

            #CartObject.objects.filter(cartid=id, price = (float(price) + float(price)))
            #totalprice = (float(price) + price))
            #CartObject.objects.filter(cartid = id).update(totalprice)
        if mode =="2":
            if quant>1:
                CartObject.objects.filter(cartid=id).update(quantity=int(quant)-1)
           # CartObject.objects.filter(cartid=id).update(price=(float(price) - float(price)))




    return  redirect("http://localhost:8000/cartpage/")


@login_required(login_url="http://localhost:8000/user_login/")
def mycart(request):
    return redirect("http://localhost:8000/cartpage/")





















