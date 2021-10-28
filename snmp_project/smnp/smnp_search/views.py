from rest_framework import viewsets
from .serializers import *
from .models import *
from django.http import HttpResponse
from threading import Thread
from django.utils import timezone
from time import sleep
from random import randint, choice 
from .smnpFunction.function import get,hlapi
_max = 2**32
start_command = [False]
def start(request):


    def categorie():
        Use.objects.all().delete()
        while start_command[0]:
            for i in Equipement.objects.all():
                for j in Interface.objects.filter(ip=i.ip):
                    try :
                        obj = get(i.ip,["1.3.6.1.2.1.2.2.1.10."+j.oids, "1.3.6.1.2.1.2.2.1.16."+j.oids],hlapi.CommunityData(i.communityString))
                        print(obj)
                        inOctet = int(obj["1.3.6.1.2.1.2.2.1.10."+j.oids] if obj["1.3.6.1.2.1.2.2.1.10."+j.oids] != "" else 0)
                        outOctet = int(obj["1.3.6.1.2.1.2.2.1.16."+j.oids] if obj["1.3.6.1.2.1.2.2.1.16."+j.oids] != "" else 0)
                        time=timezone.now()
                        speedInOctet=(inOctet-j.lastInOctet + (_max if inOctet<j.lastInOctet else 0))*800/((time.timestamp() -j.lastTimeTakeData.timestamp())*(j.speed if j.speed != 0 else 1)*(2**20)/1000)
                        speedOutOctet=(outOctet-j.lastOutOctet + (_max if outOctet<j.lastOutOctet else 0))*800/((time.timestamp() -j.lastTimeTakeData.timestamp())*(j.speed if j.speed != 0 else 1)*(2**20)/1000)
                        Use(idInterface=j, speedInOctet=speedInOctet, speedOutOctet=speedOutOctet).save()
                        j.lastInOctet=inOctet
                        j.lastOutOctet=outOctet
                        j.lastTakeTime=time
                    except RuntimeError :
                        pass
                try :
                    get(i.ip, [i.pollerEngine], hlapi.CommunityData(i.communityString))
                    try:
                        Down.objects.get(idEquipement=i).delete()
                    except Exception:
                        pass
                except RuntimeError :
                    print( i.description +" est Down")
                    try:
                        Down.objects.get(idEquipement=i)
                    except Exception:
                        Down(idEquipement=i).save()
            sleep(10)


    if start_command[0] == False : 
        start_command[0] = True    
        h = Thread (target=categorie)
        h.start()
    return HttpResponse("<H1> Done ... </H1>")

def stop (request):
    start_command[0]= False
    return HttpResponse("<H1> Done ... </H1>")

class CategorieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    filterset_fields = ['nom']
    search_fields = ['nom']

class EquipementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer
    filterset_fields = ["ip","id","description","communityString","idCategorie","pollerEngine"]
    search_fields = ["ip","id","description","communityString","idCategorie","pollerEngine"]

class DownViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Down.objects.all()
    serializer_class = DownSerializer
    filterset_fields = ["idEquipement","id","heure"]
    search_fields = ["idEquipement","id","heure"]

class UseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Use.objects.all()
    serializer_class = UseSerializer
    filterset_fields = ["idInterface","id","heure","speedInOctet", "speedOutOctet"]
    search_fields = ["idInterface","id","heure","speedInOctet", "speedOutOctet"]

class InterfaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Interface to be viewed or edited.
    """
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer
    filterset_fields = ["ip","id","oids","description"]
    search_fields = ["ip","id","oids","description"]
