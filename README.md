# Flashcard web app with spaced repetition

## Run app locally

To run the app on your local machine, navigate to the directory where you'd like the repository to be saved on your machine and clone the repository:

> `git clone https://github.com/lawsonpd/spaced_repetition_flashcards.git`  

Then create a [virtual environment](https://docs.python.org/3/tutorial/venv.html). This can be done in a few ways. [Conda](https://conda.io) manages virtual envs very well. Conda will create a directory inside your home directory where it will save virtual envs (created with Conda).

Create a virtual env with conda:

> `conda create -n <venv_name> python=3.10`  

where `venv_name` (omit the angle brackets) is whatever name you choose for this env.

Then activate the virtual env:

> `conda activate <venv_name>`  

To install the required packages into the virtual env you just created, navigate into the folder created by git and run

> `pip install -r requirements.txt`  


