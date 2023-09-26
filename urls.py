from django.urls import path #funcion para definir los caminos de los endpoints
from .views import Api #importando la clase que tiene los verbos http

urlpatterns = [
    path('', Api.as_view()),
    path('crear', Api.as_view()),
    path('actualizar/<int:id>', Api.as_view()),
    path('eliminar', Api.as_view())

]