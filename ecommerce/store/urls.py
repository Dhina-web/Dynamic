from django.urls import path
from.import views

urlpatterns=[
    path('',views.index,name='index'),
    path('catalogue/',views.catalogue,name='catalogue'),
    path('sixinch/',views.sixinch,name='sixinch'),
    path('eightinch/',views.eightinch,name='eightinch'),
    path('eleveninch/',views.eleveninch,name='eleveninch'),
    path('twelveinch/',views.twelveinch,name='twelveinch'),
    path('store/',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update_item/',views.update_item,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'), # step(ii) in Step1 of Process order Step5
]