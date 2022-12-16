from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    context: dict[str:str] = {
        'position': 'Это главная страница проекта Yatube',
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    context: dict[str:str] = {
        'position': 'Здесь будет информация о группах проекта Yatube',
        'slug': slug,
    }
    return render(request, 'posts/group_list.html', context)
