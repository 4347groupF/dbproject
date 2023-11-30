CS 4347.002 Team F
SQL Library Project

1. System Requirements
	A. Python: Latest version required, see Python Downloads at https://www.python.org/downloads/
	B. Django: Latest version required, see Django Downloads at https://www.djangoproject.com/download/
	C. Web Browser: Google Chrome is recommended

2. Server Startup Instructions
	A. Open command-line interface (CLI)
		a. Unix or MacOS: terminal
		b. Windows: Command Prompt
	B. (Optional) Activate virtual environment using:
		a. Unix or MacOS: source venv/bin/activate
		b. Windows: venv\Scripts\activate
	C. Install Python if not installed from the Python website
	D. Navigate to project directory containing manage.py
	E. Execute commands in sequence:
		a. python manage.py makemigrations
		b. python manage.py migrate
		c. python manage.py collectstatic
		d. python manage.py runserver
	F. Access server at http://127.0.0.1:8000/ in web browser

3. Technical Dependencies
	A. OS Compatibility: Works on MacOS, Windows, Linux
	B. Browser Support: Functional on Google Chrome, Internet Explorer, Safari
	C. Database Management: No DBMS installation needed, mySQL connectivity set in settings.py

4. Version Control Repository
	A. GitHub Repository: Visit https://github.com/4347groupF/dbproject for latest updates and repository access