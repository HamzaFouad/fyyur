Fyyur
-----

## Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

## Tech Stack
 * **Python3**
 * **Flask**
 * **SQLAlchemy ORM**
 * **PostgreSQL**
 * **Flask-Migrate**
 * **HTML, CSS, Js, Bootstrap3** 

<!--## Installation-->
<!--```-->
<!--git clone git@github.com:HamzaFouad/fyyur.git-->
<!--pip install -r requirements.txt-->
<!--FLASK_APP=app.py FLASK_DEBUG=true flask run-->
<!--```-->

## Main Files: Project Structure
```
$
├── README.md
├── app.py
├── config.py
├── error.log
├── fabfile.py
├── forms.py
├── migrations/
├── requirements.txt
├── static/
│   ├── css/
│   ├── fonts/
│   ├── img/
│   └── js/
└── templates/
    ├── errors/
    ├── forms/
    ├── layout/
    └── pages/
```

#### Overall:
* Models are located in the `MODELS` section of `app.py`.
* Controllers are also located in `app.py`.
* The web frontend is located in `templates/`, which builds static assets deployed to the web server at `static/`.
* Web forms for creating data are located in `form.py`


#### Highlight folders:
* `templates/pages` -- Defines the pages that are rendered to the site. These templates render views based on data passed into the template’s view, in the controllers defined in `app.py`. These pages successfully represent the data to the user, and are already defined for you.
* `templates/layouts` -- Defines the layout that a page can be contained in to define footer and header code for a given page.
* `templates/forms` -- Defines the forms used to create new artists, shows, and venues.
* `app.py` -- Defines routes that match the user’s URL, and controllers which handle data and renders views to the user.
* Models in `app.py` -- Defines the data models that set up the database tables.
* `config.py` -- Stores configuration variables and instructions, separate from the main application code.


## Setup
To start and run the local development server,
Initialize and activate a virtualenv:

1. **Download the project starter code locally**
```
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ python -m virtualenv fyyur_env
$ source fyyur_env/bin/activate
```

2. **Clone repo and install dependencies**
```
$ git clone git@github.com:HamzaFouad/fyyur.git
$ pip install -r requirements.txt
```
3. **Run:**
```
FLASK_APP=app.py flask run
```
4. **Navigate to Homepage**
` [http://localhost:5000](http://localhost:5000/)`