## Introduction

Welcome to my website.

Given the project brief, I wanted to make a fully functional website where the user create, read, update and delete their account and scheduled golf sessions.

A live website can be found [here](https://golfstar.herokuapp.com/).

# Table of Contents

-   [1. UX](#ux)
            -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Wireframes](#wireframes)
            -   [Design](#design)
-   [2. Features](#features)
-   [3. Project](#project)
-   [4. Testing](#testing)
-   [5. Project Checklist](#project-checklist)
-   [6. Deployment](#deployment)
-   [7. Bugs](#bugs)


# 1. UX

As an avid golfer, I have try my best to get out when I can and when it's quiet on the greens. I find the most convenient way of scheduling a round of golf is online. An easy to use visually appealing website that is concise makes it an appealing option to get a round of golf organised.

Hopefully this website will demonstrate such ease of use when it comes to CRUD functionality.

### Project Goals

The goal of this project is to build a website that allows the user to create and update a user account and create, update and delete a teetime booking in an easy efficient manner.

### User Goals:

New User
To be able to sign up for a user account.
To be able to shedule a teetime for a particular date and time.
TO be able to view the contact details of the website.

Account Holder:
To be able manage my tee time.
To be able to cancel a tee time if needed.
To be able to edit my account

### User Expectations:
To be able to navigate through the user interface with ease. 

-   The home page should be informative.
-   The navbar should make it easier to select the required feature.
-   The site should be resposive on mobile, desktop and ipad .

### User Stories
I took an AGILE approach to the implementation of the project. I used the tools on github such as issues, milestones and project boards to document my user stories. This helped to visualise and prioritise the project tasks. The labels, for example, are a good visual marker of what has to be done. The project board was useful to cycle the issues from to do, to doing and then finally to done.

# 2. Features

### All Pages
- The navbar is located at the top of all of the pages. The navbar is options will change accordingly as to when you are logged in or out.
- The footer contains social media icons. There is a zoom effect when hovering over icons. If icons are clicked the relevant links are provided.

### Register Page
- Is a signup form that prompts the user to enter an email address and a password. The password must be confirmed.
- The user will be prompted if they have created an account already. They can use the sign-in link to be redirected to the sign-in page.
- If the user has an account they will see an error message.
- If the password entered is not secure, they are given a message informing them that the password is not secure.
- If the user enters passwords that are not the same, a message is received informing them of same.
- Once the user has signed up, the user will be directed to the create account page.

### Login Page
- Requires the user to enter an email address and password.
- The user will be prompted if they have created an account already. They can use the sign-in link to be redirected to the sign-in page.
- If the user enters passwords that are not the same, a message is received informing them of same.

### Logout Page
- When clicking logout from the navigation bar, the user is redirected to a sign-out page to confirm their action.

### Home Page
- A Tee Off button lets the user to create a tee time page. If the user has not logged in it will prompt the user to register or log in first.
- A brief summary of the course is described.

### Create Account Page
- Once the user has registered they will be redirected to the create account page. The page displays a form for the user to enter their name, last name and number.

### Edit Account Page
- This page will display the current account details with a form below for the user to update details.

### Contact Page
- An information section that displays the number, email address, opening times and address.
- A contact form that requires the user to enter their full name, email address and a message.

### Create Tee time Page
- A form that requires the user to select the tee time details.
Full name and contact telephone number are prefilled if the user has created a account.
The user will then need to select a date, time, number of players.
- As the club is only open from 8 AM, if the user selects a time before that, the form will display an error.


### Change Tee time Page
- Displays all tee times in a list.
- It show a tee time reference, status, date, time, player count. It will also contain a button to change tee time details and a cancel tee time button.

### Edit Tee time Page
- This page will display the current tee time details with a form below for the user to update any details.
- When the changes are submitted, the tee time will be processed as the tee time requested status.

### Cancel Tee time
- When the user clicks the cancel tee time button they will be redirected to a confirmation page.

## 3. Project

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
   
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    
-   [PostgreSQL](https://www.postgresql.org/)
    
-   [Gitpod](https://www.gitpod.io/)
    
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    
-   [Balsamiq](https://balsamiq.com/)
    
-   [Google Fonts](https://fonts.google.com/)
    
-   [GitHub](https://github.com/)
    
# 4. Testing

### Google Developer Tools

I also checked the accessibility of the page using lighthouse.
![google_lighthouse](documentation_assets/images/google_lighthouse.png)

### Responsive Tools
I used [Am I Responsive](http://ami.responsivedesign.is) to make sure that all my pages are responsive to all devices.

### W3C Validator Tools
#### HTML:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.

#### CSS:
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within my CSS stylesheet.

### JavaScript:
I used [JS Hint](https://jshint.com/) to check for any errors within my JavaScript script tags.

### Python:
I used [PEP8 online](http://pep8online.com/) to check for any errors within my Python files. 

# 5 Project Checklist

- Install Django and the supporting libraries
    -  Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
    - Install support libraries including psycopg2, this is used to connect the PostgreSQL database
    - Install Cloudinary libraries, this is a host provider service that stores images
    - Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

- Create a new, blank Django Project
    - Create a new project
    - Create the app
    - Add restaurant_booking to the installed apps in settings.py
    - Migrate all new changes to the database
    - Run the server to test

- Setup project to use Cloudinary and PostgreSQL
    - Create new Heroku app
        - Sign into Heroku
        - Select New
        - Select create new app
        - Enter a relevant app name
        - Select appropriate region
        - Select the create app button

    - Attach PostgreSQL database
        - In Heroku go to resources
        - Search for Postgres in the add-ons box
        - Select Heroku Postgres
        - Submit order form

    - Prepare the environment and settings.py file
        - Create env.py file
        - Add DATABASE_URL with the Postgres URL from Heroku
        - Add SECRET_KEY with a randomly generated key
        - Add SECRET_KEY and generated key to the config vars in Heroku
        - Add if statement to settings.py to prevent the production server from erroring
        - Replace insecure key with the environment variable for the SECRET_KEY
        - Add Heroku database as the back end
        - Migrate changes to new database

    - Get static media files stored on Cloudinary
        - Create a Cloudinary account
        - From the dashboard, copy the API Environment variable
        - In the settings.py file create a new environment variable for CLOUDINARY_URL
        - Add the CLOUDINARY_URL variable to Heroku
        - Add a temporary config var for DISABLE_COLLECTSTATIC
        - In settings.py add Cloudinary as an installed app
        - Add static and media file variables
        - Add templates directory
        - Change DIR's key to point to TEMPALTES_DIR
        - Add Heroku hostname to allowed hosts
        - Create directories for media, static and templates in the project workspace
        - Create a Procfile
        
# 6. Deployment

I used the terminal to deploy my project locally. To do this I had to:
1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to local host address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, I had to:

1. Set debug = False in my settings.py file.
2. Commit and push all files to GitHub
3. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
4. In the deploy tab, go to the manual deploy sections and click deploy branch.

# 7. Bugs

<img width="704" alt="bug (2)" src="https://user-images.githubusercontent.com/88341568/196669401-2fba6b8b-7375-4604-b912-bf16b71e8d61.png">






