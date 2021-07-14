# GET GITHUB USER REPOSITORIES

This project makes a search for github users repositories and post to an Azure SQL Database.

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

```
The interface asks for a Github username:

>>> Type the GitHub username to list his repositories and store them in a Azure SQL Database: {username}

>>> {username} repos: 
    ...
    ...
    ...
    
>>> Inserting repos id's, names and URLs to a Azure SQL Database...

If everything goes right, the interface will print the following message:

>>> Succesfully inserted data in Azure Database! :)

Otherwise, it will print this:

>>> ERROR: We couldnt create a new table for this particular user :(
    Maybe the table already exists in this Azure Database, or the user doesnt exists...
    Try again by typing another GitHub username.
    
And if you type in the begginning of the code a username that doesn't exists or doesn't have any repos in GitHub, 
this is the message that you will receive:

>>> ERROR: Could not connect to Azure using the requested user '{username}' repositories.
    Maybe this github user doesnt have any repository or it doesnt exists.
```

## More information

You can access the _Requests_ library documentation [here](https://requests.readthedocs.io/en/master/)

You can access the _Pyodbc_ library documentation [here](https://github.com/mkleehammer/pyodbc/wiki)

You can watch [this video](https://www.youtube.com/watch?v=_Xr_SxDeub4) on Youtube, to learn how to properly connect to Azure using _pyodbc_ library if any connection error occurs.
