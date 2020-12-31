
*Testing Tools
"inspect" from  Development Tools.
Validator check the code ( HTML, CSS) 

6.DIFFICULTIERS:
 I had some issues with loading my css file. Sometimes it didn't show the modifications I applied to a page and had to "hard reload" quite often. 
 Some of the CSS styling is placed within showcoctail.html file as it didnt work when moved to style.css

<<<<<<< HEAD

=======
6.DIFFICULTIERS:
 I had some issues with loading my css file. Sometimes it didn't show the modifications I applied to a page and had to "hard reload" quite often. 
 Some of the CSS styling is placed within showcoctail.html file as it didnt work when moved to style.css


>>>>>>> 860a43e204fd91659033f44fe28b0d353288c69d
7.THINGS I AM HAPPY ABOUT:

I am definitely happy I kept my project simle, which helped me focus on pracrticing implementation of CRUD technologies. Before starting the project, I went through 
most nof the Code institute tutorial videos again to made sure I know what and why I want to use. Also, my mentor and slack community was wery helpful as they guided me through 
the brainstorming part of the project, which was the most challenging for me. Once the wireframe was in place I was able to to work on it mostly independently.

8.USED MATERIALS
*Code Institute video tutorials 
*Youtube videos -mainly for styling cards and making images responsive
eg. https://www.youtube.com/watch?v=7yLcgKxBRVg&t=1078s
*Materialize website
*Google icons
*StuckOverflow website
*Various online tutorials and documentation on python
*W3 Shools.com page for CSS styling
*Tutor online support 

Navbar, Footer and cards code were taken from Materialize, but they are very similar to those from the Code Institute tutorial videos.
Code for the cards for the landing page were taken from Youtube video "How to create Simple & Responsive Cards using Materialize CSS".
The main code for add cocktail was taken from Code institute tutorial ,modified and ajusted to my apps requiements.

9.MEDIA
The photos used in this site were obtained from multiples blogs/articles/webs about recipies, bartending and mixology

CREDITS
I received inspiration for this project from my mentor,Owonikoko Oluwasun. 
Also, a big thank you to all the slack community and Code Institute tutors.
<<<<<<< HEAD

Student, Anna Morawska
=======



 



<img src="/static/images/READme_image.png"/>
<h1 align="center">Cocktail Collections Website</h1>

[View the live project here.](http://milestone-project3-anna.herokuapp.com/)

APPLICATON'S PURPOSE

Cocktail Collections is an application where users can share their favourite cocktail recipes with others, thereby providing a useful source of information for those who like experimenting with new drink ideas.

This application allows users to add cocktail recipe, edit, update or delete it. It also has a section with top bartenders and links to the best cocktail bars in the world, so users can learn tips from the industry leaders.

 It is designed to be responvive and accessible on a range of devices, making it easy to navigate for potential users... cocktail lovers

<h2 align="center"><img src="https://i.ibb.co/TYvTXz1/Example-CI.png"></h2>

## User Experience (UX)

-   ### USER STORIES

    -   #### First Time Visitor Goals

        1. First Time Visitors should be able to easily understand the main purpose of the site and get familiar with the structure of the web.
        2. They should be able to easily navigate throughout the site to find content they are interested in.
        3. The content of the website should be appealing enough so the first time users remember it and want to come back.


    -   #### RETURNING VISITORS GOALS

        1. Returning Visitors should be able to go through the site and find the type of a dring recipe they are interested in and use it.
        2. Returning Visitors should be able to find community links or cocktail related quality websites.

    -   #### Frequent User Goals
        1. Frequent Users should be able to share their cocktail recipes or modify the existing ones.
        2. They should be able to develop better cocktail making skills and get inspiration to design their own unique recipes
        
-   ### DESIGN
    -   #### Colour Scheme
        -   The two main colours used are orange and black, and a white background.

    -   #### IMAGES
        -   The images for the landing and the stars pages were downloaded from internet and are stored locally in a folder "images". The rest of ithe mages are downloaded via url links, which are part of MongoDB. 
        Images were chosen for their vibrant colors and modern aestetics. The website's colors are designed to catch user's attention and stimulate his brain.

*   ### DESIGN PROCESS

 I started my design process from doing online research on cocktail websies and applications. I checked mainly top recommendations. Most of them were very complex and required some time to learn how to navigate them. I wanted to create something that would be very simple and easy to use, but at the same time informative and useful for potencial visitors.
I sketched the layouts of the main pages and planned how a user would go from one page to another. I wanted to create an app that users could use a bit like an open notebook where other can access and share their recipes.

I discovered Frigma only when my app was almost finished, so I couldn't really benefit from this tool, but it looks like it can be a big help in planning and designimg process. I will try to use it it next time.

*   ### DATABASE
Thge datata base of cocktail recipies was built based on IBA ( International Bartenders Association) and is stored in Mongo DB in a form of twwo collections: "categories" and "coctails" 


## FEATURES

* EXISTING FEATURES

1. HOME PAGE
2. COCTAIL CATEGORY PAGE
3. INDIVIDUAL COCKTAIL PAGE
4. STARS
5. ALL COCKTAILS
6. ADD NEW COCKTAIL


HOME PAGE is my landing page where I briefly explain the purpose of the app and display  nine different cocktail categories. Each category has a pulsing cocktail icone, which when clicked on reveals a small piece of information on a given category. Beneath the category image, there is a category name and a clickable link "Click Me", that takes a user to the chosen category page. 

* The cocktail categories are as follow:
    *Classics
    *New era drinks
    *Specials
    *Beer cocktails
    *Wine cocktails
    *Liquor coctails
    *Flaming drinks
    *Non-alcoholic drinks
    *Excentric

When you click on one of the cocktail categories ON HOME PAGE, you get displayed a collection of cocktails that belong to that category. 

COCTAIL CATEGORY PAGE- here you can choose your favorite cocktail and go to the  COCKTAIL INDIVIDUAL PAGE by clicking on the button "VIEW COCKTAIL"
You can also access a cocktail of your choice via ALL E. COCKTAILS page, where all the cocktails are displayed.
I have also added a page STARS where you can get familliar with some of the top cocktail creaters in the industry. 

* FEATURES LEFT TO IMPLEMENT

1. Chat window or page where users can communicate and exchange ideas on new drinks.
2. links to social media 
2. Signin\Login\Register form



-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages 

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python)

### Frameworks, Libraries & Programs Used

1. [Frigma](https://www.figma.com/files/recent)
    - In the begining I used Figma to help me design the wireframes for diffrent screen sizes, but I didn't have enough time to get familiar with this software and at the end I switched to paper and pencil. Yet, I found it a great tool, definitely worth exploring and I might use in my future projects.
2. [Color convertor](https://convertacolor.com/)
    - Color convertor was used to covert colors to hlsa sysstem taht allows to change opacity of the color. I used it to make the orange color of the flash messages slightly transparent so they create more pleasant experience for the user.
3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import fonts such as Poppins, Anton, Sans Work, which were used to style text on all pages throughout the project.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
5. [jQuery:](https://jquery.com/)
    - jQuery was mainly used to initialise the Materialize CSS framework.
6. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
7. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
8. [Google Photos:](https://www.google.com/photos/about/)
    - Google Photos was used to resize and edit the image for READEME.md, HOME and STARS pages of Cocktail Collections app.
9. [Heroku:](https://devcenter.heroku.com/categories/reference)
    -Heroku was used as a hosting platform to deploy the live version of my app.
10. [Materialize:](https://materializecss.com//)
    - Materialze was used to create and style the project's navbar, footer, cards. add and edit cocktail forms. 
11. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The Python microframework used to help write the Python code for this project. 
12.    [MongoDB:](https://www.mongodb.com/2)
    - Was used to store data in the cloud.
13.   [PyMongo:](https://pymongo.readthedocs.io/en/stable/)
    - PyMongo was used as the Python API for MongoDB. This API enabled me to link the data from the back-end database to the front-end app. 



## TESTING

I tested every component of my app as I was building it: Navigation bar, Footer, CRUD functionalities,checking if all the elements work properly. I tested every page on different devices: iphone, ipad, desktop.
Also, I checked its functional aspect by asking firiends to add a recipie and observed how long it takes to load the pagre.


### TESTING TOOLS

The following testing tools were used to minimaze the APP of errors:

- [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
- [pyTest](https://docs.pytest.org/en/stable/getting-started.html)
- [PEP8](http://pep8online.com/checkresult)
- [HTML Formatter](https://www.freeformatter.com/html-formatter.html)
- [Language Tool](https://languagetool.org/?l=en&utm_source=google&utm_medium=cpc&utm_campaign=spell_checker&utm_term=online%20spell%20check&)
- [CSS Beautyfier](https://www.freeformatter.com/css-beautifier.html)


### TESTING USER STORIES

#### First Time Visitor Experience

* to learn more about the content of the app and be able to smoothly navigate throughout all the pages. I noticed that navigation is not entirely smooth. A return button is missing on Individual cocktail page so the user can go back to category page.

#### Returning Visitor Experience

* As a Returning Visitor, I want to find the new cocktail recipes and be able to share them. I can easily acces the recipes, but share tosocial media buttons are missing.

#### Frequent User Experience

* As a Frequent User, I want to  to see if the app is popular and if there is any activities that can add value to me or to Cocktail creators community. The site doesn't have any connection to other user and this aspect still needs to be developped

### Compatibility tests

I tested my app on the following browsers to see if everything worked as planned:

* Apple Safari
* Google Chrome (main testing browser)

### Using different devices

* The project has been tested using Chrome dev tool on 20 different devices such as as Desktop, Laptop, iPhone, kinddle, iPad, etc.

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
-Footer links are not perfectly aligned. I tried to modify it with CSS flexbox, grid and Absolute\Relative positioning, but again lack of experience and time constrain made didn't let me achieve the results that would fully satisfy me.
- An image for "Honey Special Cocktail" from my DB doesn't always download, but it can be removed or replaced with another one. I just like it so much that I decided to keep it anyway, at least for some time.
- The word cocktail was misspelled at the beginning of my app development process and I didn't noticed it to the very last moment when my mentor pointed it out to me during our last project session. I did some corrections on the site where it is visible for the user, but kept the msspelled version as variable name  spelled without "k" -coctail.
Excentric is also not the word I wanted to use (I meant Eccentric), but this word is at least spelled correctly, so I didn't do any changes.


## DPLOYMENT

Deployment
My project was first developed using Gitpod as the chosen IDE and GitHub as a remote repository.

The deployed project link: https://milestone-project3-anna.herokuapp.com/

The project's GitHub repository link: https://github.com/amorawskanew/MilestoneProject3-Anna

## DEPLOYMENT TO HEROKU - STEPS

    * First, I created my project on Gitpod (
    * Project files and folders
    * requirements.txt file using "pip3 freeze --local > requirements.txt" command
    * Procfile file that starts with capital using "echo web: python3 app.py > Procfile" command
    * I cmmited both filles to GitHub
    * Next, I signed in to Heroku and created a new application
    * I set the region to Europe (which is the closest to Holland)
    * I went to Reveal Config Variables and input all the required values such as:
    MONGO_URI, IP, SECRET_KEY,PORT 
    Note: I put the wrong password in my MONGO_URI, which resulted in authentification bug.
    * I logged into Heroku from my Gitpod terminal and then pushed all my commits to Heroku via $ git push heroku master.
    * This completed the process of deploying my project to Heroku. 
    * Once deployed, I continued to push all changes made to "Cocktail Collections" to Heroku throughout the whole development process.

## CREDITS

### USED MATERIALS

-   [Code Institute](https://github.com/Code-Institute-Solutions/SampleREADME): For lettig me use the README document as a template and reference document for my own READEME, as well as creating very informative tutorial videos that vere the basis for my project.
-    [StackOverflow post](https://stackoverflow.com) for providing cards styling ideas that I used for my for my Home page.
-   [Oston Code Cypher](https://www.youtube.com/watch?v=7yLcgKxBRVg&t=1082s) : For making available video on How to create Simple & Responsive Cards using Materialize CSS

And many others

* Materialize website
* Google icons
* StuckOverflow website
* Various online tutorials and documentation on python
* W3 Shools.com page for CSS styling
* Ideas from Tutor online support 

I read and used a lot of materials throughout the application development process. I have documented only some of them as I didn't have time to keep track of all of them.

### CONTENT

-   Content of this project is a result of the collaboration between  my mentors, Slack Community, Tutors and on line materials.

### MEDIA

-   The images used in this project were obtained from multiple blogs/articles/recipe,  bartending and mixology websites.


### Acknowledgements ACKNOWLEDGEMENTS

-   A big thank you to my mentor Anna Villanueva and Owonikoko Oluwaseun for their support througout the project and continuous feedback that helped me to improve my app.

-   Thank you to all the wonderful Code Institute Tutors for their patience and help with debuging my app. 