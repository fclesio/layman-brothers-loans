
## Machine Learning Project Template
This template comes to solve a need to have a containerized environment for model 
training and batch processing.

A containerized environment will save an estimated amount of time related to
debugging any broken jobs plus will promote a standardized approach that can be used
to run data/ML jobs in other runtime platforms as SageMaker, kubernetes, AWS Batch etc.

## Requirements 
- Docker Engine: 20.10.10 
- Docker Compose: 1.29.2
- macOS: Catalina 10.15.7 or later


## Project Structure
```
├── bin                    <- Standard subdirectory for executables that can be used inside 
│                             of a docker container
├── Makefile               <- Makefile with commands like `make init` or `make start`
├── README.md              <- The top-level README for developers using this project.
├── data                   <- Mandatory folder for all projects to store data locally
├── docs                   <- Miscellaneous documents, references, plots, etc. 
├── models                 <- Trained and serialized models, model predictions, 
│                             or model summaries
├── notebooks              <- Jupyter notebooks. No naming convention
├── src                    <- Source code for use in this project.
│   ├── main               <- Folder where all code and modules will be placed
│   │   └── main.py        <- Script that will contain the main() guard to be the 
│   │                         entrypoint of any execution
│   ├── test               <- Folder that will contain all unit and integration tests
│   │   └── unit_test      <- This folder will store all unit tests and its modules
│   │       └── tests.py   <- Unit tsting script 
```

This project structure it's a lightweight version of the 
[Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) 
project. 




## Basic Usage
#### Makefile 
The current `Makefile` it's intended to have dual-usage. One using locally  
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


#### Environment Variables
We're not going to be super opinionated in terms of environment variables
but since the main usage will be to use in dockerized environment in our
infrastructure or in AWS SageMaker and AWS Batch, it's recommended to use
the current set of variables in the ``.env`` file:

```bash
AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY
AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
AWS_DEFAULT_REGION=AWS_DEFAULT_REGION
DB_REDSHIFT_USER=DB_REDSHIFT_USER
DB_REDSHIFT_HOST=DB_REDSHIFT_HOST
DB_REDSHIFT_PASS=DB_REDSHIFT_PASS
DB_REDSHIFT_PORT=DB_REDSHIFT_PORT
DB_REDSHIFT_NAME=DB_REDSHIFT_NAME
```

#### Jupyter Notebook
This image brings a Jupyter Notebook instance that will start an interactive jupyter 
server in the following host and port:

- http://0.0.0.0:8888/

Small note that right now the only port option is only the ``8888`` but you can change it
in the ``docker-compose.yml``:
```yaml
    ports:
      - 8888:8888
```

The password for the jupyter notebook instance is `root`.

#### Host Commands
Init a new project in your local environment
```sh
make PROJECT=nuclear init
```

Start to work
```sh
make start
```

Stop the work
```sh
make stop
```

Push local image to ECR
```sh
make ecr_push
```

#### Container Commands
Automatic linting
```sh
make lint
```

Unit testing
```sh
make tests
```




### Change Log
#### v0.01
- [x] Comments in the PR
- [x] Include in the readme the creation of ``.env`` file
- [x] Include ``root`` password in the readme
- [X] Change to `push`
- [X] include main logging library
- [X] Metrics and txt with the metrics inside of docs folder inside of the volume
- [X] Ensure that the ``ecr_push.sh`` replaces the `ml_template` name

#### v0.02
- [ ] Single name for the project in docker container
- [ ] Investigate the size for the push and the final image
- [ ] Set jupyter in docker compose as ``y`` by default
- [ ] include options for execution

#### v0.03
- [ ] yaml file for batch job configuration and hardware spec (serveless-batch.yaml)
- [ ] See if worth to package on pip and bootstrap everything in a single command for environment creation
- [ ] Set ``meta.json`` to collect the model metrics, version, other metadata with SHA hash and so on. 
  Ideally use it in integration tests
- [ ] Set some mechanism for model registry  

#### v0.04
- [ ] Experimentation and reproducibility in the codebase
- [ ] Model registry and artifact management
- [ ] Options to change which port jupyter notebooks get exposed at, so we can run several containers in parallel
