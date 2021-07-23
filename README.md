# Mictec_Django
## Set-up
   - Ensure that you have git installed into your machine, The link for downloading git is [Git Download](https://git-scm.com/download/win)
   
   - If you dont have a github account, Kindly create one. Open this link in a new tab and create your account [GitHub Signup](https://github.com/join)
   
   - You can learn the basics of git from this tutorial just one hour [free code camp git tutorial](https://www.youtube.com/watch?v=RGOj5yH7evk&t=7s)
 
   - The next thing is to ensure that you have Python and Anaconda into your machine, You can download Python via     [Python Download](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe) and then do the installations. For anaconda terminal the download link is [Anaconda Download](https://www.anaconda.com/download/#windows), Download it and do the installations.
   
   - The next step is that we will need and editor where we will write our codes, You can choose one of this sublime text, Atom and VS Code. The link for downloading sublime text is [Sublime Text Download](https://download.sublimetext.com/Sublime%20Text%20Build%203211%20x64%20Setup.exe), For Atom is [Atom](https://atom.io/download/windows_x64) and for VS Code is [VS Code Download](https://code.visualstudio.com/download)
   
   - Now we are good to get our hands dirty with the frame work for perfectionist:+1:.

## Getting Started
   - After Doing all the above installations, Go to your windows search bar and search for anaconda and open it. Also you can confirm if you have python installed by typing **python --version** on the terminal. 
   
   - The next step is to download the virtual environment It is always important to create an environment where you will store all the dependencies for required by your project. There are two packages that i usually use for this case; virtualenv wrapper and the virtualenv. To do the installation you will type (on your anaconda terminal) ***pip install virtualenv*** to install the virtual env and  ***pip install virtualenvwrapper-win*** for windows and ***pip install virtualenvwrapper*** on linux.
 
   - After the installation has taken place, lets create a folder where we will store our projects, type ***mkdir Mictec*** the cd into that directory by typing ***cd Mictec*** on your terminal.
 
   > NB: You ll need to pay attention to the spellings of the folder you have created and the folder you want to cd to.
   
   - The next step let us create a folder where we will house our project and the environment we will create. To do this we ll do as we have done above ***mkdir BlogEnv*** and then we ll cd into that folder by doing ***cd BlogEnv***. 
   > Now you should be an expert in that.
   - Now lets create our environment by typing the following command into the terminal ***python -m venv BlogEnv*** where the BlogEnv is the name of our environment. To activate our environment we will type ***BlogEnv/Scripts/activate*** into the terminal. You should see the name of BlogEnv behind the word Base on your terminal.
   
   - if you are using atom you can open your project folder on the editor by typing ***atom .*** and for VS Code you can type **code .** for sublime you can type ***subl .***. If any of that does not work, "Physically go to your local disk" and open the folder Users, then the folder named User or has your name, Scroll down and open the first folder that you created i.e The **Mictec folder***, Now you should see the folder named **BlogEnv**, Slowly drag :shipit: and drop it to your prefered editor.

   - The next step is to now to install django, Simply type ***pip install django*** in your terminal.

## Creating our Django Project
   - After we have installed Django, starting the project should now be a childs play. To start the project simply type ***django-admin startproject src*** Where src is the name of the project that you would want to create, It can be an E-Commerce Project, a blog, a todolist, space-z, etc.
   
   > On your editor you should see that some additional files have been added
   
   - I want you to cd into the project that you have created above for my case i will ***cd src***
   
   - To run our project, type ***python manage.py runserver*** on your terminal you should see something amazing. Copy paste the address that you see [Local Host](http://127.0.0.1:8000/) http://127.0.0.1:8000/ and paste it on your browser's url, You should see a congratulations message telling you that you have run django successfully.
   
   > Now that is not magic, it's your talent and your hard work
  
   - Now get back to your terminal and you should see an error message that reads;
   > You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s)
  
   - To do away with this error message just type ***python manage.py migrate*** and then rerun your local server by using our usual command ***python manage.py runserver***

   - You can further access the admin panel by adding /admin to your url it should be something like ***http://127.0.0.1:8000/admin***. You should now be able to see a django admin login page. But you need to create a user that can be able to login. To do this type ***python manage.py createsuperuser*** it should prompt you to input a username, email and password and confirmation password.
   
   - After you have done this rerun the server with the same command ***python manage.py runserver*** go to your admin url ***http://127.0.0.1:8000*** in your browser.
   
   - You should now be able to login using the credentials that you have used in registering the new superuser on the terminal.
   
   - After you have logged in you will be meet a nice user panel, with the group(s) and Users tabs on the left side of the admin panel. Now i want you to enjoy yourself by creating new users and new groups.
   
   > Now Repeat the whole process for how many times? Let's just say 1000 times and we ll be looking at the next [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean). In the next class we will create our first application and do something more constractive. Well, I hope you enjoyed that.
   
   > Happy Coding!!!
   
  
  
 
