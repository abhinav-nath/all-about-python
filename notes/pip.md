# General pip commands

- Upgrade pip

  `pip install --upgrade pip`


- Output installed packages in requirements format

  `pip freeze`


- Install a library

  `pip install <library-name>`

  for ex :
  - `pip install flask`
  - `pip install Flask-RESTful` - this will install flask as well


- Create a virtual Python environment

  * `pip install virtualenv` - this will install virtualvm

  * this will create a folder named `venv` and keep `python 3.5` inside it
    - `virtualenv venv --python=python3.5` (Linux)
    - `./venv/Scripts/activate.bat` (Windows)

  * `source venv/bin/activate` - this will activate the venv

  * `python --version` - verify Python's version in the venv
