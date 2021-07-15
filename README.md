# POST GITHUB USER REPOSITORIES IN AZURE

This project makes a search for github users repositories and post to an Azure SQL Database.

## Pre-requisites
You must have a existing Azure account with a SQL Database created.

## Installation

- Clone the repository
- Install _requests_ library using pip:
``` 
pip install requests
```
- Install _pyodbc_ library using pip:
``` 
pip install pyodbc
```

## Running the code

- Open the project folder in a development tool
- Run the code using Python compiler

The interface asks for a Github username and print the existing repositories:
```
>>> Type the GitHub username to list his repositories and store them in a Azure SQL Database: {username}

>>> {username} repos: 
    ...
    ...
    ...
```    
    
After that, it will ask for your Azure username, password, server name and database name:
```
>>> --Enter your Azure username and password--
>>> Username:
>>> Password:

>>> --Enter your Azure server and database name--
>>> Server name:
>>> Database name:
```

Then it will try to create a new table in the given database and insert the repos data:
```
>>> Trying to create new table and inserting repos id's, names and URLs to Azure SQL Database...
```

If everything goes right, the interface will print the following message:
```
>>> Succesfully inserted data in Azure Database! :)
```


## More information

You can access the _Requests_ library documentation [here](https://requests.readthedocs.io/en/master/)

You can access the _Pyodbc_ library documentation [here](https://github.com/mkleehammer/pyodbc/wiki)

You can watch [this video](https://www.youtube.com/watch?v=_Xr_SxDeub4) on Youtube, to learn how to properly connect to Azure using _pyodbc_ library if any connection error occurs.
