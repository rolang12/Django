from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.http import JsonResponse
from .servicios import Servicios as Services

class Crud:

    public = True
    title = ''
    body = ''
    services = Services

    def __init__(self, request):

        if (request.method == 'POST'):
            self.title = request.POST['title']
            self.body = request.POST['body']
            self.public = request.POST['public']
        else:
            self.title = request.GET['title']
            self.body = request.GET['body']
            self.public = request.GET['public']
            
    #controlador / vista
    def hola(request, hola = ''):

        ejemplo = Services
        ejempl = ejemplo.datosprueba()


        return render(request, 'index.html', {
            'variable': ejempl,
            'title': ejempl,
            'lenguajes': ejempl
        })

    def segundo_hola(request):
        return render(request, 'segundo_hola.html')

    #crear articulo
    def create_article(self, title, body, public):

        article = Services.create_article_services(title, body, public)

        return HttpResponse("Usuario creado: "+  article.body  + article.public)

    #mostrar articulo
    # def show_articles(request):

    #     articles = Services.get_all_articles_services()
    #      article = Article.objects.all() trae todos los objetis
    #     return HttpResponse(articles)

    #editar articulo desde url
    def edit_article_url(request, id):
        
        article = Services.edit_article_url_services(id)

        return HttpResponse(article)

       

    def find_article(request, id):

        article = Services.find_article_services(request, id)

        return render(request, 'edit_article.html', {'article': article})

    #editar articulo
    def edit_article(request):

        # obtengo el registro manera estandar
        # id = int(request.POST['id'])
        # article = Article.objects.get(pk=request.POST['id'])

        # try:
        #     modifico los datos
        #     article.title = request.POST['title']
        #     article.body = request.POST['body']
        #     article.public = request.POST['public']

        #     #guardo los datos
        #     article.save()     
            
        #     return HttpResponse(f"Articulo:  {article.title}")
        
        # except Exception as e:
            
        #     return HttpResponse(f"Error al encontrar el articulo: {e}")

        # Manera asincrona
        article = Services.edit_article_services(request)
    
        return redirect('find_article', id=article.id)
       
            
    #listar articulos
    def show_all_articles(request):

        articles = Services.get_all_articles_services()

        return (render(request, 'articles.html', {'articles': articles}))

    #eliminar articulo
    def delete_article(request, id):

        article = Services.delete_article_services(id)
        
        return redirect(f'show_all_articles {article.title} ha sido borrado')

        