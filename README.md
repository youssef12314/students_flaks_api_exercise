# Students Flaks api exercise
How to use:

Run ```python app.py``` to start the Flask server.

You can use tools like ```Postman``` or ```curl``` to interact with your API:

* ```POST /students``` to add a new student.
* ```GET /students``` to list all students.
* ```GET /students/<id>``` to get a specific student.
* ```PUT /students/<id>``` to update a specific student.
* ```DELETE /students/<id>``` to delete a specific student.

Structure of a student:

```
{
    "id": 1234,
    "name": "Claus",
    "age": 23,
    "grade": 12
}

```

## Exercise
The code in this repository creates a Flask rest api. The code is developed in an older version of Flask than the newest one avaliable. So when you install the dependencies (Flask and Flask-SQLAlchemy and Werkzeug) you will not be able to run the app. Your job is to first try to run it a see it fail, then fix the dependency issues, and then fix the repository so that future users of the application will have the right versions of the dependencies from the beginning. 

### Run the app and se it fail.
1. Open this repository (clone it or in Codespaces).
2. Run it by typing the command ```Python app.py```
3. Install the missing dependencies (your terminal tells you wich is missing)
4. Run the app again.

You will now get errors telling that some attributes is not defined.

### Install the right version of the dependencies
The problem with the dependencies, is that a new major version of Flask and Flask-SQLAlchemy has been released since the development of this Students api application. At the moment it is Flask version 3.x.x and the one used in this application is 2.x.x.

1. Run the commands:

``` 
    pip install Flask==2.1.2 Werkzeug==2.1.1 SQLAlchemy==2.0.23
``` 

2. Run the app again by typing the command ```Python app.py```

Now your application should work and you can see it in the browser.

### Create a requirements.txt file
In order for others not to have to do the steps you just performed every time they clone the repository, you need to fix this repository by making a ```requirements.txt``` file containing the apllication dependencies. When this is done users of the repository could just open it in Codespaces and then the right dependencies will automatically be installed. If someone wants to run the code more locally, the dependencies can be installed with the command ```pip install -r requirements.txt``` 

1. Write the command ```pip freeze > requirements.txt``` 

This will create a requirements.txt file in the folder.

2. Open the requirements.txt file and have a look at what´s in the file. 
3. add, commit and push your changes (this will create a fork in your own repository)
4. Delete the Codespace
5. Merge your branch into the master branch
6. Open a Codespace from your version of the project.

This should open a version with the right dependency versions installed.

7. Run the app again by typing the command ```Python app.py```

Hopefully this works for you, and for everybody in the future.








 
