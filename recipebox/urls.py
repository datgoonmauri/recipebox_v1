from django.conf.urls import url
from django.urls import path
from recipebox import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('addauthor/',views.add_author),
    path('addrecipe/', views.add_recipe),
    path('author/<int:id>', views.author),
    path('recipe/<int:id>/', views.recipe, name="recipe"),
    path('login/', views.loginview),
    path('logout/', views.logoutview, name='logout'),
    path('editrecipe/<int:id>/', views.edit_recipe, name='editrecipe'),
    path('favorite/<int:id>/', views.favorite, name='favorite'),
    path('unfavorite/<int:id>/', views.unfavorite, name='unfavorite'),
]
