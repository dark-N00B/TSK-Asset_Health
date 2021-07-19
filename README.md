# TSK-Asset Health (WIP)

This is my first [SCADA](https://en.wikipedia.org/wiki/SCADA) project, built using [Django](https://www.djangoproject.com/download/) and [Python](https://www.python.org/downloads/windows/) as well as REST API

## How to compile this project

Install [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/)

Install [Pycharm](https://www.jetbrains.com/pycharm/download/) or [VS Code](https://code.visualstudio.com/)

on IDE terminal type -
```Shell
python manage.py runserver
```
or
```
python FusionChartsProject\manage.py runserver
```

# NOTICE

If you're using the same version of Python as mine (3.9), you won't face a Virtual Environment issue.
Otherwise, delete the "venv" folder and on IDE terminal type -
```Shell
python -m venv C:\Users\your_username\PycharmProjects\TSK-Asset_Health\venv\
```

If you're facing cx_oracle not being found error after creating new venv (or for any other reason),
on IDE terminal type -
```Shell
python -m pip install cx_Oracle --upgrade
```

Another quick note: If you're using PyCharm as the IDE for this project, it'll be better if you install Django and Cx-Oracle using Python Packages GUI in Pycharm!

### [Website](https://dark-n00b.github.io/TSK-Asset_Health/)
