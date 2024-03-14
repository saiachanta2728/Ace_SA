Setting Up Virtual Environment
Install virtualenv: If you haven't already installed virtualenv, you can install it using pip:

bash
Copy code
pip install virtualenv
Create a virtual environment: Navigate to your project directory and create a virtual environment:

bash
Copy code
virtualenv venv
Activate the virtual environment: Activate the virtual environment based on your operating system:

Windows:
bash
Copy code
venv\Scripts\activate
Linux/macOS:
bash
Copy code
source venv/bin/activate
Managing Packages
Installing packages: Inside the activated virtual environment, install packages using pip:

bash
Copy code
pip install <package-name>
Listing installed packages: You can list all installed packages in the virtual environment:

bash
Copy code
pip freeze
Saving dependencies to a file: Save the list of installed packages to a requirements.txt file:

bash
Copy code
pip freeze > requirements.txt
Installing dependencies from a file: Install dependencies listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Deactivating the Virtual Environment
To deactivate the virtual environment and return to the global Python environment, simply type:

bash
Copy code
deactivate
