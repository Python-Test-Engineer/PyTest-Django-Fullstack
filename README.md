# Django Testing Framework

### SETUP

- ### cd TEST_SUITE_DJANGO.
- ### creater virtual env `python -m venv venv`.
- ### pip install -r requirents.txt
- ### run `playwright install` to load in playwright browsers.
- ### in one terminal run `python manage.py runserver`.
- ### For unittests run `python manage.py test`
- ### in another run `python -m pytest -v` or `python -m pytest -v --headed` if using  playwright and you want to see browsers. Sometimes this may not work so you will need to add the headless=False to the test.
- ### DB has had migrations. superuser: admin password
- ### superuser is admin/password
- ### pytest-sugar added for fancier terminal output
- ### PyBoxen used for fancy console output. Examples are in the orm app.
- ### django-extensions used in orm app so that we can run scripts in a py file rather than in shell. See `orm/_NOTES.md` for more details.

DJANGO_SETTINGS_MODULE = core.settings where core is the base app initially created with startproject must be added to pytest.ini

## If one is not using requirements.txt one would need to install:

- ### django
- ### django-extensions for the utuilities used in orm.
- ### pytest, pytest-django, pytest-cov.
- ### playwright for browser based testing (an then run `playrwight install` to load browsers).
- ### pytest-sugar for nicer output format of tests.
- ### rich and pyboxen for fancy console output used in orm.
- ### requests for order app.

### Tests

- ### (Windows) You can also get PyTest to run unittests in dDjango apps `python -m pytest .\ ` where .\ is the root of the project or you can use ` python -m pytest -vs .\posts` for a particular app. 

python -m pytest -vs .\posts\tests_posts -vs
python -m pytest -vs .\filemanager\tests_filemanager -vs
python -m pytest -vs .\ecommerce\tests_ecommerce -vs
python -m pytest -vs .\catalog\tests_catalog -vs
python -m pytest -vs .\accounts\tests_accounts -vs
## REFERENCES

- ### Pybites - https://www.youtube.com/watch?v=L5jWFU2sVXQ for help with setting up PyTest tests for Django. 

- ### Ssali Jonathan - https://www.youtube.com/watch?v=Nn3Yjea5KCI&list=PLEt8Tae2spYlVZUBBEE9PtX-NXk_hw7o4 for the TDD approach to building the `posts` app. This gives a basis for many good tests. I have transported a few for demonstation purposes in `pytest_tests`. (PyTest searches for all test files with test_ or whatever is specified in the pytest.ini file in root).

## Other resources

### These will use their own individual app to showcase them.

- ### DjangoStars - https://djangostars.com/blog/django-pytest-testing/

- ### https://pytest-with-eric.com/pytest-advanced/pytest-django-restapi-testing/#Conftest-and-Setup

- ### https://dev.to/sherlockcodes/pytest-with-django-rest-framework-from-zero-to-hero-8c4


