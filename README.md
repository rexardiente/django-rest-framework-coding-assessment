# Django REST Framework Coding Assessment

### Task 1: Create a Django REST Framework project and app.

- Create a new Django project called “TestAPIProject."
- Create a new Django app called “TestUser.”

### Task 2: Create a Model

In the “TestUser” app, create a model called User with the following fields:

```
id (AutoField)
Name (CharField)
Birthday (DateTimeField)
Create and apply the migrations for this model.
```

### Task 3: Create a Serializer

In the “Test” User app, create a serializer called UserSerializer that serializes the User model.

### Task 4: Create API Views

- Create a view named UsersList that lists all users.
- Use the UserSerializer to serialize the data.
  `URL: /api/users/`
- Create a view called UserDetail that retrieves a single user by its id.
- Use the UserSerializer to serialize the data.
  `URL: /api/users/<int:pk>/`

### Task 5: Create API URLs

- Create URLs for the views you created in Task 4.
- Use the DefaultRouter from DRF for automatic URL routing.

## Running Django Development Server

`python manage.py runserver <port>` replace <port> with the port number you wish to use.
For example, if you want to run the server on port 8080, you would use:

```
$ python manage.py runserver 8080
# App will perform system checks..
# If no issues found, then it will run to default port *:8000
```

## Open Your Choice of Browser

Enter the URL http://localhost:8000/api/users/
It will response a GUI and that indicates your API is working correctly.

## Unit Test

TODO
