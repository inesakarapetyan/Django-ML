# Django-ML
Machine Learning, Django


--------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                            DESCRIPTION                                                                                |
--------------------------------------------------------------------------------------------------------------------------------------------------------


This Django project integrates a machine learning model to provide predictions based on user input through a web interface. The project consists of the following main components:

-Django Web Framework: Manages the web application, including routing, views, templates, and static files.

-Machine Learning Model: A pre-trained model (e.g., a classifier or regressor) saved using a format like joblib or pickle.

-Integration: The Django backend loads the machine learning model and provides an form where users can submit data for prediction.





------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                            RUN CODE                                                                                |
------------------------------------------------------------------------------------------------------------------------------------------------------

For Windows Users

1.Open Visual Studio Code

2.Open Terminal:

Open the integrated terminal in VS Code by navigating to 'View > Terminal' or using the shortcut 'Ctrl + ~' (backtick).

3.py -m venv venv         # Create a virtual environment

4.\venv\Scripts\activate      # Activate the virtual environment

5.py -m pip install --upgrade pip    # Upgrade pip

6.pip install django    # Install Django

7.django-admin startproject myproject      # Create a Django project

8.cd myproject              # Navigate into the project directory

9.python manage.py startapp main   #Create a project

10.python manage.py runserver         # Start the Django development server

For Mac or Linux Users

1.Open Visual Studio Code

2.Open Terminal:

Open the integrated terminal in VS Code by navigating to 'View > Terminal' or using the shortcut 'Ctrl + ~' (backtick).

3.python3 -m venv venv             # Create a virtual environment

4.source ./venv/bin/activate            # Activate the virtual environment

5.python3 -m pip install --upgrade pip    # Upgrade pip

6.pip install django         # Install Django

7.django-admin startproject myproject     # Create a Django project

8.cd myproject              # Navigate into the project directory

9.python3 manage.py startapp main   #Create a project

10.python3 manage.py runserver         # Start the Django development server
