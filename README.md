Project structure tree

> booksearchproject
>> booksearch
>>> static
>>>> booksearch
>>>>> any image files or .js files
>>>>> 
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

![Screenshot 2023-11-28 at 10 56 51 PM](https://github.com/4347groupF/dbproject/assets/1592134/dc1ed01d-8742-42e5-80ab-e9ab95e630dd)


<br />
To start the server:

*Encouraged to do it in virtual environment.
> source venv/bin/activate
> 
<br />

Move to directory where it has all files saved (where manage.py is located).
> python manage.py makemigrations (compile models.py)
> 
> python manage.py migrate
>
> python manage.py collectstatic (compile static files)
> 
> python manage.py runserver


https://4347groupf.github.io/dbproject/
