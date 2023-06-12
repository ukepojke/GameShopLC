from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='gameproducts/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

