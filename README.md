# Basic FastAPI - Graphql CRUD

This repository contains a simple CRUD (Create, Read, Update, Delete) application built with FastAPI and GraphQL. It's a easy way to create a basic API for managing data using FastAPI's powerful features and GraphQL for querying and manipulating data. This API uses a JWT (Json Web Token) to authenticate requests.
  
## Prerequisites
Make sure you have the following prerequisites installed:

- Python (3.7+)
- Pip (Python package manager)
- Existing Postgresql database

## Installing Dependencies
1. Clone this repository to your local machine:  
   `git clone https://github.com/mariomtzjr/fastapi_graphql.git`  
   `cd fastapi_graphql`

2. Install the project dependencies:  
    `pip install -r requirements.txt`

## Run the app
1. Execute the following command:  
   `python main.py`
2. Open a web browser or use a tool like GraphiQL to interact with the GraphQL API, url where app is running:
   - http://localhost:8000/graphql

## Usage
You can use the GraphQL API to perform CRUD operations on the data. Refer to the GraphQL schema documentation for available operations.