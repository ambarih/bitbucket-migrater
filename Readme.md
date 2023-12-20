
# BITBUCKET MIGRATION API

It is very helpful to migrate the data from bitbucket server to bitbucket cloud.


## Documentation

### step1: 
Follow the below steps to use it as docker container


#### Clone the repo
```bash
  git clone https://git.altimetrik.com/bitbucket/scm/da/bitbucket_migrator.git
```
## Docker Application

To run this application as container


#### To build the image of an application
```bash
  docker build -t migration-app .
```
#### Create a network
```bash
  docker network create my-network
```
#### Run application using below command as container
```bash
  docker run -dp 5500:5500 --name migration-app --network my-network migration-app
```

#### Run bitbucket server using below command as container
```bash
  docker run -dp 7990:7990 --name bitbucket --network my-network atlassian/bitbucket
```
We must make sure the bitbucket server and bitbucket cloud up and running.

Enter the dynamic user input for server and cloud whichever is required field.



## step2:

### Run Locally
Clone the project

```bash
  git clone https://git.altimetrik.com/bitbucket/scm/da/bitbucket_migrator.git
```

Go to the project directory

```bash
  cd bitbucket_migrator
```
create an virtual environment

```bash
  python -m venv .env
```
activate the venv

```bash
  source .env/script/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python bitbucket.py
```
access the server

```bash
  http://localhost:5500/
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file
### for migration

for cloud

`workspace`

`username`

`password`

`bitbucket cloud url`

for server

`bitbucket server url with username and password`

`bitbucket server token`

#### for bitbucket server api call

to get

`bitbucket server url`
`bitbucket token`

to post and update

`bitbucket server url`
`username and password`

to delete because it will fetch projects and then delete

`bitbucket server url`
`bitbucket token`
`username and password`

#### for cloud api call
`bitbucket cloud url with username and password`
