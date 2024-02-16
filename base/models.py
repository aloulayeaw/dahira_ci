from django.db import models

# Create your models here.


class Blog(models.Model):
    tittle=models.CharField(max_length=255)
    date=models.CharField( max_length=255)
    designation=models.CharField(max_length=255, blank=True)
    photo=models.ImageField( upload_to='photos/%Y/%m/%d/')
    is_featured = models.BooleanField(default=False, null=True , blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tittle