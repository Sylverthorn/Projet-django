from django.urls import path
from . import views
from . import type_views

urlpatterns = [
        
        #POUR LES TECHNIQUE
		
        path('index/', views.index),
        path('all/', views.all),
        path('saisi/', views.saisi),
        path('traitement/', views.traitement),

        path("affiche/<int:id>/", views.affiche),
        path("update/<int:id>/", views.update),
        path("updatetraitement/<int:id>/", views.updatetraitement),
        path("delete/<int:id>/", views.delete),
        

        # POUR LES TYPE
        path('index_type/', type_views.index),
        path('all_type/', type_views.all),
        path('saisi_type/', type_views.saisi),
        path('traitement_type/', type_views.traitement),

        path("affiche_type/<int:id>/", type_views.affiche),
        path("update_type/<int:id>/", type_views.update),
        path("updatetraitement_type/<int:id>/", type_views.updatetraitement),
        path("delete_type/<int:id>/", type_views.delete)
]