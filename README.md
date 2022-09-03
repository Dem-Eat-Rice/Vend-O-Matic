# vend-o-matic

1. run git clone https://github.com/Dem-Eat-Rice/vend-o-matic.git
2. run pip install django && djangorestframework
3. run python manage.py migrate
4. run python manage.py createsuperuser 
(not sure if you'll need this for tests, but there's no formal database as Django has a built-in dev database *talk about efficient*)
	- create your login credentials 
	- access localhost:8000/admin in browser
	- In the 'Vending machines' table
		- insert a table entry named "GoodYear Tire Lobby"
	- In the 'Beverages' table
		- insert an table entry for each of the following names: Soda, Water, Juice && Set each of their "Machine" fields to the "GoodYear Tire Lobby"
5. run python manage.py runserver
