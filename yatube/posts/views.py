from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main Page! Hello world!')

def group_posts(request, slug):
    return HttpResponse((f'Page for grouped by {slug} posts.\t\n'
                         f'{request.META}\t\n'))
