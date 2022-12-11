This project is based on the bakery management model. BakeryAdmin can do crud operation like add item, delete item, edit item and can also see the order history. 
Customer can register and login, see item name and price and place order accordingly.

BakeryAdmin is the project folder and api is the app folder.

For registration we have to use Postman and paste this url "http://127.0.0.1:8000/api/v1/register/" and use bodytype JSON for Username and Password.

For login we have go to url "http://127.0.0.1:8000/api-token-auth/" and use bodytype JSON for Username and Password.

Login and Registration are done using POST method in Postman.

For admin to access bakery "http://127.0.0.1:8000/api/v1/bakery/" , here he can get, delete, modify, add item, delete item for bakery.

TO access SuperUser username = "shivam", Password = "123".

For customer url "http://127.0.0.1:8000/api/v1/customer/" .
