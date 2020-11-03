# My Favorite Recipes

Finally, a place to keep all your favorite recipes without all the added clutter and features you never use. No calorie counters, no grocery lists -- just your recipes, organized by category.

## Features

Find your recipes quickly with this simple Django application. You choose which categories you want displayed, making it easier to organize your recipes the way YOU want. 

<img width="1197" alt="Screen Shot 2020-10-03 at 2 07 42 PM" src="https://user-images.githubusercontent.com/65363804/97948014-25e71f80-1d5d-11eb-95a4-8138b104c0c3.png">

Recipes can include a summary, the recipe itself, and an optional photo. Should you choose to not upload a photo, a default picture is displayed instead.

When logged in as an adminstrator, you can add new users, add new recipes and categories, edit recipes and delete both categories and recipes. A warning -- when you delete a category, it also deletes all recipes associated with that category!

It is possible to lock down the site so the only users who can see the recipes are the ones specifically added by the administrator. As the code stands now, the site remains open for browsing categories and viewing recipes.

## Responsive design

The application looks equally good on mobile devices as it does on desktops. It is easy to read recipes on a phone, making it convenient to use in the kitchen, or on the go.

<img width="257" alt="Screen Shot 2020-10-05 at 1 58 38 AM" src="https://user-images.githubusercontent.com/65363804/97948614-1963c680-1d5f-11eb-8d90-f5f63ee55a89.png">

## Work in progress

I do have some features I'd like to add in the future. In particular, a search option, as well as the ability to add a recipe to more than one category. I'd love for potato salad to be found under both "salad" and "potatoes." 

## See live

If you would like to see the application in use, please visit my deployed version, which I use to keep my own personal recipes: http://www.myrecipesapp.com/

## Requirements

To use, fork and clone onto your local machine. To install dependencies and launch your virtual environment, run: --poetry install -poetry shell. From there you can create your own administrator account and begin adding recipes!

The application is already prepped for deployment; however, you will need to add further dependencies should you wish to deploy.

To run on a local server, you will need to turn on "debug" and make sure you have the following dependencies installed:

Python, 3.8

Django, 3.1

Django-Cleanup, 5.0.0

Pillow, 7.2.0

Django-rotate-secret-key, 0.3

Django-bootstrap-modal-forms, 2.0.0

