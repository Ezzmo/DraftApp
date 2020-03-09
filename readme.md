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
![ERD](https://github.com/Ezzmo/DraftApp/blob/master/ERD.png "ERD")



## User Stories 



## Risk Assessment 



[App](http://51.145.27.156:5000/)

## Issues and Improvements 
The majority of issues faced were due to inexperience in Web development. Error fixing took a lot of time and subsequently I was not able to manage my time as effectively as I would like. As a result, some parts of the specification were not met.

