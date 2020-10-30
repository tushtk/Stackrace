pipenv install flask-sqlalchemy
pipenv shell



heroku buildpacks:clear

heroku buildpacks:set heroku/python

 heroku ps:scale web=1