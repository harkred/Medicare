# Medicare
## Description
This is a medicine recording website where clients can create an account and record the dosage of a particular meds they need to take along with their desired frequency. The back-end of this website has been implemented via django and it lacks a front-end. As for database, its currently relying on sqlite3 to store all the necessary data. Sqlite3 was choosen because it is automatically implemented by django.

This website has not been hosted yet but will be hosted later. For now follow down all the necessary instructions on how to run this website on your local machine and also use it.

## Installing necessary dependencies
This section assumes that you have python 3.10 or above already installed on your local machine with necessary pip configurations.

To install necessary dependencies, the python virtual environmnet specific to this project must be activated. This virtual environment has all the necessary dependencies that is needed to run this program.

To activate the the virtual environment, first traverse to medicare directory via `cd medicare` command. Then use the following command to activate your virtual environment.

`.\Scripts\activate`

After activating the virtual environment, all the necessary dependencies will be installed on your local machine.

To run this website on your local machine, enter the following command.

`python manage.py runserver`

This should provide you with a localhost server link where the website is being hosted on your machine. Click on it and enjoy messing around with the website.