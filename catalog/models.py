from django.db import models
from django.urls import reverse
import uuid # Required for unique album instances

# Create your models here.

class Genre(models.Model):
    """Model representing a album genre."""
    name = models.CharField(max_length=200, help_text='Enter a music genre (e.g. Rock)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Album(models.Model):
    """Model representing a record album (but not a specific copy of that album)."""
    title = models.CharField(max_length=200)

    #Foreign key used because album can have only one musician/band, but musicians/bands can have multiple albums
    #Musician as a string rather than object because it hasn't been declared yet in the file
    musician = models.ForeignKey('Musician', on_delete=models.SET_NULL, null=True)

    year = models.PositiveSmallIntegerField()

    # ManyToManyField used because genre can contain many albums. Albums can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this album')

    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this album."""
        return reverse('album-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

    

class AlbumInstance(models.Model):
    """Model representing a specific copy of a album (i.e. that can be bought from the record store)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular album across whole store')
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True) 
    sale_date = models.DateField(null=True, blank=True)

    SALE_STATUS = (
        ('m', 'Maintenance'),
        ('a', 'Available'),
        ('s', 'Sold'),
    )

    status = models.CharField(
        max_length=1,
        choices=SALE_STATUS,
        blank=True,
        default='m',
        help_text='Album availability',
    )

    class Meta:
        ordering = ['sale_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.album.title})'


class Musician(models.Model):
    """Model representing a musician."""
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular musician instance."""
        return reverse('musician-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
