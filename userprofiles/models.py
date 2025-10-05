from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name ="userprofile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class Shop(models.Model):
    user = models.OneToOneField(User, related_name = "shop", on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=350)
    slug = models.SlugField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads/images/", blank=True, null=True)



    def __str__(self):
        return self.shop_name