from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('shop/',shop,name='shop'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('contact/',contact,name='contact'),
    path('catagory/<int:id>',catagory,name='catagory'),
    path('detail/<int:id>',detail,name='detail'),
    path('cart/',cart,name='cart'),
    path('wishlist/',wishlist,name='wishlist'),
    path('addtowishlist/<int:id>',addtowishlist,name='addtowishlist'),
    path('confirmorder/<int:id>',confirmorder,name='confirmorder'),
    path('delete/<int:id>',delete,name='delete'),
    path('deletewish/<int:id>',deletewish,name='deletewish'),
    path('addtocart/<int:id>',addtocart,name='addtocart'),
    path('minus/<int:id>',minus,name='minus'),
    path('plus/<int:id>',plus,name='plus'),
    path('checkout/',checkout,name='checkout'),
    path('orderhistory/',orderhistory,name='orderhistory'),
]
