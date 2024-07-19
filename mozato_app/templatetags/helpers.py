from django import template
from ..models import*

register = template.Library()



@register.simple_tag
def getFoodImagePath(foodId):
    return All_Food.objects.get(pk=int(foodId)).food_img
