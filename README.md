# City Hospital

A Python Based Programme To USe Hospital Services 


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Python](www.python.org)
- [Mysql-connector-Python](https://pypi.org/project/mysql-connector-python/)
- [Mysql](https://dev.mysql.com/downloads/installer/)

### Installing

A step by step series of examples that tell you how to get a development
environment running

Create A Virtual Enviroment

    python -m virtualenv env

Install Mysql.connector

    pip install mysql-connector-python

Create A Database Named CityHospital 

    create database CityHospital;

Create The Tables And Insert Data Into It

      create table users(usernmae varchar(50),password varchar(50));
      create table doctors(name varchar(50));
      create table appointment(username varchar(50),doc_name varchar(50),D varchar(50));

### Creating A Connection

Establishe A Connection Between Python And Mysql,Replace The Password Field And Port Field In The Connection Part In Every Python File
For Default Mysql Installation Remove The Port Attribute From Code

    con=p.connect(host="localhost",user="root",password="yourpassword",port=8000,database="CityHospital")

In Order To USe Login You Need To Register A User First If Using For First Time 


## Running The Script

      python main.py

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license


## License

This project is licensed under the [MIT](LICENSE.md)


