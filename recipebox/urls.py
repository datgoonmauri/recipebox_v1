from django.urls import path
from recipebox import views

urlpatterns = [
    path('', views.index,name='homepage'),
    path('addauthor/',views.add_author),
    path('addrecipe/', views.add_recipe),
    path('author/<int:id>', views.author),
    path('recipe/<int:id>', views.recipe)
]
