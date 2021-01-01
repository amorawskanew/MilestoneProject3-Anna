<img src="/static/images/READme_image.png"/>
<h1 align="center">Cocktail Collections Website</h1>

[View the live project here.](http://milestone-project3-anna.herokuapp.com/)

APPLICATON'S PURPOSE

Cocktail Collections is an application where users can share their favorite cocktail recipes with others, thereby providing a useful source of information for those who like experimenting with new drink ideas.

This application allows users to add cocktail recipes, edit, update, or delete them. It also has a section with top bartenders and links to the best cocktail bars in the world, so users can learn tips from the industry leaders.

 It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential users... cocktail lovers

## USER EXPERIENCE (UX)

-   ### USER STORIES

    -   #### FIRST TIME VISITORS GOALS

        1. First Time Visitors should be able to easily understand the main purpose of the site and get familiar with its structure.
        2. They should be able to easily navigate throughout the site to find the content they are interested in.
        3. The content of the website should be appealing enough so the first time users remember it and want to come back.


    -   #### RETURNING VISITORS GOALS

        1. Returning Visitors should be able to go through the site and find the type of drink recipe they are interested in and use it.
        2. Returning Visitors should be able to find community links or cocktail related quality websites.

    -   #### FREQUENT VISITORS GOALS
        1. Frequent Users should be able to share their cocktail recipes or modify the existing ones.
        2. They should be able to develop better cocktail making skills and get inspired to create their own unique recipes.
        
-   ### DESIGN
    -   #### COLOUR SCHEME
        -   The two main colours used are orange and black, and a white background.

    -   #### IMAGES
        -   The images for the Landing and Stars pages were downloaded from the internet and are stored locally in a folder "images". The rest of the images are downloaded via URL links, which are part of MongoDB. 
        Images were chosen for their vibrant colors and modern aestetics. The website's colors are designed to catch the user's attention and stimulate his brain.

*   ### DESIGN PROCESS

 I started my design process by doing online research on cocktail websites and applications. I checked mainly top recommendations. Most of them were very complex and required some time to learn how to navigate them. I wanted to create something that would be very simple and easy to use, but at the same time informative and useful for potential visitors.
I sketched the layouts of the main pages and planned how a user would go from one page to another. I wanted to create an app that users could use a bit like an open notebook where others can access and share their recipes.

I discovered Frigma only when my app was almost finished, so I couldn't really benefit from this tool, but it looks like it can be a big help in the planning and designing process. I will try to use it in my next project.

*   ### DATABASE
The database of cocktail recipes was built based on IBA ( International Bartenders Association) Standards and is stored in Mongo DB in a form of two collections: "categories" and "cocktails"


## FEATURES

* EXISTING FEATURES

1. HOME PAGE
2. COCTAIL CATEGORY PAGE
3. INDIVIDUAL COCKTAIL PAGE
4. STARS
5. ALL COCKTAILS
6. ADD NEW COCKTAIL


HOME PAGE is my landing page where I briefly explain the purpose of the app and display nine various cocktail categories. Each category has a pulsing cocktail icon, which when clicked on reveals a small piece of information on a given category. Beneath the category image, there is a category name and a clickable link "Click Me", that takes a user to the chosen category page. 

* The cocktail categories are as follow:
    *Classics
    *New era drinks
    *Specials
    *Beer cocktails
    *Wine cocktails
    *Liquor cocktails
    *Flaming drinks
    *Non-alcoholic drinks
    *Excentric

When you click on one of the cocktail categories ON HOME PAGE, you get displayed a collection of cocktails that belong to that category. 

COCKTAIL CATEGORY PAGE- Here you can choose your favorite cocktail and go to the  COCKTAIL INDIVIDUAL PAGE by clicking on the button "VIEW COCKTAIL"
You can also access a cocktail of your choice via ALL COCKTAILS page, where all the cocktails are displayed.
I have also added a page STARS where you can get familiar with some of the top cocktail creators in the industry. 

* FEATURES LEFT TO IMPLEMENT

1. Chat window or page where users can communicate and exchange ideas on new drinks.
2. links to social media 
2. Signin\Login\Register form

## TECHNOLOGIES USED

### LANGUAGES

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python)

### FRAMEWORKS, LIBRARIES & PROGRAM USED

1. [Frigma](https://www.figma.com/files/recent)
    - I used Figma a bit to help me design the wireframes for various screen sizes, but I didn't have enough time to get familiar with this software and at the end I switched to paper and pencil. Yet, I found it a great tool, which is definitely worth exploring. I might use it in my future projects.
2. [Color converter](https://convertacolor.com/)
    - Color convertor was used to covert colors to hsla system that allows to changing the opacity of the color. I used it to make the orange color of the flash messages slightly transparent and less saturated to create a more pleasant experience for the potential user.
3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import fonts such as Poppins, Anton, Sans Work, which were used to style text on all pages throughout the project.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
5. [jQuery:](https://jquery.com/)
    - jQuery was mainly used to initialize the Materialize CSS framework.
6. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
7. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
8. [Google Photos:](https://www.google.com/photos/about/)
    - Google Photos was used to resize and edit the image for READEME.md, HOME and STARS pages of Cocktail Collections app.
9. [Heroku:](https://devcenter.heroku.com/categories/reference)
    -Heroku was used as a hosting platform to deploy the live version of my app.
10. [Materialize:](https://materializecss.com//)
    - Materialize was used to create and style the project's navbar, footer, cards and add and edit cocktail forms. 
11. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The Python microframework used to help write the Python code for this project. 
12.    [MongoDB:](https://www.mongodb.com/2)
    - Was used to store data in the cloud.
13.   [PyMongo:](https://pymongo.readthedocs.io/en/stable/)
    - PyMongo was used as the Python API for MongoDB. This API enabled me to link the data from the back-end database to the front-end app. 



## TESTING

I tested every component of my app as I was building it: Navigation bar, Footer, CRUD functionalities,checking if all the elements work properly. I tested every page on different devices: iphone, iPad, desktop.
Also, I checked its functional aspect by asking friends to add a recipe and observed how long it takes to load the page.


### TESTING TOOLS

The following testing tools were used to minimize site errors:

- [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
- [pyTest](https://docs.pytest.org/en/stable/getting-started.html)
- [PEP8](http://pep8online.com/checkresult)
- [HTML Formatter](https://www.freeformatter.com/html-formatter.html)
- [Language Tool](https://languagetool.org/?l=en&utm_source=google&utm_medium=cpc&utm_campaign=spell_checker&utm_term=online%20spell%20check&)
- [CSS Beautyfier](https://www.freeformatter.com/css-beautifier.html)


### TESTING USER STORIES

#### FIRST TIME VISITOR EXPERIENCE

* To learn more about the content of the app and be able to smoothly navigate throughout all the pages. I noticed that navigation is not entirely smooth. A return button could be added on  the Individual cocktail page so the user can go back to directly the category page.

#### RETURNING VISITOR EXPERIENCE

* As a Returning Visitor, I want to find new cocktail recipes and be able to share them. I can easily access the recipes, but the share to social media button is not included.

#### FREQUENT USER EXPERIENCE

* As a Frequent User, I want to see if the app is popular and if there are any activities that can add value. The site doesn't have any connection to other users and this aspect still needs to be developed.

### COMPABILITY TESTS

I tested my app on the following browsers to see if everything worked as planned:

* Apple Safari
* Google Chrome (main testing browser)

### USING VARIOUS DEVICES

* The project has been tested via Chrome dev tool on 20 various devices such as Desktop, Laptop, iPhone, Kindle, iPad, etc.

### MANUAL TESTS

I  A large amount of testing was done to ensure that all pages were linking correctly and that all the components of the app operate as intended.

I checked: 

* Menu bar
* Footer
* Home
* Add cocktail
* Edit cocktail
* Delete cocktail
* All cocktails
* Category cocktail page
* Stars


### KNOWN BUGS

-   On iPhone 5/SE the delete button is slightly squeezed from the right side. It can be probably easily fixed, just requires some extra time and internet googling.
-Footer links are not perfectly aligned. I tried to modify it with CSS flexbox, grid ,and Absolute\Relative positioning, but again lack of experience and time constrain didn't let me achieve the results that would fully satisfy me.
- An image for "Honey Special Cocktail" from my DB doesn't always download, but it can be removed or replaced with another one. I just like it so much that I decided to keep it anyway, at least for some time.
- The word cocktail was misspelled at the beginning of my app development process and I didn't see it until my mentor pointed it out to me during our last project session. I did some corrections on the site where it is visible for the user, but I kept the misspelled version as variable name  spelled - coctail-  without "k"
Excentric is also not the word I wanted to use (I meant Eccentric), but this word at least exists, so I didn't do any changes.

## DEPLOYMENT

My project was first developed using Gitpod as the chosen IDE and GitHub as a remote repository.

The project's GitHub repository link: https://github.com/amorawskanew/MilestoneProject3-Anna

The deployed project link: https://milestone-project3-anna.herokuapp.com/

## DEPLOYMENT TO HEROKU - STEPS

    * First, I created my project on Gitpod (
    * Project files and folders
    * requirements.txt file using "pip3 freeze --local > requirements.txt" command
    * Procfile file that starts with capital using "echo web: python3 app.py > Procfile" command
    * I committed both files to GitHub
    * Next, I signed in to Heroku and created a new application
    * I set the region to Europe (which is the closest to Holland)
    * I went to Reveal Config Variables and input all the required values such as:
    MONGO_URI, IP, SECRET_KEY, PORT 
    Note: I put the wrong password in my MONGO_URI, which resulted in an authentification bug.
    * I logged into Heroku from my Gitpod terminal and then pushed all my commits to Heroku via $ git push Heroku master.
    * This completed the process of deploying my project to Heroku. 
    * Once deployed, I continued to push all changes made to "Cocktail Collections" to Heroku throughout the whole development process.

## CREDITS

### USED MATERIALS

-   [Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME): For letting me use the README document as a template and reference document for my own READEME, as well as creating very informative tutorial videos that were the basis for my project.
-    [StackOverflow post](https://stackoverflow.com) for providing card styling ideas that I used for my Home page.
-   [Oston Code Cypher](https://www.youtube.com/watch?v=7yLcgKxBRVg&t=1082s): For making creating a video on How to Create Simple & Responsive Cards using Materialize CSS

And many others

* Materialize website
* Google icons
* StuckOverflow website
* Various online tutorials and documentation on python
* W3 Shools.com page for CSS styling
* Ideas from Tutor online support 

I read and used a lot of materials throughout the application development process. I have documented only some of them as I didn't have time to keep track of all of them. I researched a lot of apps (online, Youtube, Github, etc..) for concept inspiration as well as web layouts.

### CONTENT

-   Content of this project is a result of the collaboration between my mentors, Slack Community, Tutors, and online developer communities.

### MEDIA

-   The images used in this project were obtained from multiple blogs/articles/recipes, bartending, and mixology websites (over 40 websites).


### ACKNOWLEDGEMENTS

-   A big thank you to my mentor Anna Villanueva and Owonikoko Oluwaseun for their support throughout the project and continuous feedback that helped me to improve my app. My mentors helped me to conceptualized the project by suggesting how to organize it and provided me with various examples of similar apps. One of the greatest tools I discovered thanks to my mentors was PEP8, the W3C Validation Service and other testing tools that helped me to become more independent in debugging my code.

-   Thank you to all the wonderful Code Institute Tutors for their patience and help with debugging my app. 