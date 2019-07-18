# Personal Code Snippet Manager
In Momentum Learning, my group is working on developing a Code Snippet Manager web application. This personal code snippet manager is being developed in order for me to better understand the setup of a web application involving Django and JavaScript.

## Creating a Github Repository
- On Github, click "New" to create a repository
- Name the repository and click "Create Repository"
- On created repository, click "Clone or Download"
- Copy the repository URL 
- Create a directory in your terminal
- Clone your repository as follows:
```bash
git clone https://github.com/<username>/<repo-name>.git
```

## Setting up a Django Development Environment
- ```cd``` into your repository directory
- Run 
```bash
pipenv --three
```
- Run the following to install Django:
```bash
pipenv install django
```
- Run the following to enter your virtual environment:
```bash
pipenv shell
```

## Start Django Project
- Run 
```bash
django-admin startproject <project_name> .
```
**Note:** Your name for the project replaces project_name.  
**Important**: Remember to insert a "space" and a "." after project_name to avoid creating an extra directory.
- Create a .gitignore file by doing the following:
```bash
touch .gitignore
```  
```bash
open .gitignore
```  
- Copy content from [https://gitignore.io/api/python,visualstudiocode](https://gitignore.io/api/python,visualstudiocode) and paste into .gitignore file
- Create app for project:
```bash
python3 manage.py startapp <app_name>
```  
**Note:** Your name for the app replaces app_name. A common app_name is "core".

## Register the app
- Open **settings.py** and find ```INSTALLED_APPS```
- Add <app_name> to the bottom as follows:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name', 
]
``` 

## Working in group projects
If you are working in a group project, you can create a branch from the origin/master branch to make a contribution to the project as follows:
```bash
git checkout -b <branch_name>
```  
**Note:** Your name for the branch replaces branch_name.  

Once you have finished your branch, you can push your branch to the repository as follows:
```bash
git push origin <branch_name>
```  

Create a pull request to merge the code from your branch with the master branch. After the merge, you can pull the updated master branch into your local master branch as follows:
```bash
git checkout master
git fetch upstream
git merge upstream/master
```  

To delete your branch, you can run the following:
```bash
git branch -d <branch_name>
```  

## Installing Debug Toolbar
Debug Toolbar is a helpful tool for debugging. Follow the directions at the following site:
[https://django-debug-toolbar.readthedocs.io/en/latest/installation.html](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

## NPM and Django
1. Create a ```package.json``` file with contents ```{"private": true}```
2. Make sure ```node_modules/``` is in your ```.gitignore``` file.
3. Install ```browserify``` and ```watchify```: ```npm install browserify watchify```
4. Try using ```browserify``` on your current JS: ```npx browserify -o <output_file.js> <input_file.js>```
5. Add a ```scripts``` section to ```package.json```:
*content_copy*
```bash
{
  "scripts": {
    "start": "npm-run-all -p -l django watch:js",
    "django": "python manage.py runserver",
    "start": "watchify -v -o <output_file.js> <input_file.js>",
    "compile": "browserify -o <output_file.js> <input_file.js>",
  }
}
```  
6. Use ```npm run start``` to start watching your input file for changes.
