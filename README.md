[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ShoabSaadat/flasktemplatemaker) 

# Welcome to the Flask Template Maker

### Author: Shoaib Saadat


1. As per directory structure, you can run app.py to setup a new customized flask app for yourself with user-management system and database already setup.

2. You can also go to exe folder and click runEXE.bat to run the portable server if you don't have python installed. There is also a zipped version of the same app in this folder.

3. Once you have created your app folder, run the following commands from the app directory:

```
Migrate---------------------------------------
set FLASK_APP=app.py
flask db init
flask db migrate -m "First Migrate Commit After App Creation"
flask db upgrade
----------------------------------------------
```

4. If you wanted to upload the app to heroku, change isLive to True in __init__.py file located in your APP NAME/appname folder. After that run the following commands:

```
Heroku Login----------------------------------
heroku login (login to your heroku account)
----------------------------------------------

Setting Heroku Remote for new push------------
heroku git:remote -a YOURAPPNAME
----------------------------------------------

Pushto Heroku-----------------------------
git add .
git commit -am "First Git Commit to Heroku"
git push heroku master
----------------------------------------------
```

5. To clone the app from heroku, you can use the following command:

```
Heroku Download-------------------------------
heroku git:clone -a clinicassist
----------------------------------------------
```

6. You can bash into your heroku using:

```
Heroku GitBash--------------------------------
heroku run bash
----------------------------------------------
```

7. You can push to your git hub account using:

```
Push to My Git-----------------------------
git add .
git commit -am "First Git Commit"
git remote add origin https://github.com/YOURUSERNAME/YOURAPPNAME.git
git remote -v
git push origin master
----------------------------------------------
```

8. If you cannot run python server locally, you can try:

```
For Local Python Running----------------------
set CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1
----------------------------------------------
```

9. You can build a new executable using the following commands:
```
For Building an Executable--------------------
pyinstaller --onedir --add-data tempraw;tempraw --icon=.\tempraw\myapp\static\pyicon.ico app.py
----------------------------------------------
```
