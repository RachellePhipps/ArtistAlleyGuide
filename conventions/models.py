from django.db import models
from django.utils.text import slugify

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
    num_attend = models.IntegerField()
    # con type
    con_type = models.CharField(max_length=1, choices=CON_TYPES, default="G")

    # Con images
    image_urls = models.JSONField(default=default_image_urls)


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

    slug = models.SlugField(unique=True, blank=True)  # For URL-friendly name

    def save(self, *args, **kwargs):
    # Automatically create a slug from the name if it's not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name