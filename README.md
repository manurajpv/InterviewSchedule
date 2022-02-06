# Interview Time Schedule using Django

  Interview Time Schedule app build using Python Django framework. Interview time slots can be registered by the candidates and Interviewer. The slots corresponding to an Interviewer and the Candidate can be found by the Registered IDs.


## Steps to install
  - Clone the Repository to your local disk.
  - Create and start the [Python virtual environment](https://docs.python.org/3/library/venv.html).
  - Go to the ITS folder and install the python reqirements by running ```pip3 install -r reqirements.txt```.
  - Initialize the Database by running ```python3 manage.py migrate```.
  - Initialize the static files by running ```python3 manage.py collectstatic```.
  - Start the development server by running ```python3 manage.py runserver```.