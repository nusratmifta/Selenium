

# Setup Instructions

## Python Setup


Here we need Python 3.8 or higher.


Here we need to run code in pip environment instead of Powershell.
To install pip environment, run `pip install pipenv` from the command line.


## WebDriver Setup

For Web UI testing, you will need to install the latest versions of webdriver (Chrome, firefox, Explora)


### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the *Path* environment variable. (on cmd search "view advance system settings -> Environment variables -> System Variables(PATH) -> Edit -> New")

# For setting virtual environment
If Pipfile and Pipfile.lock avaiable in your folder just delete these.
Then in the folder open cmd by clicking on the path.
$pipenv install
$pipenv install requests
$pipenv install selenium

### To run test case
Firstly we need to install pytest.
Before this in the terminal we need to change PowerShell to pipenv by running $pipenv shell,
$pipenv install pytest

$pipenv run python -m pytest

### To run test case using Parallel testing
Firstly we need to install pytest xdist using $pipenv install pytest-xdist
$pipenv run python -m pytest -n 3  [this is the number of test case]
