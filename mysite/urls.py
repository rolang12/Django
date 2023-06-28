from django.contrib import admin
from django.urls import path
from miapp import views
from django.urls.conf import include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('test2/', views.Crud.hola, name = "HolaPerros"),
    path('test/', views.Crud.segundo_hola, name = 'segundo_hola'),
    # path('crear-articulo/', views.create_article, name = "crear-articulo"),
    # path('show-articulo/', views.show_articles, name = "show-articulo"),
    path('edit-articulo/url<int:id>', views.Crud.edit_article_url, name = "edit-articulo-url"),
    path('edit-articulo/', views.Crud.edit_article, name = "edit-articulo"),
    path('find_article/<int:id>', views.Crud.find_article, name = "find_article"),
    path('show_all_articles/', views.Crud.show_all_articles, name = "show_all_articles"),
    path('delete_article/<int:id>/', views.Crud.delete_article, name = "delete-article"),
    path('crear-articulo-url/<str:title>/<str:body>/<str:public>', views.Crud.create_article, name = "crear-articulo-url")
    
]


# path('hola/<tipodato:nombre>/', views.hola, name = "HolaPerros")
