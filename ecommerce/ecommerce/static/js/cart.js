console.log("HI")
var updateBtns= document.getElementsByClassName('update-cart') // Just setting update-cart class a variable to query set as updateBtn coz we can't directly call the html class name//

for ( var i=0; i < updateBtns.length ; i++){
    /* var i = 0 means we going to iterate from 1st product so index is zero
    i < updateBtns.length means while i is less than our product update the cart
    by increamenting the item in the cart that is i++ */
    updateBtns[i].addEventListener('click', function(){
    /* on each iteration we want to get our query set that is updateBtns[i] so on each iteration i (item) is will be increamented
    .addEventListener for each button the type of event 'on click' will be added 
    and "on click" what needs to be done so we add function this function is going to exceute on each click some of fucntionalities below */
        var productId= this.dataset.product
        var action = this.dataset.action
        console.log('ProductId:', productId, 'Action:', action)
        
        /* 'this' represents when the item is clicked on and we are adding the custom attribute as a data set.product so when the item is clicked the console will be initiated to add the item thus by holding readyly the product that's going to be added

        once the item is clicked then the action of add item will be excuted. */

        console.log('USER:', user)
        if (user == 'AnonymousUser'){ //passing in the cookie data if the user is not authendcated can be able to add items to the cart
            addCookieItem(productId, action) 
        }else{
            updateUserOrder(productId, action) // these are for backend services and process
        }


    })
    
}
function addCookieItem(productId, action){ //step (1)in step 2 of video 4
    console.log('User is not authendicated')

    if (action =='add'){
        if (cart[productId]==undefined){ //step (ii) in step 2 of step 1 video 4
            cart[productId] = {'quantity':1} //if the item is not in the cart add quanity of 1 to cart of an item
        }
        else{
            cart[productId]['quantity'] +=1 //if the product is already exisits increase the quantity of the item
        }
    if (action =='remove'){
        if (cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }
            if (cart[productId]['quantity'] <=0){ // if the item quantity becomes less than one delete the entire product form cart
                delete cart[productId]
            }
        else{
            cart[productId]['quantity'] -=1 // if the action is remove so the item will be there and decrease the quantity of it
        }
        
    }
    console.log('cart:',cart) //step(iv) in step2 of step 1 video 4
    document.cookie ='cart=' +JSON.stringify(cart)+ ";domain=;path=/"
    location.reload()
    }
}

function updateUserOrder(productId, action){
    console.log('User is authendicated') /* this function is used to detemine whether the user is a registerd or not  and this fucntion will be triggered if our user is logged in then our function sends a post request to the server */
    var url='/update_item/' // this is where we want to send our data to//
    /* to send the data use fetch API */
    fetch(url,{
        method:'POST',    // what kind of data type going to send to the backend//
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken, //study fetch API to understand better//
        },     // headers going to be the object//
        body:JSON.stringify({'productId':productId, 'action':action})   /* Body is the data that we gonna send to the back end as an object pass our product ID and action send it as a JSON string  */
    }) // passing url to send the data to//
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data)
    })

} 