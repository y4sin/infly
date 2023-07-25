from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=225)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    discription = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items_images', blank=True, null=True)

    def __str__(self):
        return self.name