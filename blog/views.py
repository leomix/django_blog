from django.shortcuts import render

# Create your views here.
def render_article(request):
    return render(request, 'articles.html')
