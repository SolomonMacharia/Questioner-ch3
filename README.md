# Questioner-ch3

[![Build Status](https://travis-ci.org/SolomonMacharia/Questioner-ch3.svg?branch=develop)](https://travis-ci.org/SolomonMacharia/Questioner-ch3)
[![Coverage Status](https://coveralls.io/repos/github/SolomonMacharia/Questioner-ch3/badge.svg?branch=develop)](https://coveralls.io/github/SolomonMacharia/Questioner-ch3?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f92e237be6e37d1edbf1/maintainability)](https://codeclimate.com/github/SolomonMacharia/Questioner-ch3/maintainability)



A web application that helps meetup organizers prioritize questions to be answered.

A web application that helps meetup organizers prioritize questions to be answered

**This application should have the following api endpoints working.**

**Question Endpoints**

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/7f9c41ed06a08cadc841)

| Method | Endpoint | Function |
| ------ | ------ |------ |
| GET | /api/v1/questions | Fetches all question records
| GET | /api/v1/questions/questionId | Fetches a specific question record
| POST | /api/v1/questions | Creates a question record
| PATCH | /api/v1/questions/questionId/upvote | Increments a questions' votes by 1
| PATCH | /api/v1/questions/questionId/downvote | decrements a questions' votes by 1

**Meetup endpoints**

| Method | Endpoint | Function |
| ------ | ------ |------ |
| POST | /api/v1/meetups | Creates a meetup record
| GET | /api/v1/meetups/upcoming | Fetches all meetup records
| GET | /api/v1/meetups/meetupId | Fetches a specific meetup record
| DELETE | /api/v1/meetups/meetupId | deletes a specific meetup record

**RSVP Endpoints**

| Method | Endpoint | Function |
| ------ | ------ |------ |
| POST | /api/v1/rsvp | Creates an rsvp record


**using the `POST` question endpoint**

To test the **api/v1/questions** endpoint, use a payload in the following format.

 ```
            payload = {
                'meetupId': int,
                'title': 'title',
                'body': 'body
            }
```

**using the `POST` meetup endpoint**

To test the **api/v1/meetups** endpoint, use a payload in the following format.

 ```
            payload = {
                "images": "images",
                "location": "The venue",
                "tags": [
                    "tag1",
                    "tag2",
                    "tag3"
                ],
                "topic": " "
            }
```

**using the `create` rsvs  endpoint**

To test the **api/v1/meetups/meetupId/rsvs** endpoint, use a payload in the following format.

 ```
            payload = {
                "meetupId": 343,
                "topic": "topic",
                "status": "status"
            }
```

**using the `register` user endpoint**

To test the **api/v1/users** endpoint, use a payload in the following format.

 ```
            payload = {
                "email": "email",
                "password": "password",
                "confirmPassword": "password"
            }
```

## Getting Started

**Prequisites**

Ensure you have

* Python3 installed
* Postman

### Installing 

1. **Clone this repository.**
```
https://github.com/SolomonMacharia/Questioner.git
```
2. **Create a virtual environment**
```
python3 -m venv env
```
3. **Activate the virtual environment**
```
source env/bin/activate
```
4. **Install the required dependancies**
```
pip install -r requirements.txt
```
```
pip freeze > requirements.txt
```

5. **Development environment variables**
```
export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_DEBUG=1
```
6.**Run the application**

```
flask run
```
**Using either Postman/ Insomnia:**

Run the above endpoints to test that they are functioning as expected:

## Running the tests

simply run

`pytest`

## Deployment

To deploy the app, create an account on Heroku and follow the steps given to deploy the app.

**App Demo**

[Heroku Demo](https://git.heroku.com/bootcamp-questioner.git)


## Built with
 * Python v.3.6
 * Flask v.1.02

## Authors

* **Solomon Macharia** - *Initial work*

# License

This project is built under the MIT licence - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* Team3 Members

* NBO-36 Team 
