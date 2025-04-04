from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


def default_image_urls():
    return ["https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1200px-No_image_available.svg.png"]


 # conventions
class Convention(models.Model):
    CON_TYPES = {
    "A": "Anime",
    "G": "Games",
    "F": "Furry",
    "C": "Comic",
    "H": "Horror",
    "G": "General",
    }
    # con name
    name = models.CharField(max_length=64)
    # date happening
    con_date = models.DateField()
    # city
    city = models.CharField(max_length=30)
    # state
    state = models.CharField(max_length=2)
    # website
    website = models.CharField(max_length=64)
    # number of attendees
    num_attend = models.IntegerField(default=1)
    # con type
    con_type = models.CharField(max_length=1, choices=CON_TYPES, default="G")

    # Con description
    description = models.TextField(blank=True, null=True)

    # Con google maps location
    location = models.TextField(blank=True, null=True)

    # number of days
    num_days = models.IntegerField(default=1)

    # Convention image 
    image = models.ImageField(upload_to='images/', default='images/default.png')

    # Artist Stuff

    # average apply date
    apply_date = models.DateField()
    # table cost
    table_cost = models.IntegerField()
    # travel cost
    travel_cost = models.IntegerField()
    # number of artists
    num_artists = models.IntegerField()
    
    # rating
    rating = models.FloatField(null=True, blank=True)


    # Convention Center TODO


<<<<<<< HEAD
=======


>>>>>>> 507e6d1d914bf551225fb5b42d206ae28d950235
    slug = models.SlugField(unique=True, blank=True)  # For URL-friendly name

    # Favorites relationship
    favorited_by = models.ManyToManyField(User, related_name='favorite_cons', blank=True)

    def save(self, *args, **kwargs):
    # Automatically create a slug from the name if it's not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
# Convention images
class ConventionImage(models.Model):
    convention = models.ForeignKey(Convention, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD

# for comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    con = models.ForeignKey(Convention, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.con.name}"
=======
>>>>>>> 507e6d1d914bf551225fb5b42d206ae28d950235
