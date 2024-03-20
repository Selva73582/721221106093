from django.db import models

# Create your models here.

available_chioces = (
        ("yes","yes"),
        ('no',"no"),
    )

class CompanyName(models.Model):
    company_name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.company_name

class catrgories(models.Model):
    category_name=models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    company=models.ForeignKey(CompanyName,on_delete=models.CASCADE)
    catrgory=models.ForeignKey(catrgories,on_delete=models.CASCADE)
    productName=models.CharField(max_length=20)
    price=models.IntegerField()
    rating=models.FloatField()
    discount=models.IntegerField()
    availability=available_chioces

    def __str__(self) -> str:
        return self.productName

