To start server use:

python manage.py runserver

To test API use CURL Command:

curl -X POST 'http://127.0.0.1:8000/model/detect/' -d 'url=https://pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg' ; echo ""
