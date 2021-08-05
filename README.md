# Mictec_Django

## Set-up

- Ensure that you have git installed into your machine, The link for downloading git is [Git Download](https://git-scm.com/download/win)

- If you dont have a github account, Kindly create one. Open this link in a new tab and create your account [GitHub Signup](https://github.com/join)

- You can learn the basics of git from this tutorial just one hour [free code camp git tutorial](https://www.youtube.com/watch?v=RGOj5yH7evk&t=7s)

- The next thing is to ensure that you have Python and Anaconda into your machine, You can download Python via [Python Download](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe) and then do the installations. For anaconda terminal the download link is [Anaconda Download](https://www.anaconda.com/download/#windows), Download it and do the installations.

- The next step is that we will need an editor where we will write our codes, You can choose one of this; sublime text, Atom and VS Code. The link for downloading sublime text is [Sublime Text Download](https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe), For Atom is [Atom](https://atom.io/download/windows_x64) and for VS Code is [VS Code Download](https://code.visualstudio.com/download)

- Now we are good to get our hands dirty with the framework for perfectionist:+1: :+1: :+1:

# Lesson I

## Getting Started

- After Doing all the above installations, Go to your windows search bar and search for anaconda and open it. Also you can confirm if you have python installed by typing **python --version** on the anaconda terminal.

- The next step is to download the virtual environment, It is always important to create an environment where you will store all the dependencies required by your project. There are two packages that i usually use for this case; virtualenv wrapper and the virtualenv. For our project we will use the virtualenv, though you can still learn how to use the virtualenv wrapper and use it. To install the virtualenv type **_pip install virtualenv-win_**. After the installation has taken place, lets create a folder where we will store our projects, type **_mkdir Mictec_** then cd into that directory by typing **_cd Mictec_** on your terminal.

> NB: You ll need to pay attention to the spellings of the folder you have created and the folder you want to cd to.

- Let us now create a folder where we will house our project and the environment that we will create. To do this we ll do as we have done above **_mkdir BlogEnv_** and then we ll cd into that folder by doing **_cd BlogEnv_**.
  > Now you should be an expert in that.
- Now lets create our environment by typing the following command into the terminal **_python -m venv BlogEnv_** where the BlogEnv is the name of our environment. To activate our environment we will type **_BlogEnv/Scripts/activate_** into the terminal. You should see the name of BlogEnv behind the word Base on your terminal.

- if you are using atom you can open your project folder on the editor by typing **_atom ._** and for VS Code you can type **code .** for sublime you can type **_subl ._**. If any of that does not work, "Physically go to your local disk" and open the folder Users, then the folder named User or has your name, Scroll down and open the first folder that you created i.e The **Mictec folder\***, Now you should see the folder named **BlogEnv**, Slowly drag and drop it :shipit: to your prefered editor.

- The next step is to now install django, Simply type **_pip install django_** in your terminal.

## Creating our Django Project

- After we have installed Django, starting the project should now be a childs play. To start the project simply type **_django-admin startproject src_** Where src is the name of the project that you would want to create, It can be an E-Commerce Project, a blog, a todolist, space-z, etc.

> On your editor you should see that some additional files have been added

- I want you to cd into the project that you have created above for my case i will **_cd src_**

- To run our project, type **_python manage.py runserver_** on your terminal you should see something amazing. Copy paste the address that you see [Local Host](http://127.0.0.1:8000/) http://127.0.0.1:8000/ and paste it on your browser's url, You should see a congratulations message telling you that you have run django successfully.

> Now that is not magic, it's your talent and your hard work

- Now get back to your terminal and you should see an error message that reads;

  > You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s)

- To do away with this error message just type **_python manage.py migrate_** and then rerun your local server by using our usual command **_python manage.py runserver_**

- You can further access the admin panel by adding /admin to your url it should be something like ***http://127.0.0.1:8000/admin***. You should now be able to see a django admin login page. But you need to create a user that can be able to login. To do this type **_python manage.py createsuperuser_** it should prompt you to input a username, email and password and confirmation password.

- After you have done this rerun the server with the same command **_python manage.py runserver_** go to your admin url ***http://127.0.0.1:8000*** in your browser.

- You should now be able to login using the credentials that you have used in registering the new superuser on the terminal.

- After you have logged in you will be meet a nice looking user panel, with the group(s) and Users tabs on the left side. Now i want you to enjoy yourself by creating new users and new groups.

> Now Repeat the whole process for how many times? Let's just say 1000 times and we ll be looking at the next [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean). In the next class we will create our first application and do something more constractive. Well, I hope you enjoyed that.

> Happy Coding!!!

# Lesson II

- From our last class i can confidently state that, most of you now have the capabilities of creating a new project, running the migrations, creating a superuser and may be have some basic understanding of how the django admin panel works.
- Additionally, most of you know what the settings.py does, what the urls.py is for and so on....

- Probably, most of you have even created tonnes of these projects with the previous instructions and are even wondering what next after this, :sunglasses::sunglasses::sunglasses:

> Before we go on just remember that this is a marathon and not a sprint, **_"Pasos cortos vision larga"_** which means **_Short Steps Long Vision_**. Thus, i would like to encourage you to continue creating at least 4 projects a day using the instructions from the previous class.

## Getting started in todays lesson

- In today's lesson we will start by configuring our **_settings.py_**, just adding some basic codes to it. So go to your settings.py and right at the top of the **_from pathlib import path_**, import the os simply by typing this line of code;
  ```
  import os
  ```
- The other line of code (in the settings.py) that i would like you to alter with is the **_ALLOWED_HOSTS=[]_** which usually helps us in indicating the hosting platform that we would like to host our project in, but to do away with that, i would like our project to be hosted by any hosting company thus your code should go as follows;

```
ALLOWED_HOSTS = ["*"] #We just added "*"
```

- The next landing point is in the **_TEMPLATES=[]_** list, In this section i would like you to add just the **_os.path.join(BASE_DIR,"templates")_** in the empty "DIRS":[--here--], Thus your code in that section should appear as follows;

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],# Changes were done here
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

- What the above lines of code does is that they helps in pointing our project to the templates folder, ie. where we will be storing our html files. I know some of you are already farmiliar with this mark-up language.

> We will be creating the templates folder soon.

- The next lines of code that i would like you to add to our project are with regards to the Static files. Static files are the css,js and images.

- So right below the STATIC_URL, i want you to include the following lines of code;

```
STATIC_URL = '/static/' #You can ommit this line since it is already in your project
STATICDIRS_FILES=[
os.path.join(BASE_DIR,"static")
]
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
STAIC_ROOT=os.path.join(BASE_DIR,"staticfiles")
```

- The above lines of code helps in pointing our settings to the folders where our images, css and js are stored.

- For the media, this is a folder that will be auto created,once we start uploading some images to our project. It's essence is that, it stores the images that we upload. For instance if you upload your profile picture, it will be stored in the media folder.

- The next point that i would like you to go is in the urls.py,

> Keep in mind that this is our root URL file, and each project will have its urls which will be pointing to this root URL.

- Currently, i know that in your urls.py there are some codes which are as follows (i deleted the comments above this lines of code)

```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # I hope you remember the url https://127.0.0.1:8000/admin
    # Now the /admin is right here, as we go on we will create our own urls and you ll learn what happens here
    ]
```

- Now i want you to add the missing lines of code on your urls.py from the code below.

```
from django.conf.urls.static import static #Add this line
from django.conf import settings #Add this Line
from django.contrib import admin
from django.urls import path, include #Add the word include

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add this URL
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Add this URL

```

- So the first line of code **_from django.conf.urls import static_** this basically enables us to import the statics urls from our settings.py
- The code **_from django.conf import settings_**, this line of code just enables us to import our settings.py in to our urls.py
- The word include will be useful to us, in that it well help us to include the urls and namespaces from the other applications

- The urlpattern **_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)_** provides our project with the route where our uploaded images are stored ie. the media folder (It will be auto created). The urlpattern **_urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)_** provides our root urls.py with the routes to the folder where we store our static files ie. css, images and js files.
- The next step is that i would like us to create the templates folder and the static folder in the base directory of our project, For this i would like you to look at our project layout and see where the templates and static folders are.
- In the static directory, i would also like you to create an additional 3 folders for css, js and images. Kindly, check my repository and see where our directories are located.

## Creating our first application

- In django we usually work with applications for instance in an e-commerce project we usually have the following applications, Accounts,Payments,Store, Invoicing,delivery and etc.
- In this section we will first begin our project by creating an application called the **_blog_**
- To create our first application type the following command in your terminal.

```
 python manage.py startapp blog
```

> Kindly note that the term blog is the name of our application.

- Once you have created our blog application you should see an additional folder in your project with the name blog
- If you expand that folder in your editor you might see the migrations folder, the dunder init script,(_init_.py),admin.py,apps.py,models.py,tests.py and the views.py.

- Now i want you to add your application to your project, thus just go to your projects settings.py, in the INSTALLED_APPS=[] section and the apps name there. Your code for that section should look as follows;

  ```
  # Application definition
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'blog', #Name of your application
      ]
  ```

- So the next step will be creating our urls.py for our blog application. The new urls.py should appear right inside the blog application.
  > Kindly check the structure of our blog application before creating your urls, (Just to ensure that we are on the same page.)
- The next step after you have created the urls.py, i want you to add the following lines of code to it.

```
from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
#Currently we dont have any urls
]

```

> To be continued...
> Happy Coding!

# Lesson III

# Recarp

- From our last class we were to learn how to create our first application. Probably, you might have even gone further to creating new projects with new applications. As i stated earlier, in django we usually work in applications.
- It is worth noting that for a complex project it is a great idea to split up the whole project into applications. In doing this it always helps you plan the work flow of your project, for instance if you are developing a chat application using the django channels, you might find out that spliting the whole project might bring rise to an accounts application and a chat application.
- Basically, this might tell you that you need to start working on the Accounts application before you can get your hands dirty with the chat app.
- Also, the reason as to why i recommend the use of application is because, in many work places developers usually work in tickets, where by you go and pick a ticket that holds a certain feature such that your feature might involve you or your team to work on a certain application lets even say a delivery application or a ticketing module which will fall in the ticketing ticketing application.

- To bring a recarp of how we created our Blog application, we typed this command in our terminal;

  ```
  python manage.py startapp <AppName (Blog)>
  ```

- After we created this application we went to our settings and placed the name of our applications in the ```

```
installed_apps=[
  'Blog',
  ]
```

- On finishing this we headed to our Blog application folder and created a **_urls.py_** file and inside this file we wrote this codes;

```
from django.urls import path
from Blog import views
app_name="Blog" #App name is the name of your application it might be Store,Delivery,Chat,Ticketing,....

urlpatterns=[

]
```

- After doing this headed straight into our root urls to tell it that we have other urls that are for another application in doing this, this is how the whole code block should look like,

  ```
  from django.conf.urls.static import static
  from django.conf import settings
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
  path('admin/', admin.site.urls),
  path("",include("blog.urls")) #This is the url that we added it is pointing to the blog.urls
  ]
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  ```

## Creating our first view

-Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application.

- The MVT Structure has the following three parts –

### Model

- Model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database (generally relational databases such as MySql, Postgres).

### View

-The View is the user interface — what you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files.

### Template

- A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. To check more, visit – Django Templates

![alt text](https://miro.medium.com/max/875/1*I_JVLw05Qqway-FQYq0ohg.png)
