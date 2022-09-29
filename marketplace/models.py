from django.db import models
from django.urls import reverse

# class Category(models.Model):
#     category = models.CharField(max_length=100)

#     def __str__(self):
#         return self.category

# class Currency(models.Model):
#     currency = models.CharField(max_length=100)

#     def __str__(self):
#         return self.currency
    
# class Artist(models.Model):
#     artist_name = models.CharField( max_length=50)

#     def __str__(self):
#         return self.artist_name

class Testimonials(models.Model):
    user_name = models.CharField(max_length=100)
    review = models.CharField(max_length=500)
    rating = models.IntegerField(default=4)

    def __str__(self):
        return self.user_name
       
    def get_absolute_url(self):
        return reverse("details", args=[(self.id)])
    
    
        
class Collection(models.Model):
    name_of_NFT = models.CharField(max_length=30)
    artist_name = models.CharField( max_length=50)
    image = models.ImageField(upload_to= 'static/uploads')
    detail = models.CharField(max_length=500)
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_NFT
       
    def get_absolute_url(self):
        return reverse("details", args=[str(self.id)])

class MyModel(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    

# class Detail(models.Model):
    # nft_name = models.ForeignKey(Collection, on_delete=models.CASCADE)
    # image_nft = models.ForeignKey(Collection, on_delete=models.CASCADE)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # currency = models.ForeignKey(Currency, on_delete=models.CASCADE)