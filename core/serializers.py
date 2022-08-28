from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Carro, Marca


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"