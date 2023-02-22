# A-Z_Designers

### [A-Z_Designers](https://a-z-designers.herokuapp.com/) is my final milestone project at [Code Institute] and it is a full stack E-Commerce website developed to be a website for an online clothing store. This website allows users to purchase clothing that is in stock as Anonymous users and even create an account which allows them to save shipping/billing details and previous orders. This project demonstrates my learning and understanding throughout the course of full stack website development.

### I believe I produced a website that is very adaptable and can be repurposed for many ecommerce applications, this includes subscriptions and transactional services. There are numerous features which I would like to have added for submission of this project, however, due to limited time this was not possible for the moment.

If you wish to test account functionality, demo accounts have been provided below. Please note that not all error pages have been created and therefore on the occasional error the base django template will show up.

![responsive](https://user-images.githubusercontent.com/97538312/203823455-a1f9d1d8-3687-4b54-a6a1-2b5d1a8e8026.jpg)

To test website functionality, please find account details below.

| Username | Password | Desription |
| ----- | -------- | ---------- |
| hodedar | 11@@11@@ | Customer account created with temp-mail and consists of multiple orders and reviews. (testing email confirmation was successful) |
| AZ_Designer_super | @@11@@11 | Admin account with create and update permissions to all custom models, these are accessible in the access admin area and product management on the website account section. |
  
##  **Purpose**
  - The purpose of this E-Commerce website is to connect users with a retail business in which the user can purchase designer clothing online efficiently from the comfort of their home.

## Agile Methodology
  - Use of Github Issues and User Stories is involved as part of Agile methodology
  ![user_stories](https://user-images.githubusercontent.com/97538312/204099265-eb4c50b9-ed7d-4d70-b27c-5a2d807fd17e.jpg)


## User Stories

### Customer
  - As a shopper I can see the products for sale so that I can select items to buy
  - As a Shopper I can read product description so that I know more about the product being sold
  - As a shopper I can quickly navigate to my desired product so that my shopping experience is much faster and smoother.
  - As a shopper I can see how many products I have added to my bag and price total so that I know exactly how much I have selected/selected for.
  - As a site user I can register quickly so that I can save my details to make shopping here again a faster experience
  - As a site user I can login so that I can access my personal account information and history
  - As a site user I can recover my password so that I can still login to my account if I forget my login credentials
  - As a site user I can receive an email confirmation so that I know for sure my account has been registered to the website
  - As a shopper I can sort for products by various stats so that I can quickly and efficiently find what I am looking for
  - As a shopper I can search for a product so that I can immediately see if the site offers that product
  - As a shopper I can select the size and quantity so that I get the correctly sized article of clothing and more than one if I desire
  - As a site user I can check the company's social media so that I can further verify their credibility and follow them
  - As a site user I can contact the company so that any questions I have can be addressed
  - As a user I would like to be able to select the quantity of a specific product without having to click on it multiple times, so that my shopping experience is         smoother and faster.
  - As a user I want to be able to enter my payment details securely without the fear of them getting leaked and use trusted and well known payment methods.
  - As a user I want to receive confirmation of my order to know everything went through and I can expect my order to be on the way.
  - As a user I am not entirely comfortable giving my information to register and would like the option to shop without creating an account.
  
### Site Owner
  - As a website owner I want users to have an enjoyable UX and therefore to adapt to errors happening include a not so boring 404 error page.
  - As a site owner I want to add new products and have them automatically display on the website, so that customers can purchase them.
  - As a site owner I want to be able to edit product details, for example, price and stock so that products can be updated.
  - As a site owner I want to be able to delete products from display, so that if I have stock issues I can prevent customers from viewing it.
  - As a site owner I want to be able to link customer orders to the Stripe PaymentIntent dashboard, so that I can verify custom payment details, if I need to.
  - As a site owner I want to be able to manage customer reviews, so that any inappropriate content can be removed if necessary.


## **Features**

- **User Features** 
  - Fully functioning front end website for users to get information on about the lessons
  - Ability to register an account and login/logout.
  - Ability for users to place bookings for their desired class
  - Ability for users to change or cancel their bookings
  - The layout of certain sections changes, dpending if a user is logged in or not.
  - Fully responsive design using bootstrap and media queries for user on all devices.

- **Admin Features**
  - As an admin only I have the ability to login to the admin panel
  - Admin is able to see all placed reservations and control them
  - Admin is able to see all customer input details
  - Admin can see who placed the reservations by their login details
  - Most importantly the admin can update or delete all reservations

- **Site Features**
  - The site is developed to be a single scroll page except for the register and login forms
  - The main section loads up with an image displaying the theme of the website (golf) and the title clearly visible to users
  - The navbar is compact into a hamburger menu icon and is transparent if the page is at the complete top
  - Once the user scrolls for better user experience, the navbar is set to always be visible and a background colour appears using JavaScript
  - For extra functionality there is a button which if clicked simply scrolls down to the About Us section
  - Clicking on sections in the navbar scrolls the page down to that desired section
  - Clicking on the heading will also scroll the page back up to the top
  
## Main section
![main-screenshot](https://user-images.githubusercontent.com/97538312/201192933-98a6b956-1bc9-43e9-84d8-8ba22933ffd2.jpg)
  - The landing page is designed to immediately inform a user that they are on a golf website
  - Provide an easy UI and UX with it's easy to read design
  - The button in the middle takes the user down to the next section

## Navbar to not logged in users 
  - Log in and register options are available
  - Manage bookings does not show up 
  - Log out option is not shown
  
![nav_not_logged_in](https://user-images.githubusercontent.com/97538312/204134958-fe247587-a0fe-441e-afae-74adcf072acd.jpg)

## Navbar to logged in users
  - Option to make a booking
  - Option to manage bookings
  - Login and Register are now hidden
  - Logout option is visible
  
![logged_in_nav](https://user-images.githubusercontent.com/97538312/204134974-443be7a9-cb17-4560-91aa-b48721dd5ceb.jpg)

## About Us
![about-us](https://user-images.githubusercontent.com/97538312/204131322-e8051a0d-a255-43f4-950d-f753532350f2.jpg)
  - In this section a user is informed about the mission of the ImproveYourGolf company


- **Classes**
  - The classes section is designed to look different for authenticated users and those who are not logged in
  - If a user is not logged in then a message at the bottom of the class description appears to inform a user they must first login
  - When a user logs in this message disappears and the 'Book Now' button appears
  - The responsive features set the columns to align from 3 across to a 2,1 layout and then in a row formation for mobile devices
  - Each class has a different image to indicate the type of lesson to expect

## Classes when not logged in 
![classes_notauth](https://user-images.githubusercontent.com/97538312/201193183-2252d2ed-a915-4d1d-b734-fa61ae8fb172.jpg)

## Classes to logged in viewers 
  - The book now button is shown
  
![classes_auth](https://user-images.githubusercontent.com/97538312/201193253-d616c879-8851-4726-9fb6-ada64418b095.jpg)


- **Register & Login Forms**
  - When the register or login option is selected by the user, they are redirected to the form page.
  - These forms are of very simplistic design for easy and satisfying user experience.
  - Both forms are designed to look the same and contain the same navbar and footer elements as on the main page.

## Register form
![signup](https://user-images.githubusercontent.com/97538312/204099776-1019a34c-b1ba-4175-a117-291956594794.jpg)

## Sign in form
![sign-in-screenshot](https://user-images.githubusercontent.com/97538312/202302531-b3fa0508-89ad-47df-8140-16c6126b0bef.jpg)

## Sign out
![sign_out](https://user-images.githubusercontent.com/97538312/204134892-8879b46d-5a4c-4626-bde8-5c34179e3c11.jpg)


## Booking
  - The booking system required a database to store in formation. For this 3 models were created. They store, Customer, Classes and the Booking details.
  - The booking page consists of a form which is made using crispy forms
  - The user must input their name, email, requested class and requested date
  - Once this is done if the fields are correct the form is recorded in the database
  - When booking, a user must enter the exact same username and email they used for signup or the booking may fail
![booking-page](https://user-images.githubusercontent.com/97538312/203824345-9ed984e1-9236-43f5-b7b9-35d97e2bd7ae.jpg)
  - The use of a calendar with the help of Jquery is in place for easy date selection 
  ![calendar](https://user-images.githubusercontent.com/97538312/204099599-90ea3c12-3f52-48d8-8dac-d4f8b5a07831.jpg)


## Manage Bookings
  - Users can see their made bookings in the manage bookings section
  - If no bookings are reorded by the user, they are redirected to the booking page
  - When a user wants to delete their booking an extra modal pops up to confirm this 
  - The bookings are displayed in Rows and 2 bookings show up per row
  ![booking_display](https://user-images.githubusercontent.com/97538312/204134931-d87036da-f066-44c6-823b-433af0dd653f.jpg)

  
  
## Unfixed Bugs 
  
  
## Testing 
- For the testing process I used print statements and kept running the code after a new function was added which was noticeable when run
- Verified the HTML using the W3C HTML validator and all tests passed : https://validator.w3.org/
- Verified CSS using the Jigsaw w3 css validator to confirm all css is valid : https://jigsaw.w3.org/css-validator/
- Tested the python code by running it through PEP8 online :  http://pep8online.com/
- JsHint was used to check JavaScript code : https://jshint.com/
- The only errors were to indicate that the line is too long
- I manually tested that errors in the form fields show up and required fields cannot be left empty
- Tested that messages get displayed when Logging in, adding to the bag, making any adjustments to products, on successfull or failed checkout and signing out.

## Message Testing / Toasts


## Form field testing 
![email_field_test](https://user-images.githubusercontent.com/97538312/204099630-8446fcaa-fc3a-42c9-a040-fe2ebcc00e19.jpg)

## Lighthouse test 
![lighthouse](https://user-images.githubusercontent.com/97538312/204099655-1f7ccfd5-edce-49d2-9a56-dc051040ef09.jpg)

## Webhook test / Stripe

## Checkout test

## Bag test

## Profile Information update test

## Design
 **The website was designed using Photoshop**
 - Please note that the final product does differ from the early-stage mockups

 ## Design Images

 
 ## Main page

## Products

## Product details / Individual product

## Register form

## Product management

## Bag

## Checkout




## Deployment 
  ### Heroku 
  - I deployed the project to heroku which is a cloud based hosting platform https://www.heroku.com/
    - Log in to Heroku
    - Select `New` and create a new app
    - Create an app name (as similar to repo name as possible)
    - Select a Region (Europe for me)
    - Click on `Create app`
  - Heroku took care of the config variables such as : DATABASE_URL, SECRET_KEY and CLOUDINARY_URL

  ### Elephant SQL
  - The database is deployed using ElephantSQL : https://www.elephantsql.com/
    - This is done by creating a new instance on ElephantSQL 
    - Select Table quries in BROWSER and select an option that looks familiar
    - The DATABASE URL is then pasted into heroku config vars 

  ### Github & Gitpod

  - The code institute full template is used for setting up this project on gitpod
  - When making a new repository
    -  Click `No Template` button
    -  Select the desired template
    -  Add a repository name
    -   To create a Gitpod workspace you then need to click `Gitpod`
    -   This will then start to build a workspace
  - The code is deployed and pushed to a Github branch which is then linked to heroku and set to automatically deploy with every push

  ### Amazon AWS Storage
  

## Credits
  - Credit 1 etc
  
