# Django-Instagram-Clone
A Django application that allows users to upload, like and comment on other peoples images. Images have captions and users have profiles where you can see all their images Images are hosted on Cloudinary.

![](https://github.com/steve-njuguna-k/Django-Instagram-Clone/blob/master/Screenshots/1.PNG)
![](https://github.com/steve-njuguna-k/Django-Instagram-Clone/blob/master/Screenshots/2.PNG)
![](https://github.com/steve-njuguna-k/Django-Instagram-Clone/blob/master/Screenshots/3.PNG)
![](https://github.com/steve-njuguna-k/Django-Instagram-Clone/blob/master/Screenshots/4.PNG)

## Requirements
The user can perform the following functions:

- A user can Sign in to the application to start using it.
- A user can upload pictures to the application.
- A user can see their profile with all their pictures.
- A user can follow other users and see their pictures on my timeline.
- A user can like a picture and leave a comment on it.
- A user can search for other usersnames on the application.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 3.9.6

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/steve-njuguna-k/Django-Instagram-Clone.git
```
2. cd into Django-Instagram-Clone
```
cd Django-Instagram-Clone
```
3. create a virtual env
```
py -m venv env
```
4. activate env
```
env\scripts\activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
py manage.py makemigrations
```
7. Migrate DB
```
py manage.py migrate
```
8. Run Application
```
py manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please find me on [LinkedIn](https://www.linkedin.com/in/steve-njuguna-aa426096/)

© 2022 Steve Njuguna

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
