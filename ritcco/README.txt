

This is a Sample Django Project created with following software installations:

Python			3.7
			
Django			2.0

SQLite			3.0



After cloning the repository:

1. Set up your django environment
2. Make  migrations
3. runserver

=> The portal opens on http://127.0.0.1:8000

=> This landing page allows you to add your following details:
		-* Name
		-* Phone
		-* Email ID
		-* Years of Experience
		-* Domain
		-* CV/Resume

=> Phone & Email ID are unique keys and can't be repeated

=> The uploaded files are stored in media folder inside the project folder

=> The registered users can be seen in the Applicant section of the page.
 
=> The RITCCO Admin logo takes you to the admin login Page.



Admin Login
=> The credentials for the admin login are as follows:
	id: ritcco
	pw: 123456
=> Here the admin can edit the Applicant object
=> So a selected candidate's object can be updated with a status of shortlisted and vice versa
=> A candidate can be deleted as well to remove that model entry.

