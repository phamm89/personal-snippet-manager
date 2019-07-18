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
Note: Your name for the project replaces project_name.  
**Important**: Remember to insert a "space" and a "." after project_name to avoid creating an extra directory.
- Create a .gitignore file by doing the following:
```bash
touch .gitignore
```  
```bash
open .gitignore
```  
- Copy content from [https://gitignore.io/api/python,visualstudiocode](https://gitignore.io/api/python,visualstudiocode) and paste into .gitignore file
