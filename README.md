## Introduction

Welcome to my website.

Given the project brief, I wanted to make a fully functional website where the user can create, read, update and delete their account and scheduled golf sessions.

A live website can be found [here](https://golfstar.herokuapp.com/).


<img width="916" alt="Am I resp pro 4" src="https://user-images.githubusercontent.com/88341568/211676464-a21a74cd-3930-4744-b9da-447868058b92.png">




# Table of Contents

-   [1. UX](#ux)
            -   [Project Goals](#project-goals)
            -   [User Goals](#user-goals)
            -   [User Expectations](#user-expectations)
            -   [Wireframes](#wireframes)
-   [2. Features](#features)
-   [3. Project Tools Used](#project-tools-used)
-   [4. Testing](#testing)
-   [5. Project Checklist](#project-checklist)
-   [6. Deployment](#deployment)
-   [7. Bugs](#bugs)


# 1. UX

As an avid golfer, I have tried my best to get out when I can and when it's quiet on the golf course. I find the most convenient way of scheduling a round of golf is online. An easy to use visually appealing website that is concise makes it an appealing option to get a round of golf organised.

Hopefully this website will demonstrate such ease of use when it comes to CRUD functionality.

### Project Goals

The goal of this project is to build a website that allows the user to create and update a user account and create, update and delete a teetime booking in an easy efficient manner.

### User Goals

New User
To be able to sign up for a user account.
To be able to shedule a teetime for a particular date and time.
To be able to view the contact details of the website.

Account Holder:
To be able change my tee time.
To be able to cancel a tee time if needed.
To be able to edit my account

### User Expectations
To be able to navigate through the user interface with ease. 

-   The home page should be informative.
-   The navbar should make it easier to select the required feature.
-   The site should be resposive on mobile, desktop and ipad .

### Wireframes:


<img width="720" alt="2023-01-10 (7)" src="https://user-images.githubusercontent.com/88341568/211678975-4b92e0e8-ba94-4918-83d5-ea2388487e9f.png">


<img width="447" alt="2023-01-10 (11)" src="https://user-images.githubusercontent.com/88341568/211679601-45ff9ac4-96a7-49b8-86ed-6c402c9c27e9.png">


<img width="697" alt="2023-01-10 (13)" src="https://user-images.githubusercontent.com/88341568/211680156-bd88a678-d040-4fc6-a797-af593e9f13cc.png">



### User Stories
I took an AGILE approach to the implementation of the project. I used the tools on github such as issues, milestones and project boards to document my user stories. This helped to visualise and prioritise the project tasks. The labels, for example, are a good visual marker of what has to be done. The project board was useful to cycle the issues from to do, to doing and then finally to done.


<img width="956" alt="2023-01-10 (5)" src="https://user-images.githubusercontent.com/88341568/211677380-1d87bdfc-5dde-40f1-a37b-261c99669e20.png">



# 2. Features

### All Pages
- The navbar is located at the top of all of the pages. The navbar options will change accordingly as to when you are logged in or out.
- The footer contains social media icons. There is a zoom effect when hovering over icons. If icons are clicked the relevant links are provided.


<img width="645" alt="2023-01-10 (26)" src="https://user-images.githubusercontent.com/88341568/211682686-e92ca433-6b02-4891-a305-e9626ad62573.png">


<img width="652" alt="2023-01-10 (25)" src="https://user-images.githubusercontent.com/88341568/211682545-4ea36032-060d-4584-adee-6d6c0c84ab61.png">




### Register Page
- Is a signup form that prompts the user to enter an email address and a password. The password must be confirmed.
- The user will be prompted if they have created an account already. They can use the sign-in link to be redirected to the sign-in page.
- If the user has an account they will see an error message.
- If the password entered is not secure, they are given a message informing them that the password is not secure.
- If the user enters passwords that are not the same, a message is received informing them of same.
- Once the user has signed up, the user will be directed to the create account page.


<img width="956" alt="2023-01-10 (38)" src="https://user-images.githubusercontent.com/88341568/211686121-32434844-2a90-489e-86fd-4fccd8f7386d.png">



### Login Page
- Requires the user to enter an email address and password.
- The user will be prompted if they have created an account already. They can use the sign-in link to be redirected to the sign-in page.
- If the user enters passwords that are not the same, a message is received informing them of same.


<img width="960" alt="2023-01-10 (28)" src="https://user-images.githubusercontent.com/88341568/211686331-72418e47-6592-476c-b7ff-a501f11b929a.png">



### Logout Page
- When clicking logout from the navigation bar, the user is redirected to a sign-out page to confirm their action.


<img width="956" alt="2023-01-10 (29)" src="https://user-images.githubusercontent.com/88341568/211686546-0e04a532-f563-4dce-b1b3-3df6ae94c33e.png">




### Home Page
- A Tee Off button lets the user to create a tee time page. If the user has not logged in it will prompt the user to register or log in first.
- A brief summary of the course is described.


<img width="960" alt="2023-01-10 (16)" src="https://user-images.githubusercontent.com/88341568/211686224-26f9954d-36e4-4714-b724-453d2e64bb62.png">



### Edit Account Page
- This page will display the current account details with a form below for the user to update details.


<img width="956" alt="2023-01-10 (30)" src="https://user-images.githubusercontent.com/88341568/211687569-b072491f-2fbb-4c49-bb0a-2e0a18057039.png">



### Contact Page
- An information section that displays the number, email address, opening times and address.
- A contact form that requires the user to enter their full name, email address and a message.


<img width="960" alt="2023-01-10 (31)" src="https://user-images.githubusercontent.com/88341568/211687659-52f3d216-cfab-46d1-9c61-810ff2e8979a.png">


### Create Tee time Page
- A form that requires the user to select the tee time details.
Full name and contact telephone number are prefilled if the user has created an account.
The user will then need to select a date, time, number of players.


<img width="960" alt="2023-01-10 (32)" src="https://user-images.githubusercontent.com/88341568/211687799-1011303f-e968-4916-af9f-26cf881ed98d.png">



### Change Tee time Page
- Displays all tee times in a list.
- It shows a tee time reference, status, date, time, player count. It also contains a button to change the tee time details and a cancel tee time button.


<img width="956" alt="2023-01-10 (33)" src="https://user-images.githubusercontent.com/88341568/211688087-ab20b6e4-a392-4c19-99fb-9b610a986b73.png">



### Cancel Tee time
- When the user clicks the cancel tee time button they will be redirected to a confirmation page.


<img width="956" alt="2023-01-11 (2)" src="https://user-images.githubusercontent.com/88341568/211689890-eb77a58c-e2e3-4568-84ca-f1058a24a992.png">



## 3. Project Tools Used

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

I checked the performance and accessibility of the pages using lighthouse.


<img width="954" alt="Lt perf home" src="https://user-images.githubusercontent.com/88341568/211690301-9fb9db12-a75f-425a-9d79-af7836664c18.png">


<img width="956" alt="Lt perf contact" src="https://user-images.githubusercontent.com/88341568/211690341-538acfbc-ea37-4dfb-82c4-4715f38bcaf4.png">


<img width="949" alt="Lt perf signup" src="https://user-images.githubusercontent.com/88341568/211690395-5fb66699-db2f-42ee-912a-e6a3c0a97198.png">


<img width="955" alt="Lt perf signin" src="https://user-images.githubusercontent.com/88341568/211690440-6d9eedc2-1b8e-4e32-9aa6-07b785a6c21f.png">


<img width="955" alt="Lt perf teetime" src="https://user-images.githubusercontent.com/88341568/211690526-db61d9f9-2cc6-494f-9cef-b5542099eaff.png">


<img width="955" alt="Lt perf edit acc" src="https://user-images.githubusercontent.com/88341568/211690583-4987fe74-f187-4755-8368-76f0a6d7f13b.png">


<img width="955" alt="Lt perf change teetime" src="https://user-images.githubusercontent.com/88341568/211690624-fcba8fce-bc90-46a0-88e3-f4e8cf686e14.png">


<img width="955" alt="Lt perf signout" src="https://user-images.githubusercontent.com/88341568/211690656-eea4d810-7b88-4e16-9731-9e6f9620367a.png">



### Responsive Tools
I used [Am I Responsive](http://ami.responsivedesign.is) to make sure that all my pages are responsive on all devices.

### W3C Validator Tools
#### HTML:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.


<img width="956" alt="2023-01-11 (7)" src="https://user-images.githubusercontent.com/88341568/211766637-084a8018-0ce4-4c8b-bb02-72493dc3ba91.png">


#### CSS:
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within my CSS stylesheet.


<img width="960" alt="2023-01-11 (8)" src="https://user-images.githubusercontent.com/88341568/211767488-4c9afc5c-472a-4403-8d2d-792295c67757.png">


### JavaScript:
I used [JS Hint](https://jshint.com/) to check for any errors within my JavaScript script tags.


<img width="490" alt="2023-01-11 (10)" src="https://user-images.githubusercontent.com/88341568/211768241-2aca4ea6-7e1d-49ab-873e-e76b0aa26b6e.png">


### Python:
I used [PEP8 online](http://pep8online.com/) to check for any errors within my Python files.


### Manual Testing:
I tested the website on various different browsers and devices.

- Browsers

            - Mozilla Firefox.
            - Google Chrome.
            - Microsoft Edge.
          
- Devices

            - Android Smartphone.
            - Ipad Air.
            - Laptop.
            

# 5 Project Checklist

- Install Django and the supporting libraries

            - Install Django and Gunicorn. Gunicorn is the server I am using to run Django on Heroku.
            - Install support libraries including psycopg2, this is used to connect the PostgreSQL database
            - Install Cloudinary libraries, this is a host provider service that stores images
            - Create the requirements.txt file. This includes the project's dependencies allowing us to run the project in Heroku.

- Create a new, blank Django Project
            
            - Create a new project
            - Create the app
            - Add app to the installed apps in settings.py
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


<img width="956" alt="2022-10-15 (4)" src="https://user-images.githubusercontent.com/88341568/211751238-a0c0b9df-6712-481d-b9a3-7ab5e384e346.png">



# 7. Resolved Bugs

I was getting a server 500 error. Firstly I had change my DEBUG settings to True to view the bug. In order to resolve the issue I needed to change my model to include the null=True value rather than null=blank.


<img width="960" alt="player count err (2)" src="https://user-images.githubusercontent.com/88341568/211751523-b86726c7-4ccc-4701-b8ba-868c6967b099.png">


<img width="960" alt="2023-01-11 (3)" src="https://user-images.githubusercontent.com/88341568/211753693-b4ef546d-fe36-4225-bf8d-f5e8eedb18f7.png">


I had an application error. In my requirements.txt file, I found that gunicorn had not been installed. Once it was installed the application error subsided.


<img width="956" alt="2022-12-07 (8)" src="https://user-images.githubusercontent.com/88341568/211754513-6bd1258c-643e-4e55-9eb5-60efee64a1fd.png">



# 8. Credits

- Code
            
            - Bootstrap - The styling and column structure.
            - Code Institute – project tutorials.
            
- Content
            
            - Images – https://www.pexels.com/
            - Colour scheme – https://mycolor.space/
            - Compress images – https://tinypng.com/ 
            - Font - https://fonts.google.com/
            - Icons - https://fontawesome.com/

- Project Acknowledgements

            - Code Institue Tutor Support.
            - My Mentor.













