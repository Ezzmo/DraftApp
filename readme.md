#  Team Drafinng App

##  Project Brief
Create a CRUD application that has a CI pipeline.

##  Initial Idea:  
A board editable only by an admin that displays draft lineup for a team. Intended for use as a noticeboard for players to know if they're playing.

## Tables
###  Players 
-	These are the registered players, editable using resgister functionality.

### Teams
- The drafts that have been made so far

##  Interface
-	User is greeted by the home page which is the baord of teams so far. If the user is logged in as admin then they can access:
  - Navbar at the top links to: Home, About, Maker, Edit, Add players, Clear board, Logout
  - Home: the board
  - About: quick explanation
  - Maker: Create a lineup
  - Edit: edit lineups
  - Add players: Add players to the players table for use in lineups
  - Clear board: Clears the board if no longer needed
  - Logout
 -If they are not logged in then they can only acces the board and log in
## Technologies
- Hosting for virtual machines and database servers are both by Azure.
  - Database: Azure MySQL Server
  - Virtual Machine: Ubuntu 18.04
- For development, the code is written in Python, using the Flask framework for the architechture and HTML for the front end
- For the version control system, Git was used through Github.
- For the CI server:, Jenkins was used


## Entity Relationship Diagram 
![ERD](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/ERD%20Diagram%20(Database).png "ERD")
My initial ERD describes the relationships between all of my tables within my database, as you can see the user can has the capability of choosing from many leagues, as this is the permis of my project and will dictate what the user is allowed to choose in the next step which is the league that the club belongs to. 

![Added Table](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/ERD%20Diagram%202.png "Added Table")

My final ERD had some slight changes, in order to display the users chosen 5 aside team I had to create another table that onoce the five player values had been confirmed would go into, then print this on a separate HTML page. 

## User Stories 
![User Stories](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/User%20Stories.PNG "User Stories")


## Risk Assessment 
![Risk Assesment](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/Risk%20assesment.PNG "Risk Assesment")



Above is a screenshot of the final application, The drop down menus are driven by your previous chocie, only allowing you to select the club and player once you have confirmed the initial dropdown. Once ALL fields are chosen the user will be shown their selection.

[App](http://51.145.27.156:5000/)

## Issues and Improvements 
Throughout this project I faced many issues, I would have liked to have the players selection work properly, outputting the correct values and issuing the correct error messages so the app doesn’t break, also i would have liked to be able to print more information about the players that the user had chosen, for example the players position, club, and certain attributes but i did not have the time and it was too big of a risk trying to implement this and putting my project in jeopardy.

The next steps would be to fully fix the team selection page and have a more user-friendly team display page that shows more than just the name of the player, and to give the different players a picture. I would also like to add a team save function so that the user can name and save their teams and view or edit them later. Also properly implementing vigorous testing, that covers all aspects of the app, from testing the database to the login system etc. 

In future, to ensure that all builds that I make work correctly and are delivered in full by the project deadline is to spend less time thinking about the features and how I am going to implement them, if i had started sooner with coding I would have resolved the issues I faced sooner and been able to change or modify my application.
