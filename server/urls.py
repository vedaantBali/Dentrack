# from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'dt/b2b/gql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
admin.site.site_header = "Dentrack Tool Admin Dashboard"
admin.site.site_title = "Dentrack Admin"
