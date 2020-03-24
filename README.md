***Django Project Cheat Sheet***

***Basic Setup***

**Block 1 - Create main djnago project**
    [
         Step 1 : create a fresh django project **djnago-admin createproject eduliant_main**
         Step 2 : change project name to eduliant_main_project
         Step 3 : add git ignore **touch .gitignore**
    ]

**Block 2 - Create django app**
    [
        Step 1 :  add app **python manage.py startapp edu_defaultapp**
        Step 2 : start serve **python manage.py runserver**
    ]

**Block 3 - configure db with django app (optional)**
    [
        Step 1 : We can go with default sqllite db or
        Step 2 : configure DB -postgres
                    **sudo su postgres**
                    **enter password - your computer password**
                    **enter psql**
                    postgres started

        Step 3 : create db **CREATE DATABASE edu_db_name;**
        Step 4 : configure settings.py with postgres
                    DATABASES = {
                            'default': {
                                'ENGINE': 'django.db.backends.postgresql',
                                'NAME': 'edu_db_name',
                                'USER': 'postgres',
                                'PASSWORD':'niitR1234',
                                'HOST':'localhost',
                                'PORT':'5432'
                            }
                        }
    ]

**Block 4 - Create SuperUser**
    [
        Step 1 : do migrate **python manage.py migrate**
        Step 2 : do migrations **python manage.py makemigrations**
        Step 3 : do migrate **python manage.py migrate**
        Step 4 : create super user **python manage.py createsuperuser**
        (deeplearning/deeplearning)
    ]

**Block 5 - Register the app**
    [
        Step 1 : Register the app in settings.py under
                    INSTALLED_APPS = [
                    'edu_defaultapp.apps.EduDefaultappConfig',
                    'edu_onboarding.apps.EduOnboardingConfig',
                    '',...
                    ]
    ]

**Block 6 - django project to default app View Template configuration**

    [
        Step 1 : in urls.py import views.py of edu_defaultapp
        Step 2 : add a url pattern - path('',views.home,name='home'),
        Step 4 : go to views.py of edu_defaultapp and create a function home
                def home(request):
                    return render(request,'base/home.html')
        Step 5 : create a director in edu_defaultapp templates/base/home.html
        Step 6 : run the server, everything should work fine and home page is displayed
    ]

***Advance Setup***

**Block 1 - create a static folder for all bootstarp configuration,image upload also create a base template and call it in app templates**
    [
        Step 1 : create a static folder in the main app, call css,js and all supporting folders for bootstrap put in the static folder
        Step 3 : create director templates/eduliant_main/base.html,in base.html file in befote <html></html> tag call {% load staticfiles %} - to load media and image
        Step 4 : this base.html contains headers and footers used throughout the web app,in-between header and footer where we want to call other templates add
                    {% block content %}{% endblock%}
        Step 5 : go to settings.py and under TEMPLATES,'DIRS': [], add 'eduliant_main/templates/base_content'
        Step 6 : in settings.py add
                        STATICFILES_DIRS = [
                                    os.path.join(BASE_DIR,'eduliant_main/static/')
                                ]

                                STATIC_ROOT = os.path.join(BASE_DIR,'static')
                                STATIC_URL = '/static/'
        Step 7 : run **python manage.py collectstatic**, and run server
    ]

***Add Open Iconic***

download the folder and put it into project static folder as we have added a new file
we need to call

python manage.py collectstatic

---------------------------
Public Key

Private Key



--------------------------------------------
Everytime we make any changes to our django project file we need to
1. restrat gunicorn
sudo systemctl restart gunicorn
2. sudo nginx -t && sudo systemctl restart nginx


How to reset a password
# python manage.py changepassword <user_name>






















