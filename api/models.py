from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class bakery(models.Model):
    bakery_id=models.AutoField(primary_key=True)
    Ingredients=models.CharField(max_length=100,choices=(('milk','milk'),('egg','egg'),('sugar','sugar')),default="milk")
    iteam_name=models.CharField(max_length=100,default=0)
    Ingredients_quantity=models.CharField(max_length=100,choices=(('milk','80%_milk'),('egg','40%_egg'),('sugar','90%_sugar')),default="50%_sugar")
    cost_price=models.IntegerField()
    selling_price=models.IntegerField()
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return "iteam-->"+self.iteam_name + "~~~~"+"price-->"+str(self.selling_price)


    
   
class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default=0)
    phoneNumber=models.CharField(max_length=10,default=0)
    address=models.CharField(max_length=200,default=0)
    product=models.ForeignKey(bakery,on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return self.name
    

