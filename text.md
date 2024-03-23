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