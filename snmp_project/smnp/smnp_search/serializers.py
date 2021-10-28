from django.db.models import fields
from rest_framework import serializers
from smnp_search.models import Categorie,Use,Equipement,Down,Interface


class CategorieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta :
        model = Categorie
        fields = ["id","nom"]

class EquipementSerializer(serializers.HyperlinkedModelSerializer):
    idCategorie = CategorieSerializer(read_only=True)
    class Meta :
        model = Equipement
        fields = ["id","ip","description","communityString","pollerEngine","idCategorie"]

class DownSerializer(serializers.HyperlinkedModelSerializer):

    class Meta :
        model = Down
        fields = ["id","idEquipement","heure"]

class UseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta :
        model = Use
        fields = ["id","idInterface","heure","speedInOctet","speedOutOctet"]


class InterfaceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta :
        model = Interface
        fields = ["id","ip","oids","description"]
