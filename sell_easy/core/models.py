from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q, Max, QuerySet
from core.account.models import Profile

# Create your models here.

class Store(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    
    def __str__(self) -> str:
       return self.name


class Category(models.Model):
    #owner
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    #owner
    store = models.ForeignKey(Store, related_name='products', on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='products', null=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveIntegerField()
    
    def discount(self, discount=20):
        self.price = self.price * (discount/100)
        return self.price
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ('name', "-price",)
        verbose_name = "Products"
        # constraints = [models.CheckConstraint(check=Q("price__gt=12000"), name="price_gt_1200")]
    
    
    @property
    def num_reviews(self):
        num = self.ratings.count()
        return num
    
    
    @num_reviews.getter
    def get_num_reviews(self):
        return self.num_reviews
    
    def average_rating(self):
        rating = self.ratings.aggregate(models.Sum("rating"))
        total = rating.get("rating__sum")
        return total / self.get_num_reviews if total is not None and self.get_num_reviews is not None else 0
        
    
class Rating(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name="ratings", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]) # 0-5
    remark = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.rating}"