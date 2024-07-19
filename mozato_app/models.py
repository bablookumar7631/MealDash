from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default=None, max_length=100, null=True)
    mobile_no = models.CharField(max_length=10, unique=False)
    profile_img = models.ImageField(default='images/default.jgp', upload_to = 'profile_img', null=True, blank=True)

    def __str__(self):
        return str(self.user)






class Food_category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    cattegory_img = models.ImageField(default="")

    def __str__(self):
        return self.category_name
    
class All_Food(models.Model):
    food_status_choice = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    ]
    food_id = models.AutoField(primary_key=True)
    food_category =  models.ForeignKey(Food_category,on_delete=models.CASCADE,blank=True, null=True)
    food_name = models.CharField(max_length=100)
    food_img =  models.ImageField()
    food_price = models.FloatField()
    food_desc = models.TextField()
    food_status = models.CharField(choices=food_status_choice, null=True, blank=True, max_length=50)

    def __str__(self):
        return self.food_name + "("+ str(self.food_price)+")"
    
