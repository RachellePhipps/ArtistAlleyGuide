from django.db import models

class Convention(models.Model):
    CON_TYPE = [
    ("A", "Anime"),
    ("G", "Gaming"),
    ("C", "Comic"),
    ("F", "Fantasy"),
    ("FR", "Furry"),
    ("H", "Horror"),
    ("G", "General"),
]
    con_name = models.CharField(max_length=100)
    con_date = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    num_attend = models.IntegerField()
    con_type = models.CharField(max_length=2, choices=CON_TYPE)    
    booth_cost = models.IntegerField()
    travel_cost = models.IntegerField()
    apply_date = models.DateField()
    description = models.TextField()

