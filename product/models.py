from django.db import models

# Create your models here.
class Marque (models.Model):
    nom=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.nom

class Produit (models.Model):
    nom=models.CharField(max_length=200,null=True)
    prix=models.FloatField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    marque=models.ForeignKey(Marque,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom