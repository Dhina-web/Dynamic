from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from django.template.loader import render_to_string
from .models import *
from .utils import cookieCart, cartData, guestOrder

# Create your views here.
def index(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    products=Product.objects.all()
    context={'products' :products, 'cartItems':cartItems}
    return render(request,'store/index.html',context)

def catalogue(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    context={'products' :products, 'cartItems':cartItems,}
    return render(request,'store/catalogue.html',context)

def sixinch(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    products=Product.objects.all()
    context={'products' :products, 'cartItems':cartItems}
    return render(request,'store/sixinch.html',context)


def eightinch(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    products=Product.objects.all()
    context={'products' :products, 'cartItems':cartItems}
    return render(request,'store/eightinch.html',context)


def eleveninch(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    products=Product.objects.all()
    context={'products' :products, 'cartItems':cartItems}
    return render(request,'store/eleveninch.html',context)


def twelveinch(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    products=Product.objects.all()
    context={'products' :products, 'cartItems':cartItems}
    return render(request,'store/twelveinch.html',context)






def store(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']
    
    """
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        cookieData = cookieCart(request) #step 2 in step 4 video 4
        cartItems = cookieData['cartItems'] # our cookiecart has a objects so indexing values
        
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order['get_cart_items']
        """

    products=Product.objects.all()
    context={'products' :products, 'cartItems':cartItems}
    return render(request,'store/store.html',context)

def cart(request):
    data = cartData(request)# step 2 in step 5 of video 4

    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    context={'items' :items, 'order':order}
    return render(request,'store/cart.html',context)

    """
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        cookieData = cookieCart(request) #step 2 in step 4 video 4
        cartItems = cookieData['cartItems'] # our cookiecart has a objects so indexing values
        order = cookieData['order']
        items = cookieData['items']
        

        try: # if the new user click add to cart button then create cookies
            cart= json.loads(request.COOKIES['cart']) #step(ii) of step 2 in step 1 video 4
        except:# except is used when a new user comes to website it prevents error thus by adding a empty objects to the cart cookies
            cart= {}
        print('Cart:',cart)
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart: # Step 1 in step 3 of video 4
            try:
                cartItems += cart[i]["quantity"]
                product= Product.objects.get(id=i) # i is the key and i is a product ID
                total=(product.price * cart[i]["quantity"]) # step(ii) in step 3 video 4
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]["quantity"]


                item = { # Step (iii) in Step 3 build cart items video 4
                'product':{ # first attribute is product assuming as a object
                    'id':product.id, # passing in the product attributes
                    'name':product.name,
                    'price':product.price,
                    'imageurl':product.image.url,

                        },
                    'quantity': cart[i]["quantity"], # second attribute
                    'get_total':total,  
                    }
                items.append(item) # adding the loop item in for loop to the dictionary


                if product.Shipping == False: # Step 3 in step 3 video 4
                    order['Shipping'] == True # if product is not digital needs to be shipped
            except: # step 4 in step 3
                pass
            """

def checkout(request):
    data = cartData(request)# step 2 in step 5 of video 4
    
    cartItems= data['cartItems']
    order= data['order']
    items= data['items']

    """
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        cookieData = cookieCart(request) #step 2 in step 4 video 4
        # our cookiecart has a objects so indexing values
        order = cookieData['order']
        items = cookieData['items']
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        """

    context={'items' :items, 'order':order}
    return render(request,'store/checkout.html',context)

def update_item(request):# once we parse the data it becomes python dictionary # we are
    data=json.loads(request.body)#parsing data
    productId=data['productId']
    action=data['action']

    print('Action:',action)
    print('ProductID:',productId)

    customer=request .user.customer
    product=Product.objects.get(id=productId)

    order, created=Order.objects.get_or_create(customer=customer, complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order, product=product)

    if action=="add":
        orderItem.quantity = (orderItem.quantity +1)
    elif action=="remove":
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
        
    return JsonResponse('item was added', safe=False)

def processOrder(request): #Step1 in Step 5 Process Order
    #print("Data:",request.body) # to ensure that the data was sent to process order
    transaction_id = datetime.datetime.now().timestamp() # step3 step1 in video 3
    data = json.loads(request.body) # Parsing the data

    if request.user.is_authenticated: # step 4 video 3
        customer= request.user.customer # if user is authendicatd get customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False) #get order
        # to get userFormData and shippingInfor 
        """
        total= float(data['form']['total']) # to get the speicfc info parsing the data learn parsing
        order.transaction_id = transaction_id # set the value for order transaction ID

        if total == order.get_cart_total: # Step 5 of Step 5 video 3
            order.complete = True # the total we pass ii (line 79) same as the total of cart total go ahead and set order complete to true
        order.save()

        if order.shipping == True: # step 6 in step 5 video 3
            # go ahead and create shipping address objects
            ShippingAddress.objects.create( # here shipping address is the model
                customer = customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],

            )
        """

    else:
        customer, order =guestOrder(request,data) # step 3 from step 6 video 4
        """
        print("User is not logged in")

        print('COOKIES:', request.COOKIES) # step2 in step 6 of video 4 accessing the data by sending the request of cookies from cookies we need to get the name email for the guest user
        name = data['form']['name'] # getting data here data is name from form and defining as a name
        email = data['form']['email'] 
        # getting the cart data note for quest user it's cookiecart

        cookieData = cookieCart(request) # getting cart data from cookiecart function and since we have assingend a cookieData function so we can pass in the data to cookieData function also
        items= cookieData['items'] # getting items from cookiedata and assinged as items
        # now we want to create a customer since it's guest user
        customer,created = Customer.objects.get_or_create(
            #if a customer visits second time and email matches
            email = email,  
        )

        customer.name = name # We can tarce them buy identifying the same name
        customer.save()# if customer wants to chnage the name they can 

        order = Order.objects.create(
            # seting up the staus of complete to false until the payment processed
            customer= customer,
            complete = False,
        )

        need to add these items to the data base and create and then attach them  to the object that was created previous lines of codes

        for item in items:
            # need  to qurey the product coz need to attach an order item to the product the item must be connected to the product and to an order
            product= Product.objects.get(id=item['product']['id'])
            # create an order item
            #OrderItem is a model
            orderItem= OrderItem.objects.create(
                product= product,
                order=order,
                quantity=item['qunatity'] # for quantity get the quantity 
            ) # on each iteration we are going to create order item and going to attach it to it's product
            """

    total= float(data['form']['total']) # to get the speicfc info parsing the data learn parsing
    order.transaction_id = transaction_id # set the value for order transaction ID

    if total == order.get_cart_total: # Step 5 of Step 5 video 3
        order.complete = True # the total we pass ii (line 79) same as the total of cart total go ahead and set order complete to true
    order.save()

    if order.shipping == True: # step 6 in step 5 video 3
        # go ahead and create shipping address objects
        ShippingAddress.objects.create( # here shipping address is the model
            customer = customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],

        )



    return JsonResponse('Payment Completed', safe=False) 