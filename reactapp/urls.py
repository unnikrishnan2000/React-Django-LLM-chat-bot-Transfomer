from django.urls import path
from . import views


urlpatterns = [
    path('api/queries/', views.search_query_list, name='search_query_list'),
]
