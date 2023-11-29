Readme.txt

Requirements:
- Up-to-date python version (Go to below URL for installation).
	a. https://www.python.org/downloads/
- Web browser (Chrome recommended)

How to run server:
1. Open terminal.
2. Type below command in terminal for virtual environment execution.
	a. source venv/bin/activate
3. Install python if not installed.
4. Move to the directory where all files are saved (where manage.py is located).
5. Type below commands in order.
	a. python manage.py makemigrations
	b. python manage.py migrate
	c. python manage.py collectstatic
	d. python manage.py runserver
6. Type below URL in desired web browser.
	a. http://127.0.0.1:8000/

Technical dependencies:
- Compatible with any Operating Systems; MacOS, Windows.
- Compatible with known web browsers such as Chrome, Internet Explorer, Safari.
- Does not require to install DBMS, platform, nor frameworks as SQL server connection information is included in settings.py.

Github Repository:
- https://github.com/4347groupF/dbproject



 
