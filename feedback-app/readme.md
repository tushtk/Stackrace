## Python Feedback App

A Simple web based application written in Python hosted in heroku 



### Challenges

1. Buildpack not loading correctly for python. Not detecting dyno 
 
 
<br>

1. pipenv install flask-sqlalchemy
2. pipenv shell

3. pip freeze > requirements.txt

4. heroku buildpacks:clear

5. heroku buildpacks:set heroku/python

6.  heroku ps:scale web=1
 
 1. pushing code to heroku  - git push heroku main



## Pipenv

### Custom Indexes
Until Pipenv it was difficult to use private Python repositories, for example if you’d like to host private Python libraries within your organization. Now all you need to do is define them as an additional sources in the Pipfile:


[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[[source]]
url = "https://www.example.com"
verify_ssl = true
name = "some-repo-name"

[packages]
django = "*"
my-private-app = {version="*", index="some-repo-name"}

[dev-packages]

[requires]
python_version = "3.7"


>Notice that we told my-private-app to use the private repo. If omitted, Pipenv will cycle through indexes until it finds the package.



### Deploying
When deploying it’s important that your deploy fails if there’s a mismatch between installed dependencies and the Pipfile.lock. So you should append --deploy to your install step which does just that:

> $ pipenv install --deploy

You could also check which dependencies are mismatched:

> $ pipenv check

And see which sub-dependencies are installed by packages:

> $ pipenv graph --reverse


> $ pipenv run python manage.py runserver
