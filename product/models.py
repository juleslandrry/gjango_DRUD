from django.db import models
import os
import datetime

# Create your models here.
class Marque (models.Model):
    nom=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.nom

def filepath(request,filename):
    old_filename=filename
    timeNow=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/',filename)


class Produit (models.Model):
    nom=models.CharField(max_length=200,null=True)
    prix=models.FloatField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    marque=models.ForeignKey(Marque,null=True,on_delete=models.SET_NULL)
    image=models.ImageField(upload_to=filepath,null=True,blank=True)
    
    def __str__(self):
        return self.nom