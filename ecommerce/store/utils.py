import json
from .models import *

# step (i) in step 4 creating a cookie cart function 
# which will handle all the guest user logic codes here. and thus make our code more re usable however most sitea won't allow a guest user to place an order without an account

def cookieCart(request):
    try: # if the new user click add to cart button then create cookies
            cart= json.loads(request.COOKIES['cart']) #step(ii) of step 2 in step 1 video 4
        #it is used when a new user comes to website it prevents error thus by adding a empty objects to the cart cookies

    except:
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

            if product.digital == False: # Step 3 in step 3 video 4
                order['shipping'] == True # if product is not digital needs to be shipped 
        except: # step 4 in step 3
            pass
    
    return {'cartItems': cartItems, 'order':order, 'items':items} # this will be the cookie data

def cartData(request): # step 1 in step 5 of video 4
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request) #step 2 in step 4 video 4
        # our cookiecart has a objects so indexing values
        cartItems= cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'cartItems': cartItems, 'order':order, 'items':items} # this will be the cookie data


def guestOrder(request,data): #step 3 of step 6 video 4
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

    """ need to add these items to the data base and create and then attach them  to the object that was created previous lines of codes """

    for item in items:
        # need  to qurey the product coz need to attach an order item to the product the item must be connected to the product and to an order
        product= Product.objects.get(id=item['product']['id'])
        # create an order item
        #OrderItem is a model
        orderItem= OrderItem.objects.create(
            product= product,
            order=order,
            quantity=item['quantity'] # for quantity get the quantity 
        ) # on each iteration we are going to create order item and going to attach it to it's product
    return customer, order
