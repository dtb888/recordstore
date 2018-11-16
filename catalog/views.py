from django.shortcuts import render
from catalog.models import Album, Musician, AlbumInstance, Genre
from django.views import generic

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_albums = Album.objects.all().count()
    num_instances = AlbumInstance.objects.all().count()
    
    # Available albums (status = 'a')
    num_instances_available = AlbumInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_musicians = Musician.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_albums': num_albums,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_musicians': num_musicians,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class AlbumListView(generic.ListView):
    model = Album
    paginate_by = 20

class AlbumDetailView(generic.DetailView):
    model = Album

class MusicianListView(generic.ListView):
    model = Musician
    paginate_by = 20

class MusicianDetailView(generic.DetailView):
    model = Musician


