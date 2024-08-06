from .models import Catagory,Cart,Wishlist

def cat(request):
    CatData=Catagory.objects.all()
    total=0
    count1=0
    wcount=0
    if request.user.is_authenticated:
        
        cr=Cart.objects.filter(u_id=request.user)
        count1=Cart.objects.filter(u_id=request.user).count()
        wcount=Wishlist.objects.filter(u_id=request.user).count()
        
        for i in cr:
            total+=i.total()
        
    return {'CatData':CatData,'total':total,'count1':count1,'wcount':wcount}