# Questioner-ch3
A web application that helps meetup organizers prioritize questions to be answered.

A web application that helps meetup organizers prioritize questions to be answered

**This application should have the following api endpoints working.**

**Question Endpoints**

| Method | Endpoint | Function |
| ------ | ------ |------ |
| GET | /api/v1/questions | Fetches all question records
| GET | /api/v1/questions/questionId | Fetches a specific question record
| GET | /api/v1/rsvp/rsvpId | Fetches a specific rsvp record
| POST | /api/v1/questions | Creates a question record
| PATCH | /api/v1/questions/questionId/upvote | Increments a questions' votes by 1
| PATCH | /api/v1/questions/questionId/downvote | decrements a questions' votes by 1
| DELETE | /api/v1/questions/questionId | deletes a specific meetup record

**Meetup endpoints**

| Method | Endpoint | Function |
| ------ | ------ |------ |
| POST | /api/v1/meetups | Creates a meetup record
| GET | /api/v1/meetups/upcoming | Fetches all meetup records
| GET | /api/v1/meetups/meetupId | Fetches a specific meetup record
| PUT | /api/v1/meetups/meetupId | Updates a specific meetup record
| DELETE | /api/v1/meetups/meetupId | deletes a specific meetup record

**RSVP Endpoints**

| Method | Endpoint | Function |
| ------ | ------ |------ |
| POST | /api/v1/rsvp | Creates an rsvp record
| PUT | /api/v1/questions/questionId | Updates a specific question record
| PUT | /api/v1/rsvp/rsvpId | Updates a specific rsvp record
| DELETE | /api/v1/rsvp/rsvpId | deletes a specific rsvp record

## Getting Started

**Prequisites**

Ensure you have

* Python3 installed
* Postman

### Installing 

1. **Clone this repository.**
```
https://github.com/SolomonMacharia/Questioner-ch3.git
```
2. **Create a virtual environment**
```
python3 -m venv env/path/to/new/virtual/environment
```
3. **Activate the virtual environment**
```
source yourvirtualenvironment/bin/activate
```
4. **Install the required dependancies**
```
pip install -r requirements.txt
```
```
pip freeze > requirements.txt
```
5. **Export the contents in the .env file**

In your terminal run all settings in the .env file as follows
```
export some/flask/setting
```
6.**Run the application**

Simply run in the command line,
```
flask run
```
**Using either Postman/ Insomnia:**

Run the above endpoints to test that they are functioning as expected:

## Running the tests

To run the tests in the **command line**, use either:

>`python tests.py` ,

Runs unittest

or

>`nosetests`

Runs nosetest

or

>`nosetests -v`

Runs nosetests in verbose
```

or simply
```
`pytest`

## Deployment
To deploy the app, create an account on Heroku and follow the steps given to deploy the app.

## Built with
 * Python v.3.6
 * Flask v.1.02

## Authors

* **Solomon Macharia** - *Initial work*

# License

This project is buuild underthe MIT licence - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* Team3 Members

* NBO-36 Team 
