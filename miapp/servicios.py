from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.http import JsonResponse

class Servicios():
    
    public = True
    title = ''
    body = ''
    
    def datosprueba():
        
        lenguajes = ['Python', 'Java', 'C#', 'JavaScript', 'PHP']
        return  lenguajes
    
    def get_all_articles_services():

        # return Article.objects.all()
        return Article.objects.order_by('title')[:3] #si le pongo -title lo ordena de forma descendent [] limitar numero de registros


    def create_article_services(title, body, public):

        article = Article(
            title = title,
            body = body,
            likes = 0,
            public = public
        )
        #guardar los datos
        article.save()

        return article
    
    # def get_all_articles_services():
        
    #     try:
    #         article = Article.objects.get(id=3)
    #         response = f"Articulo: <h3> {article.title}</h3>"
    #     except:
    #         response = "articulo inexistente"
        

        # return HttpResponse(response)
    
    def find_article_services(request, id):
        try:
            article = Article.objects.get(pk=id)
            # response = f"Articulo: <h3> {article.title}</h3>"
        except:
            response = "articulo inexistente"

        return article
        
    def edit_article_services(request):
        if request.method == 'POST':
            try:
                # Obtén el artículo y modifica los datos
                article = Article.objects.get(pk=request.POST['id'])
                article.title = request.POST['title']
                article.body = request.POST['body']
                article.public = request.POST['public']
                article.save()
                
                
                # return JsonResponse({'message': 'Artículo actualizado exitosamente.'})
            except Article.DoesNotExist:
                return JsonResponse({'error': 'Artículo no encontrado.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        return article
            
        


    def edit_article_url_services_url(id):

        #obtengo el registro
        article = Article.objects.get(pk=id)

        try:
            #modifico los datos
            article.title = "Batman"
            article.body = "Batman es el mejor"
            article.public = True
            #guardo los datos
            article.save()  

            return HttpResponse(f"Articulo:  {article.title}")

        except Exception as e:

            return HttpResponse(f"Error al encontrar el articulo: {e}")

    def delete_article_services(id):

        try:
            article = Article.objects.get(pk=id)
            article.delete()

        except Exception as e:
            raise e
        
        return article