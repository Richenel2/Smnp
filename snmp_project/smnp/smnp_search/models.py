
from django.db import models
from django.utils import timezone
from .smnpFunction.function import get_bulk_auto,hlapi
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

# Create your models here.

class Categorie(models.Model):

    """ Categorie des Equipements"""

    nom = models.CharField(max_length=25)

    class Meta:
        #nom d'affichage
        verbose_name = "Categorie"

    def __str__(self) -> str:
        return self.nom

class Equipement(models.Model):

    """ Encapsulation des Equipements"""

    ip = models.CharField(max_length=25, unique= True)
    description = models.CharField(max_length=25)
    communityString = models.CharField(max_length=25, verbose_name="Community String")
    pollerEngine = models.CharField(max_length=25)
    idCategorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        #nom d'affichage
        verbose_name = "Equipement"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        try: 
            try:
                Interface.objects.get(ip=self.ip)
            except ObjectDoesNotExist:
                its = get_bulk_auto(self.ip, ['1.3.6.1.2.1.2.2.1.1', '1.3.6.1.2.1.2.2.1.2','1.3.6.1.2.1.2.2.1.5','1.3.6.1.2.1.2.2.1.10','1.3.6.1.2.1.2.2.1.16'], hlapi.CommunityData(self.communityString), '1.3.6.1.2.1.2.1.0')
                for it in its :
                        a=[v for k,v in it.items()]
                        Interface(ip=self.ip,oids=a[0],description=a[1],speed=a[2],lastInOctet=a[3],lastOutOctet=a[4]).save()
            except MultipleObjectsReturned:
                    pass
        except RuntimeError:
            pass
    def __str__(self) -> str:
        return self.description


class Down(models.Model):
    
    idEquipement = models.ForeignKey('Equipement', on_delete=models.CASCADE)
    heure = models.DateTimeField(default=timezone.now, 
                                verbose_name="heure")
    class Meta :
        verbose_name = "Equipement Down"

class Use(models.Model):
    
    idInterface = models.ForeignKey('Interface', on_delete=models.CASCADE)
    heure = models.DateTimeField(default=timezone.now, 
                                verbose_name="heure")
    speedInOctet =models.IntegerField()
    speedOutOctet =models.IntegerField()

    class Meta :
        verbose_name = "Equipement utilisation"

class Interface(models.Model):

    ip = models.CharField(max_length=40)
    oids = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    speed = models.IntegerField()
    lastInOctet =models.IntegerField()
    lastOutOctet =models.IntegerField()
    lastTimeTakeData = models.DateTimeField(default=timezone.now, 
                                verbose_name="Heure des dernieres donnees")
    class Meta : 
        verbose_name = "Interface"