Welcome to the Pilot Logbook!

Pilots can sign up for an account, log in and add a profile photo. Their account details would include:
* First name
* Last name
* Email address
* Aviation reference number
* Licence type
* Ratings

And of course they would be able to add flights to their logbook including:
* Date
* Aircraft type
* Aircraft registration
* Pilot in command
* Other pilot or crew
* IATA airport codes
* Single or multi-engine
* Hours

## Installing and Running Pilot Logbook

### System Requirements

* UN*X operating system, such as Linux or MacOS

    OR
* Windows operating system with Linux Bash Shell

* Python
* Python PIP
* PostgreSQL
* A web browser, e.g. Chrome, Firefox, Microsoft Edge or Safari.

### Installation

1. Clone this repository to a directory on your hard drive.
2. Open the terminal shell and navigate to the directory containing this program.
3. Create a DB User and password and add to the .env file
4. Create and activate a venv
5. ```pip install -r requirements.txt```
6. ```psql postgres```
7. ```CREATE DATABASE logbookdb;```
8. ```\q```
9. ```flask db-custom create```

### Running the Program

1. Open the terminal shell and navigate to the directory containing this program.
2. The enter the following text and press Enter/Return: ```./run.sh```. This will activate your venv and run Flask.
3. In your browser, navigate to http://127.0.0.1:5000/