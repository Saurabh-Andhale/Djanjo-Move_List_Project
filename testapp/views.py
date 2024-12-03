from django.shortcuts import render
from six import moves
from testapp.models import Movie

def index_view(request):
    return render(request,'testapp/index.html')

def list_movie_view(request):
    movie_list=Movie.objects.all()
    my_dict={'movie_list':movie_list}
    return render(request,'testapp/move.html',my_dict)


