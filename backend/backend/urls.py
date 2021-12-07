from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphiql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

#http://127.0.0.1:8000/graphiql

