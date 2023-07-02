# eventmanagement_grewon

<!-- Please follow the below steps to set-up the project -->
1. clone the project using `git clone git@github.com:jaychovatiya4995/eventmanagement_grewon.git`

2. create virtul enviourment using `python -m venv env`

3. Activate the virtul enviourment using command `source env/bin/activate`

4. move to project directory ../eventmanagement/

<!-- Set up the database schema Run Below Command -->
5. python manage.py migrate

6. Load the user data run command `python manage.py loaddata events/fixtures/users.json

`. This will add some users in your db for testing purpose only, you can replace it with actual.`

7. Now, Add the Event for the User. after adding the events for the users check user aviability using api `127.0.0.1:8000/events/available-user/`
