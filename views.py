from rest_framework import status
from rest_framework.views import APIView, Response
from .models import Items
from .serilizers import ItemsSerializer

#clase que retornara vistas, es decir "clases basadas en vistas"
class Api(APIView):

    #---metodo get
    def get(self, request):

        items = Items.objects.all()#para obtener todos los datos de la base
        items_data = ItemsSerializer(items, many=True).data
        response_data = {"dato" : items_data}#variable que contiene el diccionanrio (json) de respuesta

        return Response(response_data, status=status.HTTP_200_OK)
    

    #---metodo post
    def post(self, request):
        name = request.data.get('name')
        #en caso de que el cuerpo no tenga "name" como parametro mandamos como respuesta mala solicitud
        if name is None:
            response_data = {"mala peticion" : "propiedad no valida"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        Items.objects.create(name=name)#Del nombre que p
        response_data = {"respuesta" : "item creado"}
        return Response(response_data, status=status.HTTP_200_OK)
    

    #---metodo put
    def put(self, request, id):
        name = request.data.get('name')
        #filtrando por id
        item = Items.objects.filter(id = id).first()
        #verificando si es nulo
        if item is None:
            response_data = {"respuesta":"Item no encontrado"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        #si no entro al if
        item.name = name
        item.save()
        response_data = {"respuesta":"Item actualizado"}
        return Response(response_data, status=status.HTTP_200_OK)
    

    #---metodo delete
    def delete(self, request):
        #obteniendo el id del item del cuerpo del request
        id = request.data.get('id')
        #del id recuperado del cuerpo del request lo filtramos en el item
        item = Items.objects.filter(id = id).first()
        #si no encuentra nada 
        if item is None:
            response_data = {"respuesta" : "Item no encontrado"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        #si no entra en el if entonces eliminamos
        item.delete()
        response_data = {"respuesta" : "Item eliminado"}
        return Response(response_data, status=status.HTTP_200_OK)

    