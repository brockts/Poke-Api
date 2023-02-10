# Proyecto PokeAPI
<br/>

<div align="center">
	<img height="200" src="https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi.svg?sanitize=true" alt="PokeAPI">

<br/>

</div>

<br/>

## Description

A RESTful API built with Django to retrieve data from the [PokeAPI](https://pokeapi.co/docs/v2).


## Environment Variables

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
You need to have Python and pip installed on your machine to run the API.

## Installing

Clone the repository to your local machine:

```bash
    git clone https://github.com/your-username/pokeapi.git
```

## Go to the project directory

```bash
  cd POKE-API
```

## Create a virtual environment and activate it:

```bash
    python -m venv env
    source env/bin/activate
```

## Install the required packages:

```bash
    pip install -r requirements.txt
```

## Migrate the database:
```bash
    python manage.py migrate
```

## Run the development server:
```bash
    python manage.py runserver
```

### The API will now be available at http://127.0.0.1:8000/.

## Urls:
	`pokemon/`, views pokemon all
	`pokemon/<int:id>/`, views pokemon by id
	`pokemon/<str:name>/`, views pokemon by name
	`pokedex/`,views all pokedex
	`pokedex/<str:name>/`, wviews pokedex by name

## Authors

- [Ian Flores](https://github.com/Ianskev)
- [Sebastian Arquinigo](https://github.com/sebas0303)


