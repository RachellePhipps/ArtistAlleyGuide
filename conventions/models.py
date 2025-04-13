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
    #artist alley description
    art_description = models.TextField(blank=True, null=True)
    
    # rating
    rating_total = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, blank=True)  # For URL-friendly name

    # Favorites relationship
    favorited_by = models.ManyToManyField(User, related_name='favorite_cons', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        return self.rating_total / self.rating_count if self.rating_count > 0 else 0
    
# Convention images
class ConventionImage(models.Model):
    convention = models.ForeignKey(Convention, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# for comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    con = models.ForeignKey(Convention, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    
    def __str__(self):
        return f"{self.user.username} - {self.con.name}"
