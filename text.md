# DJ CRM

- Create git repo with proper licence and python gitignore and readme file.
- Clone existing repository for project in folder
```bash 
 git clone <url>
```
- Go inside project folder 
```bash
cd <foldername>
```

### Install virtualenv 
```bash
pip install virtualenv
```

### create virtual environmnt 
```bash
virtualenv <venvname> 
```
### Activate virtual environment in bash and linux
```bash
source <venvname>/Scripts/activate
```

### Activate virtual environment in windows
```bash
.\<venvname>\Scripts\activate
```

### install django and make requirement file having all dependencies.
```bash
pip install django==3.1.4
pip freeze > requirements.txt
```

### Create project in existing folder 
```bash
django-admin startproject djcrm .
```

### Run project 
```bash
python manage.py runserver
```

### Migrate changes 
```bash 
python manage.py migrate
```

### Create new app 
```bash
python manage.py startapp <appname>
```

- Add filename to main project folders settingfile inside installed app
- Goto models file inside new app file 
- Create class for create table in database and also give variables for define schema of table.

### For create changes in database we need to make migrations 
```bash 
python manage.py makemigrations
```
` - it will create migration file for create table in database with given variable names in class of model file`
```bash
python manage.py migrate
```
` - it will apply migrations or changes to database `

### We can use Model Manager for manage objects 

`suppose we created model Car`
```bash
class Car(models.Model):
    CAR_MANUFACTURER = (
        ("Audi","Audi"),
        ("BMW","BMW"),
        ("Ferrari","Ferrari"),
    )
    make = models.CharField(max_length=20, choices=CAR_MANUFACTURER)
    model = models.CharField(max_length=20),
    year = models.IntegerField(default=2015)
```
`To access car manager, we use:`
```bash
## to access model manager
Car.Objects
```
`Using manager we can create new cars:`
```bash
## To create new car
Car.objects.create(make="BMW", model="x5", year=2017)
```

### Query sets
`Using the manager we can query the database:`
```bash
## query for all cars in database
Car.objects.all()

## query for cars with the make equal to Audi
Car.objects.filter(make="Audi")

## query for cars with a year greater than 2016
Car.objects.filter(year__gt=2016)
```

### To use python shell 
`Here you can write codes and statements like in normal shell like cmd and powershell`
```bash
## normal shell like cmd 
python 
>>> from xyz import abc 

## in django use python shell
python manage.py shell
>>> from leads.models import Leads
>>> Leads.objects.all()
>>>
>>> exit()  ## for exit from shell
```

### To create user directly 
`Run below command in command line `
```bash 
python manage.py createsuperuser
## it will ask for username, email and password 
Username : 
Email : 
Password : 
Password again : 
## then ask for conformation (y/n) press y and enter
```

### Find user through shell and right way 
```bash 
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.all()
<QuerySet [<User: pratikr1521998@gmail.com>]>    ## response
``` 
`Make admin user`
```bash
admin_user = User.objects.get(username="pratikr1521998@gmail.com")
## get retrive only single match from database
admin_user
<User: pratikr1521998@gmail.com>
```
### Create admin 
```bash 
from leads.models import Agent
agent = Agent.objects.create(user=admin_user)
agent
<Agent: Agent object (1)>
exit()
```
### Make method to return user inside Agent
```bash 
def __str__(self):
    """it return str representations of users"""
    return self.user.email
```
`Now we can see Agents from shell`
```bash
python manage.py shell
from leads.models import Agent
Agent.objects.all()
<QuerySet [<Agent: pratikr1521998@gmail.com>]>   ## Response
```
`Create lead `
```bash
>>> from leads.models import Lead 
>>> pratik_agent = Agent.objects.get(user__email="pratikr1521998@gmail.com")  
>>> pratik_agent
<Agent: pratikr1521998@gmail.com>
>>> Lead.objects.create(first_name="mehul", last_name="panchal", age=35, agent=pratik_agent)
<Lead: Lead object (1)>
>>> exit()
```
`Create method inside Lead to view str representation of Lead`
```bash
def __str__(self):
    return f"{self.first_name} {self.last_name}"
```
`Retrive leads`
```bash
python manage.py shell
>>> from leads.models import Lead
>>> Lead.objects.all()
<QuerySet [<Lead: mehul panchal>]>
```
<br><br>
## Register models to admin for view in admin 
<hr>

- Run project 
```bash
python manage.py runserver
```
- Go to Baseurl/homepage 
- Go to route "./admin"
- It will ask for user id and password login through we created earliar superuser login id and password. 
- `You can see site administration page available group option`
- `We need to add all models at adinistration page so for that we need to add models in admin page`

### Add users in admin as below
```bash
from .models import User, Lead, Agent

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
## Now you can access all these models in django administration side 
```

<br><br>
## Views 
<hr>

There is 3 ways to render content

### 1. `Using HttpResponse`
<br>

- Go to views pag inside leads 
- Create view for homepage 
```bash
def home_page(request):
    return HttpResponse("Hello World !") 
```
- Go to root path 
- Go to main project folder inside urls file 
- Put url inside that file so we can view our template or content 
```bash 
from django.contrib import admin
from django.urls import path

from leads.views import home_page            ## import home_page from leads app views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page)                       ## this url will help us to view our homepage 
]
```

### 2. `Using html pages inside app template folder`
<br>

`You can also make folders of template so you can render template `
- Make folder inside app leads named templates
- Inside templates folder make one more folder named leads `django by default get templates by that path`
- Make html page inside that folder for view.
`We careated named home_page.html`
```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h5>Wel come to my home page</h5>
</body>
</html>
```
### Now we will render template so we can see content inside of html file in specific route.
```bash
from django.shortcuts import render
from django.http import HttpResponse

 
def home_page(request):
    # return HttpResponse("Hello World !") 
    return render(request, "leads/home_page.html")
```
`Now it render html page instead html response`

### 3. `Using templates inside templates folder in root path`
<br>
- Create templates folder inside root path.
- Configure that path in base project folders setting file's template path.

`We already have imported path library and already set baseurl as root path`

```bash
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
```

- Set dir path inside templates 
```bash 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates" ],                             ## set here dir path
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

`Make a second_page inside templates folder`

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Second page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h5>This is the second page.</h5>
</body>
</html>
```
`We need to render second page `
```bash 
from django.shortcuts import render
from django.http import HttpResponse

 
def home_page(request):
    # return HttpResponse("Hello World !") 
    # return render(request, "leads/home_page.html")
    return render(request, "second_page.html")
```
`Now we can see second page at home root`
<br><br><br>

## Context 
<hr>

- We can render information as contect in our html page by pass content in views.

```bash
from django.shortcuts import render
from django.http import HttpResponse

 
def home_page(request):
    # return HttpResponse("Hello World !") 
    # return render(request, "leads/home_page.html")
    
    context = {
        "name":"partik",
        "age":26
        }
    return render(request, "second_page.html", context=context)
```
`We need to add contaxt values in html page `
```bash 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Second page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h5>This is the second page.</h5>

    {{name}} ## here in place of {{name}} show value inside contect key name e.g: pratik
    {{age}} ## here in place of {{age}} show value inside contect key age e.g: 26

</body>
</html>
```

`We can also show contents inside our database using context`
- We will show leads on our second page 

```bash 
from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
 
def home_page(request):
    # return HttpResponse("Hello World !") 
    # return render(request, "leads/home_page.html")
    
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request, "second_page.html", context=context)
```

`We also need to change in our html page for view leads`
```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Second page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h5>This is the second page.</h5>
    <!-- leads seen here -->
    {{leads}}                 
</body>
</html>
```
`Now we will be able to see leads on our homepage.`
`For intractive look we can use render it as below`
```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Second page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h5>This is the second page.</h5>
    <!-- leads seen here -->
    {{leads}}    
    <ul>
        {% for lead in leads %}
        <li>{{ lead }}</li>
        {% endfor %}
    </ul>             
</body>
</html>
```

## Specific url file for all apps 

- Create url file inside app folder.
```bash
from django.urls import path  
from .views import home_page


urlpatterns = [
    path('', home_page)
]
```
`we need to configure new url file with system url file of base app`
```bash
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads"))
]
```
`make app path like below also give app name so easily identify path`
```bash
from django.urls import path  
from .views import home_page


app_name = "leads"

urlpatterns = [
    path('all/', home_page)
]
```
`now you can see second page on below url`
```bash
127.0.0.1/leads/all/
## Here leads is app name and all is route/endpoint.
```

## Now we will change all names and functions according to out project 

`we can route of home page of leads app `
```bash
from django.urls import path  
from .views import lead_list


app_name = "leads"

urlpatterns = [
    path('', lead_list)
]
```
`according to that we need to change out name of fuction`
```bash
def lead_list(request):
    # return HttpResponse("Hello World !") 
    # return render(request, "leads/home_page.html")
    
    leads = Lead.objects.all()
    context = {
        "leads":leads
    }
    return render(request, "leads/lead_list.html", context=context)
```
`Remember don't forgot to change path of template`
`We also have to change out template name to lead_list and content as well`

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <style>
        .leads{
            margin: 10px 10px;
            padding: 10px;
            background-color: bisque;
        }
    </style>
</head>
<body>
    <div class="leads">
        <h2>Leads : </h2>
        {% for lead in leads %}
            {{ lead.first_name }}    ## we can also get inside variables as well.
        {% endfor %}
    </div>
</body>
</html>
```

- We need to make one more page for render details of this lead on click
- We need to make another function for handle request getting from leads 
`Create below function for view leads `
```bash
def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse("Here is a detail view")
```
`now we need tyo give url for the same to render response`

```bash
from django.urls import path  
from .views import lead_list, lead_detail


app_name = "leads"

urlpatterns = [
    path('', lead_list),
    path('<pk>/', lead_detail)   ## here we can see response of leads for a perticular lead
]
```
- Go to below url for see both the leads which has id 1 and 3.
```bash 
127.0.0.1/leads/1/
## or 
127.0.0.1/leads/3/
```
`It will print detail of given id in console as we can see in function `

`Below is a response in console`
```bash
3
krish panchal
[25/Mar/2024 18:24:32] "GET /leads/3/ HTTP/1.1" 200 21
1
mehul panchal
[25/Mar/2024 18:25:18] "GET /leads/1/ HTTP/1.1" 200 21
```
`It also render HttpResponse on screen`

### Now we need to on click on lead it redirect to detail page of that perticular lead.

- We will add lead in ancher tag so we can able to redirect o click.
```bash
    <h3>Leads :</h3>
    {% for lead in leads %}
    <div class="leads">
        <a href="/leads/{{ lead.pk }}/">{{lead.first_name}} {{lead.last_name}}</a> Age : {{lead.age}}
    </div>
    {% endfor %}
```
`Now on click this will redirect to detail page`

### We need to make a detail page so we can render all detail related to lead
- After make detail page we need to render it 
```bash 
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)

    context={
        "lead":lead
    }
    return render(request, "leads/lead_detail.html", context=context)
```
`we also need to do some changes in detail page`
```bash
<body>
    <a href="/leads">Go back to leads</a>
    <hr>
    <h3>This is details of {{lead.first_name}}</h3>
    <p>This person's Age : {{ lead.age }}</p>
</body>
```
`It will render detail of lead as well as it allow to go back at leads`
<br><br>

## Create Leads 
<hr>

`create new function for render page lead create inside views`
```bash 
def lead_create(request):
    return render(request, 'leads/lead_create.html')
```
`Create new page lead_create html for render inside leads/templates `
<br><br>


### Forms
<hr>
Create one more file inside leads forms.py 

`Create form fields inside that`
```bash
from django import forms  


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
```

`create context for render that form on page `

```bash 
from .forms import LeadForm

def lead_create(request):
    context = {
        "form":LeadForm()
    }
    return render(request, 'leads/lead_create.html', context)
```

`We also need to make a changes in html page for render form and also get data through it `
`Add below lines in create lead page for get data from form`

```bash 
<body>
    <a href="/leads">Go to leads</a>
    <hr>
    <h1>Create new lead</h1>
    <form method="post" action="">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit"> Submit </button>
    </form> 
</body>
```

`for test print response of form by this way`
```bash 
def lead_create(request):
    print(request.POST)                 ## It will print response 
    context = {
        "form":LeadForm()
    }
    return render(request, 'leads/lead_create.html', context)
```

`it return response in console`
```bash 
<QueryDict: {'csrfmiddlewaretoken': ['DWs41xnOmL29piPFVrnL9W9ptms4TsBWksF8tnQRhokK17Wa05YsjG9PZcEe5qC1'], 'first_name': ['xcv'], 'last_name': ['xcv'], 'age': ['25']}>
```

`Lets proper this output`
```bash 
def lead_create(request):
    form = LeadForm()                             ## Make a blank form instance
    if request.method == "POST":                  ## check is method is post
        print("Receiving the post request")       
        form = LeadForm(request.POST)             ## Get data in form 
        if form.is_valid():                       ## Validate form data 
            print("the form is valid")
            print(form.cleaned_data)              ## Print form data in valid json format
        
    context = {
        "form":LeadForm()                         ## This will help to render form on page
    }
    return render(request, 'leads/lead_create.html', context)
```
`Now lets store lead `
```bash 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm


def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        print("Receiving the post request")
        form = LeadForm(request.POST)
        if form.is_valid():
            print("the form is valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']        ## Grab first name
            last_name = form.cleaned_data['last_name']          ## Grab last name 
            age = form.cleaned_data['age']                      ## Grab age
            agent = Agent.objects.first()                       ## grab first agent from agents 
            Lead.objects.create(                                ## Create lead using all data
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            print("lead has been created!")   
            return redirect('/leads')                           ## This will redirect on leads page      
    context = {
        "form":LeadForm()
    }
    return render(request, 'leads/lead_create.html', context)
```

`We can make exact data gethering form`

```bash 

```