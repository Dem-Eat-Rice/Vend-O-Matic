# vend-o-matic
	This is my implementation of a vending machine based on the specifications given.
	I made a few assumptions regarding the following:
		1. The id in the inventory/:id route needed to be an integer
		2. The "# of items vended" was an accumulation of all items vended and not the number of items per transaction (which is constrained to 1).

1. run git clone https://github.com/Dem-Eat-Rice/vend-o-matic.git
2. run pip install django && djangorestframework
3. run python manage.py makemigrations
4. run python manage.py migrate
5. run python manage.py createsuperuser 
6. run python manage.py runserver


