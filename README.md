Project structure tree

> booksearchproject
>> booksearch
>>> templates
>>>> booksearch
>>>>> .html files
>>>>>
>>> urls.py, views.py, models.py, forms.py
>>>
>> booksearchproject
>>> setting.py, urls.py, etc,..
>>>
>> scripts
>>> Update Fine.sql
>>>
>> manage.py







To start the server:

*Encouraged to do it in virtual environment.
> source venv/bin/activate

Move to directory where it has all files saved (where manage.py is located).
> python manage.py makemigrations (compile models.py)
> 
> python manage.py migrate
>
> python manage.py collectstatic (compile static files)
> 
> python manage.py runserver


https://4347groupf.github.io/dbproject/
