from django.db import models

# Create your models here.
class Product(models.Model):
    product_image = models.ImageField(upload_to="products/")
    category = models.CharField(max_length=90)
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name
    
def product_view(request):
    products = Product.objects.all()
    return render(request, 'main/predict.html' , {'products': products})


#Adding Features like to store prediction history
from django.conf import settings
from django.db import models

class CropPrediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField(default=6.5)
    rainfall = models.FloatField(default=100)
    predicted_crop = models.CharField(max_length=100)
    recommended_fertilizer = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Prediction by {self.user.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"