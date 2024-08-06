from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Catagory(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=20)
    def __str__(self):
        return self.cname
    
    
class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=25)
    pprice=models.IntegerField()
    disc=models.TextField()
    pimage=models.ImageField(upload_to='img')
    c_id=models.ForeignKey(Catagory,on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.pname
    
    
class Top_Product(models.Model):
    tid=models.AutoField(primary_key=True)
    t_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.t_id.pname
    
    
class Cart(models.Model):
    cid=models.AutoField(primary_key=True)
    p_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.u_id.username
    
    def total(self):
        
        return self.p_id.pprice * self.quantity
    
class Wishlist(models.Model):
    wid=models.AutoField(primary_key=True)
    p_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.u_id.username
    
    
class O_tracker(models.Model):
    otid=models.AutoField(primary_key=True)
    status=models.CharField(max_length=50)
    
    def __str__(self):
        return self.status
    
class Order(models.Model):
    o_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    phone=models.BigIntegerField()
    address=models.TextField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
    amount=models.IntegerField()
    pay_type=models.CharField(max_length=30)
    odate=models.DateTimeField(auto_now_add=True)
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    ot_id=models.ForeignKey(O_tracker,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class O_item(models.Model):
    item_id=models.AutoField(primary_key=True)
    o_itemid=models.ForeignKey(Order,on_delete=models.CASCADE)
    p_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    sub_total=models.IntegerField()