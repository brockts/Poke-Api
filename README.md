# Proyecto PokeAPI

A RESTful API built with Django to retrieve data from the [PokeAPI](https://pokeapi.co/docs/v2).

<br/>

<div align="center">
	<img height="200" src="pokeapi.svg" alt="PokeAPI">

<br/>

</div>

<br/>

PokeAPI
A RESTful API built with Django to retrieve data about Pokemon.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You need to have Python and pip installed on your machine to run the API.

Installing
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/pokeapi.git
Navigate to the project directory:
bash
Copy code
cd pokeapi
Create a virtual environment and activate it:
bash
Copy code
python -m venv env
source env/bin/activate
Install the required packages:
Copy code
pip install -r requirements.txt
Migrate the database:
Copy code
python manage.py migrate
Run the development server:
Copy code
python manage.py runserver
The API will now be available at http://127.0.0.1:8000/.
Endpoints
The API has the following endpoints:

/pokemon/: returns a list of all Pokemon in the database.
/pokemon/<id>/: returns the detail view for a specific Pokemon with the given id.
Built With
Django - The web framework used
Django Rest Framework - Used for building the RESTful API
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

Authors
Your Name - Initial work - Your Github