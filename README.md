#Project Thor
===
###Current To-Do List:
App: succinctly
	* Create views for the following pages:
		- Home
		- About
		- Contact
		- Terms of Service
		- Privacy
	* Edit the views for the following pages:
		- Index of all summaries
		- Detailed view of each summary
	* Create all pertinent tests	

App: accounts		
	* Build custom User model
	* Create the following views:
		- Login 
		- Logout
		- Edit page
		- Profile page
		- Will probably need to add other views as I go
	* Create the necessary methods to use with the registration that dont inherit
	* Shore up authentication and make sure Users have little to no permissions enabled
	* Create all pertinent tests	

Other:
	* Set up Crawler, either in the Django application or outside of it
		- If set up inside Django app, make sure it is governed by only superusers
		- And impossible to find if you dont know where to look for it
	* Make sure all the templates are pretty 
	* Edit the bootstrap set up so that the site looks mostly custom		