# Foot Galaxy

Telephile is an E-commerce store for a multinational business that sells classic and modern football jerseys to fans and collectors around the world. Shoppers can sign up and create an account, browse the store's jerseys and make purchases through the checkout. Shoppers gain a user profile when signing up where they can view past orders and save their personal info, the site also lets them review the business and save items to their wishlist. 

You can find the live site [Here](https://foot-galaxy-e4d24e6240cb.herokuapp.com/).

<br>
Please do not input your own credit card details. While purchasing a product please enter the following digits to make use of the checkout system. 
<br>
Card number: 4242 4242 4242 4242. Expiry: 42/42. CVC: 424. PostCode: 42424. 

####

![Home Page Desktop](static/images/homeScreenshot.png)
&nbsp;
![Home Page Mobile](static/images/mobile%20screenshot.png)
&nbsp;

# Purpose
I built this website as my fifth and final project for the code institutes full stack development and e-commerce applications course. 
I built this website from scratch using the Django framework and the knowledge I gained while studying at the code institute where I have learned the basics of Python, HTML, Javascript and CSS.

# Target audience
* Football Fans
* Shirt Collectors 
* Fashion lovers 

# User Experience 

<br>

## Site Aims

* Provide football lovers with a store to purchase classic football shirts.
* Get as many users signed up as possible. 
* Create a good relationship with customers and keep them returning. 

# Design 

## Agile Methodology 
The agile methodology was implemented in the design of this project. The project was planned on github using the project board feature.
* You can find the project board [Here](https://github.com/users/Mcdaid101/projects/3).
* The project board consists of three sections: 
* 1. Todo 
* 2. In progress 
* 3. Done.
* Each user story was drawn up in the issues section of github and passed on to the kanban where once added to the project board, it was placed in the todo section. Once a user story was undertaken it was then moved into "in progress"section and when finally implemented and complete moved into the third. 
<br>

## User stories
### First iteration
* 1. As a shopper I want to view products the site is offering.
* 2. As a shopper I want to be able to view the info on a product such as its name, price and size.
* 3. As a shopper I want to be able to apply different filters to products to filter and view them by price, in alphabetical order etc.
* 4. As the site admin I want to be able to edit pricing, images and description.
* 5. As the site admin I want to be able to add new products for sale and delete products if they are no longer being sold.
### Second iteration
* 6. As a shopper I want to be able to view a FAQ section for any frequently asked questions.
* 7. As a shopper I want to be able to add products to my basket and view them before proceeding to the checkout.
* 8. As a shopper I want to be able to remove items from my basket
* 9. As a shopper I want to view my order details before I checkout.
* 10. As a shopper I want to be able to enter payment info quickly and easily and save it for the future.
* 11. As the site admin I want to be able to view orders made by customers to ship them as soon as possible.
### Third iteration
* * 12.  As a shopper I want to be able to create an account to be able to interact with the site and feel a part of it.
* 13. As a shopper I want to be able to log in and out of my account on the site.
* 14. As a shopper I want to be able to view my past orders on my profile
* 15. As a shopper I want to be able to save items to my account to show I like them and would maybe like to purchase them in the future.
* 16. As a shopper I want to receive a confirmation email when signing up.
### Fourth Iteration
* 17. As a site owner I want to be able to add, update and delete products from the main site
* 18. As a shopper I want to know the location of the site’s store so I can shop there in person.
* 19. As a shopper I want to be able to leave a review on the site’s services.
* 20. As a shopper I want to be able to recover my password if I have forgotten it.
* 21. As a shopper I want to receive regular news on the site and new products/plans via email.
* 22. As the site admin I want to create a mailing list for subscribers to the site’s newsletters.
* 23. As a shopper I want to be able to access the site’s social media to keep up to date with new plans and products.

### Future features 
* Order confirmation email.
* The ability for the site admin to manage review via the website ui.
* A football training plan subscription section giving users the chance to subscribe and unsubscribe
<br>

## Wireframes and Schema

<details><summary>Desktop Wireframes</summary>
<p>

![Home page](static/images/home%20wireframe.png)

![Products page](static/images/products%20wireframe.png)

![Profile page](static/images/profile%20wireframe%20.png)

![Product Detail page](static/images/product%20detail%20wireframe.png)

![Bag](static/images/bag%20wireframe.png)

![Checkout](static/images/checkout%20wireframe.png)

</p>
</details>

<details><summary>Database Schema</summary>
<p>

![Database](static/images/databaseschema.png)

</p>
</details>

## Design choices 
<br>

### Colour scheme


### Font 


## Features
<br>

### Nav bar
To navigate the site Users use the nav bar at the top of each page. What appears on the nav bar depends on if the user is authenticated or not. (if the user is signed up)
* Signed out 
![Nav bar signed out]()
* Signed in
![Nav bar signed in]()

### Footer
Similar to the nav bar the footer appears on each page and has a sticky effect. The footer contains links to the site's social media pages and has a light/dark mode button so users can choose which way to view the site. 
![Footer]()





# Technology Used 
<br>

## Languages 
* Python
* HTML
* CSS 
* Javascript
* Jquery
* Tailwind Css

<br>

## Tools and Frameworks
* Git 
* Github 
* Vs Code IDE in browser
* Django
* Postgres
* Techsini Multi Device Mockup Generator used in this readme to display an image of the website on different devices 
* Heroku -  Hosts live site
* Allauth - login and registration
* Tailwind CSS used to style and structure site 
* ElephantSQL - HOsts database
* Bootstrap 4 - Used for site structure and making the site responsive
* Basimiq - Created wireframes 
* Whitenoise - Hosts and displays static files and images for the site
* Amazon Web Services host static and media files
* Crispy forms - Improve the sites forms
* Crispy tailwind - styled the sites forms 
* Django storages - helped with file storages 
* Django browser reload - automatic browser reloads in development 
* Stripe API
* Pillow

# Bugs 


<br>


<br>


<br>

# Testing and validation

<br>

I have manually tested this project by doing the following:
* Passed the pages through the W3C HTML and CSS validators
* Passed the project through a pep8 linter and the Code Institute python checker and confirmed there is no problems.
* Tested in my gitpod terminal and the Heroku terminal.
* Tested each user story to make sure each one passes. 

W3C validations
![HTML]()
![CSS]()

Pep8
* No errors were returned from the code institute's python Linter or from extendsclass.com/pythontester.
![Python]()

Lighthouse testing
* At first my test results came up quite poor but after switching to an incognito window on chrome and downsizing the main hero image on the home page the site got a high score as seen in the images below. All pages got a similar result.
 ![Test]()

<br>

## Manual Testing

## First time stories 
* As a first time user: I want to be able to post a review on Telephile <br>
Testing done to make sure that users can post reviews.
<details><summary>First time user 1</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Add your own post| Once signed up and logged in, users can navigate to the add a review page and add a post. The post is successful ifthey receive an alert telling them so | The user receives an alert notifying them that their post is pending  | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to sign up and create an account <br>
 Testing done to ensure that users can sign up to the website.
<details><summary>First time user 2</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Create an account feature | Users can navigate to the sign up page and create an account  | Once the user signs up their account is created and they can log in and out as they please and make use of the rest of the site's features  | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to leave comments on other's posts <br>
  Testing done to ensure that users can comment on posts
<details><summary>First time user 3</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Comments | Users can comment underneath other users posts | Comments appear once they are posted and approved by the admin | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to be able to view how many likes and comments are on a post  <br>
 Testing done to ensure that the amount of likes and comments on a post appear underneath the post
<details><summary>First time user 4</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|Amount of likes and comments | Navigate any posts page and find out how many users commented and liked the post underneath the image beside the author  | The amount of likes and comments appear underneath the post | Works as expected |
</p>
</details>
<br>
<br>

* As a first time user: I want to see what posts I have made <br>
 Testing done to ensure that the your reviews section shows the user's reviews.
<details><summary>First time user 5</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Your reviews section| navigate to the your reviews section to view the posts you have made | Your reviews appear in the your reviews section  | Works as expected |
</p>
</details>
<br>
<br>

## Returning stories

* As a returning user: I want to be able to log in without putting my details again <br>
Testing done to ensure each user can have their details remembered for login. 
<details><summary>Returning user 1</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Remember login details | Navigate to login page and click remmeber details | The user's login details will be remembered for next time | Works as expected |
</p>
</details>
<br>
<br>

* As a returning user: I want to be able to like posts I enjoy and have the option of unliking them if I want <br>
Testing done to ensure that users can like and unlike posts
<details><summary>Returning user 2</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Likes | Clicking the heart under a post liked the post and clicking it again unlikes it | The post is liked  | Works as expected |
</p>
</details>
<br>
<br>

## Owner stories 
* As the site owner: I want to be able to moderate what is posted on the site  <br>
Testing done to ensure that the admin can approve and disapprove of what is posted on the site
<details><summary>Site owner 1</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Approve of and disapprove of posts and comments | Admin can approve and disapprove of users posts and comments, they will not get posted until they are approved| Posts and comments do not appear until approved | Works as expected |
</p>
</details>
<br>
<br>

* As the site owner: I want to be able to choose the category each post belongs in  <br>
Testing done to ensure that posts can be placed in a specific category
<details><summary>Site owner 2</summary>
<p>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Categorizing | Admin can choose which category a post belongs to | The category the admin chooses the post to be in, is which one it ends up in the category page  | Works as expected |
</p>
</details>
<br>
<br>


# Deployment 

## Creating this project
This project was created by navigating to the Code Institute's Gitpod student template and clicking the 'use this template' button. I then inputted the repository name "Foot Galaxy" and included all branches. With the repository now created, I used the browser version of Vs Code to create the project. 
<br>

I used the following commands throughout this project:
* Git add . - This added my file to the staging area to be committed
* Git commit -m - This command committed any changes to the local repository along with a message
* Git push - pushed my changes to the github repository and to Heroku 
* git reset --hard HEAD^ - This removed my last commit 
* python3 manage.py runserver - This ran my code in the terminal
* python3 manage.py makemigrations - This made my migrations
* python3 manage.py migrate - This migrated my changes to my databases

## Heroku
This website is deployed on Heroku

## Steps for deployment 
* Fork or clone this repository
* Linked the heroku app to the repository via github
* Clicked automatic deploys so each git push would automatically go to the heroku app
* This was ideal for testing so I could see what the site looked like on the Heroku terminal with each git push

<p> 1. Create Django project and app </p>

* Install django using the command pip3 install 'django<4' gunicorn
* Then install the database libraries dj_database_url and psycopg2, using pip3 install dj_database_url psycopg2
* Then create the requirements.txt file using the command pip3 freeze --local > requirements.txt
* Then created my Django project with the command django-admin startproject project_name .
* I created the Django app with the command python3 manage.py startapp app_name
* I used the commands python3 manage.py makemigrations and python3 manage.py migrate to migrate my changes.
* To test and run the project I used python3 manage.py runserver.

<p> 2. Create Heroku app </p>

* I opened the heroku website and logged into my account
* I created a new app with the project name
* Select region as Europe
* Open the Resources section and select Heroku Postgres
* Open the Settings section and select Config VARS, then add the keys needed to start development DATABASE_URL/SECRET_KEY/CLOUDINARY_URL, with Config VARS you add: PORT: 8000 + DISABLE_COLLECTSTATIC: 1;

<p> 3. Set up Django settings.py and necessary folders/files </p>

* Set up to connect the environment variables
         from pathlib import Path
         import os
         import dj_database_url
         from django.contrib.messages import constants as messages
         if os.path.isfile('env.py'):
         import env
         
* Inside INSTALLED_APPS I added the necessary apps

* For the database I replaced it with the following code

        DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
        
* For the static files I replaced it with the following code to conect to Cloudinary

      STATIC_URL = '/static/'
      STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

      MEDIA_URL = '/media/'
      DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
      
* Create a Procfile and add the following text

web: gunicorn autoclassic.wsgi

<h3> 4. Final deployment. </h3>

* In settings.py set the DEBUG = False;
* In Heroku I went back to Settings > Config VARS and removed the DISABLE_COLLECTSTATIC var;
* In Heroku I navigated to the Deploy section;
* I clicked to connect to GitHub and searched for my repository for this project;
* I clicked on manual deploy to build the App;
* When finished, I clicked the View button, which redirected me to the live site.

<br> 

# Credits
* W3schools provided me with the code for my scroll to top of page function and my dark/light mode button. 

## Media 
* Site's posts feature image if unprovided: [here](https://www.pexels.com/photo/retro-tv-set-on-concrete-surface-5721869/)
* Posts feature image if unprovided: [here](https://images.pexels.com/photos/10599961/pexels-photo-10599961.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)
* Home page hero is from scontent on facebook image is [here](https://scontent-lcy1-1.xx.fbcdn.net/v/t39.30808-6/311134067_416071014039021_806491811075822809_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=e3f864&_nc_ohc=S21fvKd8L4YAX_OWoXn&_nc_ht=scontent-lcy1-1.xx&oh=00_AfA04p9E2-rNTd0Mg8B7RBirtWGhH-zMiavymSuL7Ks3zA&oe=646BFA28)

## Acknowledgements 
* I would like to thank my mentor Ronan Mc Clelland for his help and guidance while I built this project.
* I would like to thank my family for their love and support.
* And finally my girlfriend for her advice on my site's style. 