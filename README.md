# VoiceCloner_Task
pip install -r requirements.txt

Python3 manage.py runserver 

The API url path is http://127.0.0.1:8000/api/schema/docs/.

I use Swagger for API documentation.

Sign up and Login the system with Django RestFramework.

I use a simple SQLite database but you can change it to Postgresql database. You can just create your PostgreSQL database in pgAdmin and change the DATABASE in ssetting.py.

run pytest command to run the test

You can use the REST Client extension in VSCode to run API_endpoint_test.rest to test APIs.Link https://marketplace.visualstudio.com/items?itemName=humao.rest-client
