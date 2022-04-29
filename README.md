# Rock the Boat Revival

This website has been created for users to buy and review a selection of RC Boats.

The live site can be found [here](https://rock-the-boat.herokuapp.com/)

![Responsive Mockup of site](media/mockup.png)

## Table of Contents

* [User Experience](#user-experience)

    * [User stories](#user-stories)
    * [Admin Stories](#admin-stories)

* [Planning](#planning)

* [Features](#features)

* [Future Features](#future-features)

* [Django apps and models](#django-apps-and-models)

* [Testing](#testing)

* [Languages and Programs Used](#languages-and-programs-used)

    * [Languages](#languages)

    * [Libraries and Frameworks](#libraries-and-frameworks)

    * [Development tools](#development-tools)

    * [Required modules](#required-modules)

* [Credits](#credits)

## User Experience

### User stories

As a user I would like to be able to...

* Products

    * View all products so that I can select some to purchase
    * View a paginated list of products so that I can view a select few at a time without having to scroll too much
    * View individual product details so that I can see the price, size, location and other details more clearly
* Profile

    * Register for an account so that I can have a personal account and view my profile
    * Login and logout easily so that I can access my personal account and logout to prevent others from accessing it
    * Have a personalised profile so that I can view my order history and reviews
* Bag

    * Keep track of all the products I am wanting to purchase so that I can continue shopping and purchase 
    * See the total price of my purchases so that I can keep track of how much I'm spending and avoid spending too much
* Currency

    * Change currency so that I understand the cost of my purchases in my local currency
* Filter & Sort
    * Filter by category so that I can easily find the product I want within the categories I want
    * Search for a product so that I can find a specific product to buy
    * Sort a list of products so that I can easily identify the best priced and categories that I want
* Reviews

    * View a list of reviews so that I can see other shoppers opinions
    * Leave a review for a game so that my opinion is heard and I can be involved in rating the game
    * Edit or delete my review in order to show my change of opinion or remove mistakes
* Discounts
    * Enter discount codes so that I can save money when buying products

### Shop Owner Stories

As a store owner I would like to be able to...

* Products

    * Add new products so that I can sell new products
    * Edit products so that I can adjust product details
    * Delete products so that I can remove products that are no longer being sold
    * Secure the site so that I can prevent unauthorised users from adding/editing/deleting products
* Reviews

    * Secure the reviews so that I can prevent users from being able to delete other users reviews
    * Only allow users to review products they've bought to prevent false reviews


## Planning

* Colour scheme

* Fonts

* Fimga

## Features

* Index

    * Logo

    * Search Bar

    * Nav

        * Currency
        * Profile
        * Bag
        * Categories
        * Sorting

    * Banner

    * Slogan and Image

    * Footer

* Products

    * Sorting

    * List of products

    * Pagination

    * Top of page arrow

* Product Detail

    * Full Product Info

    * Edit/Delete Buttons

    * Quantity and add to bag

    * Reviews

* Add/Edit product

    * Admin can add and edit products on these templates
    * Secured so that only an admin can access these pages

* Profile

    * Saved Delivery Information

    * Order History

    * Purchased Boats to review

    * Review History

* Bag

    * View all products currently in the fleet before purchasing

    * Can ajust quantity because buying

    * Can remove items no longer wanted

    * Can apply discount codes and see how much you've saved

    * Be reminded how close you are to the delivery threshold

* Checkout

    * Can fill in delivery information

    * Can save delivery information to profile

    * Checkout success page to view purchase and doubles as order history detail page

* Reviews

    * Create reviews with resposive stars to represent score

    * Can edit previous reviews

    * Edit and delete links hidden for reviews made by other users



## Future Features

* Delete modal

## Django Apps and Models

## Testing

### HTML

* Tested using the official [W3C Validator](https://validator.w3.org/)
* Removed Duplicate Ids
* Put li elements into a ul element

### CSS

* Tested using the official [Jigsaw W3C Validator](https://jigsaw.w3.org/css-validator/)

### JavaScript

* Tested using [JSHint JavaScript Validator](https://jshint.com/)

### Browsers

* Tested on Google Chrome, Internet Explorer, Microsoft Edge and even the Samsung Internet App on Mobile and Tablet

### Responsiveness

* Tested responsiveness on a Samsung A21 Phone, Samsung Galaxy Tablet and Desktop
* Tested with Google Chrome Development tools for different screen sizes

### Accessibility

* Tested using a web accessibility evaluation tool called [Wave](https://wave.webaim.org/)
* Semantic HTML is used
* Changed main background colour to #0054AD for a better contrast ratio
* Added aria-labels and alt texts

## Languages and Programs Used

### Languages

* HTML5 for site structure
* CSS3 for styling
* JavaScript for star ratings and message timeouts
* Python 3.0 for Django

### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)'s model view template structure was used to create apps and run them
* [Boostrap4](https://getbootstrap.com/docs/4.5/getting-started/introduction/) framework used for responsive styling and templates

### Development tools
* Git for version control
* VS Code as IDE (integrated development environment)
* PIP to install packages
* Postgresql for the database to create content and manage data
* Heroku used for deployment
* Stripe used for handling payments and webhooks
* AWS used for cloud hosting for static and media files

### Required modules

All modules required are located in the [requirements.txt](requirements.txt) file.

## Deployment

### Heroku

Create Heroku App

    1. Create Heroku account and login
    2. Click new then create new app
    3. Name app a unique name
    4. Select your region most appropriate for you

Link Gitpod workspace to Heroku App \
(Heroku have removed the functionality to deploy Github apps through the Heroku Dashboard)

    1. In the gitpod terminal run the commad 'heroku login -i'
    2. Login with your email and password
    3. Run the command 'heroku git:remote -a your_app_name_here', replacing 'your_app_name_here' with your app name
    4. Automatic deployments are no longer available at time of writing so after each 'git push' you need to also run 'git push heroku main' to manually deploy

Add Postgresql Database

    1. Click onto the Resources Tab
    2. Under Add ons search for Heroku Postgres
    3. Select Hobby Dev - Free plan
    4. Submit order form

Set Environment Variables

    1. Click onto the Settings tab
    2. Click reveal Config Vars.
    3. Add the variables below
    4. Set them as follows

|Key | Value|
--- | ---|
|AWS_ACCESS_KEY_ID | (AWS Access key)|
|AWS_SECRET_ACCESS_KEY | (AWS Secret Access key)|
|DATABASE_URL | (Postgresql Database url)|
|EMAIL_HOST_PASS | (Email Host password)|
|EMAIL_HOST_USER | (Email Address)|
|SECRET_KEY | (Secret Key value)|
|STRIPE_PUBLIC_KEY | (Stripe Public Key value)|
|STRIPE_SECRET_KEY | (Stripe Secret Key value)|
|STRIPE_WH_SECRET | (Stripe WH Key value)|
|USE_AWS | True|

### AWS Configuration

Amazon AWS S3 Bucket

    1. Creat an AWS account and login
    2. Go to Services then S3
    3. Create an S3 bucket
    4. Untick 'Block all public access' to make is publically accessable
    5. Create and apply bucket policy, Cross-origin resource sharing (CORS), Access Control List (ACL)
    6. Go to services then IAM
    7. Go to policies and create bucket policy
    8. Add a JSON file with your policy arn in the Resource
    9. Creat User Group and User to manage the S3 bucket
    10. Upload media files into the S3 bucket through the AWS console
    11. Copy the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY values to the Config Vars in Heroku.

## Credits

* RC Boat images and data was used from [Zeptronics](https://www.zeptotronics.net/)
* JavaScript code for star ratings is based on code from [Brad Traversy](https://codepen.io/bradtraversy/pen/GQLRZv)
* Pagination styling based on [Codemy.com](https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw)'s video on Pagination
* [Bootstrap cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/) helped by listing boostrap classes in an easy to find manner
* [Boostrap Templates and Examples](https://getbootstrap.com/docs/5.1/examples/) used as a basis for some features
* [Font Awesome](https://fontawesome.com/) used for the stars
* [W3Schools](https://www.w3schools.com/) used for reference in using coding [languages](#languages)
* [Stack Overflow](https://stackoverflow.com/) was used to find solution to some coding issues
* The [Code Institute](https://codeinstitute.net/) study material was used