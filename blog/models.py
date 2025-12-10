from django.db import models
class Yozuvchi (models.Model):
    ism=models.CharField(max_length=200)
    familiya=models.CharField(max_length=200,blank=True,null=True)
    telefon_raqam=models.CharField(max_length=20,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.ism 
    


# Create your models here.
