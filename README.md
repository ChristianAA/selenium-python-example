[![Daily Selenium UI Tests](https://github.com/ChristianAA/selenium-python-example/actions/workflows/daily-test.yml/badge.svg)](https://github.com/ChristianAA/selenium-python-example/actions/workflows/daily-test.yml)

# Selenium-Python-Example

This repository contains the base setup of an UI testing project,
using Python, Selenium Webdriver and Page Object Model pattern.

A simple search in DuckDuckGo to check that results are displayed is used as example

# Requirements

* Python 3.12.3
* pip (24.0) and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

Assuming python, pip and venv are installed correctly:

1. Download or clone this repository 
2. Open a terminal
3. Go to the project root directory "/selenium-python-example/".
4. Create a virtual environment: 
   - (UBUNTU): `python3 -m venv .venv`
   - (WINDOWS): `py -m venv venv`
5. Activate the virtual environment executing the following script: 
   - (UBUNTU): `source .venv/bin/activate`
   - (WINDOWS): `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`


# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/data/config.yaml" file

# Results

To check the report, open the '/results/report.html' file once the execution has finished.


# Links
   
   [Selenium - Python Documentation](<https://selenium-python.readthedocs.io/>)
   
   [Webdriver Manager for Python](<https://github.com/SergeyPirogov/webdriver_manager>)
   
   