from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('index/', views.index),
        path('all/', views.all),
        path('saisi/', views.saisi),
        path('traitement/', views.traitement),

        path("traitement/<int:id>/", views.affiche),
        path("update/<int:id>/", views.update),
        path("updatetraitement/<int:id>/", views.updatetraitement),
        path("delete/<int:id>/", views.delete),
        path("all/<char:type>", views.type_filter)
]