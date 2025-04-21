![Image](https://github.com/user-attachments/assets/676e9471-714b-4212-b1af-bb4e1824e83d)

Check it out here! 

https://artistalleyguide.pythonanywhere.com


Table of Contents:
- What is "Artist Alley Guide"?
- Demo
- Project Structure and Libraries Used


### What is "Artist Alley Guide"?
Artist Alley Guide is a website designed to help artists looking for conventions to sell their artwork in an artist alley. It contains information about around 30 conventions currently and their details regarding acceptance to sell.

![Image](https://github.com/user-attachments/assets/5cdfe240-5453-4660-96ce-1f9825d121eb)

### How can I utilize this site?
This website allows users to search for a convention by name, convention date, and artist alley application date. Clicking on a convention will take the user to a special page for that convention detailing its location, about the convention itself, how to apply, and more. Logged-in users are able to leave comments and ratings on conventions they have attended as well as favorite conventions for later.

![Image](https://github.com/user-attachments/assets/7175a1e5-97dd-4507-9996-ffe84d1066f6)

![Image](https://github.com/user-attachments/assets/c158a224-b6a3-459b-b46f-620d1772a51e)
### What is an "artist alley"?
An artist alley is a designated area at conventions for artists to sell their own artwork and merchandise. This can range from digital art, handcrafts, prints, apparel, and much more. Usually many artists have a mixture of original work and fan-art from existing media.

![Image](https://github.com/user-attachments/assets/fe079a3e-9b21-4381-afaf-94e6263a9e38)
Anime Expo 2024 Website

---

### Demo:
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/_XzZPQO8GPY/0.jpg)](https://www.youtube.com/watch?v=_XzZPQO8GPY)


---

### Installing 

To install and use, you will need **python** on your device due to Django being python-based.

https://www.python.org/downloads/

Next, it is suggested that you have python virtual environment to keep the intalled libaries in. 

https://docs.python.org/3/library/venv.html

As for libraries, you will need to install **Django, django-widget-tweaks, Pillow, and Bootstrap.**


#### Django 

https://www.djangoproject.com/download/

Follow the above to install Django onto your device.

Mac/Linux:
```
python -m pip install Django
```

Or Windows:
```
py -m pip install Django
```

#### django-widget-tweaks

https://pypi.org/project/django-widget-tweaks/

Installing using pip:
```
pip install django-widget-tweaks
```

#### Pillow

https://pypi.org/project/pillow/

Installing using pip:
```
pip install pillow
```

#### Bootstrap
https://getbootstrap.com/docs/4.0/getting-started/download/

Follow the above to install Bootstrap onto your device.

If you have npm available, use the following to install:
```
npm install bootstrap
```

If you do not have npm, follow the link below to install:

https://docs.npmjs.com/cli/v8/commands/npm-install


#### Running the Server

To run the server, make sure you are in the ArtistAlleyGuide Project folder and *manage.py* is present in the file path. Use the following to start the local development server:
```
python manage.py runserver
```

---

### Project Structure 
The structure can be broken down as shown here:
![Image](https://github.com/user-attachments/assets/057618a5-2890-493d-981a-7780cdd46992)

**Framework:**
For the backend, I used *Django*. This was due Django have a built-in database system and authentication system for users. It also does well with populating a template 'html' page which was needed for each convention page.

For the frontend, I used:
- HTML
- CSS
- Bootstrap

Bootstrap was chosen as its frontend library has many out-of-the-box templates for forms, headers, footers, cards, and much more. 



