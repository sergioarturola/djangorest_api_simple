from rest_framework import serializers
from .models import Items #para importar la clase y asi poder convertir los modelos a json

class ItemsSerializer(serializers.ModelSerializer):

    #Con la subclase Meta especificamos el "modelo" y el "campo" a ser "serializado"
    class Meta:
        model = Items
        fields = ['id', 'name']
