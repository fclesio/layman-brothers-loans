# Layman Brothers Loans
Toy monolith that contains a RESTFul API, a Juypter Notebook server and a nice frontend blended by 
steamlit.

## Requirements 
- Docker Engine: 20.10.10 
- Docker Compose: 1.29.2
- macOS: Catalina 10.15.7+ / Ubuntu 18.05+ 

## Run locally via docker
```shell
docker run \
  -p 8888:8888 \
  -p 8000:8000 \
  -p 8503:8503 \
  mlopsde/layman-brothers-loans:latest \
  make start_services
```

## Project Structure
```
├── bin                    <- Standard subdirectory for executables that can be used inside 
│                             of a docker container
├── data                   <- Mandatory folderpydantic for all projects to store data locally
├── docs                   <- Miscellaneous documents, references, plots, etc. 
├── meta                   <- General info about the models and plots 
├── models                 <- Trained and serialized models, model predictions, ## Makefile Basic Usage
The current `Makefile` it's intended to have **dual-usage**. One using locally  
with some set of commands to generate a containerized environment, and another
to be executed inside the container. 

The rationale behind it is that once an Engineer place its code in the current
structure (_i.e._ placing the code in the `main` and `test` folder) it's possible
to run the same set of commands for any case (_e.g._ linting, testing, generating a 
new project).

Consolidate everything in a single `Makefile` helps us to keep a minimum amount of 
project standardization and remove any exotic configurations and/or project 
anti-patterns that can lead a harder debugability and reduce the engineers 
cognitive load during such kind of project.
│                             or model summaries
├── notebooks              <- Jupyter notebooks. No naming convention
├── src                    <- Source code for use in this project.
│   ├── logger             <- Small logging factory
│   ├── data_models        <- pydantic class for schema enforcement in the API call
│   ├── frontend           <- Streamlit application
│   ├── prediction         <- Module that loads the model for the API
│   └── main.py
│   └── model_training.py
│   ├── test               <- Folder that will contain all unit and integration tests
│   │   └── unit_test      <- This folder will store all unit tests and its modules
├── Makefile               <- Makefile with commands like `make init` or `make start`
├── README.md              <- The top-level README for developers using this project.
```

This project structure it's a lightweight version of the 
[Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) 
project. 


## Makefile Commands
### Host commands

All commands has it's own description in the help. Probably this is 
the most useful command:
```sh
make help
```

Start docker-container that setup the development
```sh
make start_dev_env 
```

Stop docker-container that setup the development
```sh
make stop_dev_env 
```

Push images to the docker registry:
```sh
make docker_push
```


### Container Commands
Start all services (I) Jupyter, (II) Frontend, (III): 
```sh
make start_services
```

Run all tests:
```sh
make tests
```
 




## Services
### RESTFul API

Swagger API: 
- http://0.0.0.0:8000/docs

Ping to check if the API is running: 
- http://0.0.0.0:8000/ping

API call: 
  ```sh
  curl -X 'GET' \
    'http://0.0.0.0:8000/ping' \
    -H 'accept: application/json'
  ```

Call to test if the model is working:

```sh
curl -X 'POST' \
  'http://0.0.0.0:8000/v1/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "limit_bal": 0,
  "education": 0,
  "marriage": 0,
  "age": 0,
  "bill_amt1": 0,
  "bill_amt2": 0,
  "pay_amt1": 0,
  "pay_amt2": 0
}'
```


### Jupyter Notebook
This image brings a Jupyter Notebook instance 
that will start an interactive jupyter server in the following host and port:

- http://0.0.0.0:8888/

The password for the jupyter notebook instance is `root`.


### Frontend
The frontend is powered by Streamlit and has a buch of sliders that can be used for a more real-life user
experience:

- http://0.0.0.0:8503/



## Makefile Basic Usage
The current `Makefile` it's intended to have **dual-usage**. One using locally  
with some set of commands to generate a containerized environment, and another
to be executed inside the container. 

The rationale behind it is that once an Engineer place its code in the current
structure (_i.e._ placing the code in the `main` and `test` folder) it's possible
to run the same set of commands for any case (_e.g._ linting, testing, generating a 
new project).

Consolidate everything in a single `Makefile` helps us to keep a minimum amount of 
project standardization and remove any exotic configurations and/or project 
anti-patterns that can lead a harder debugability and reduce the engineers 
cognitive load during such kind of project.