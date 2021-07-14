import textwrap
import pyodbc
import psycopg2
import list_repos

if (list_repos.repo_qty != 0):

    list_repos.username = list_repos.username.replace('-', '')

    print("\nInserting repos id's, names and URLs to a Azure SQL Database...\n")

    # DRIVER SPECIFIED
    driver = '{ODBC Driver 17 for SQL Server}'

    # SERVER NAME AND DATABASE NAME
    server_name = 'viniciussilva-server'
    db_name = 'vinicius_silva_DB'

    # CREATING SERVER "URL"
    server = f'tcp:{server_name}.database.windows.net,1433'

    # DEFINE USERNAME & PASSWORD
    username = 'vinicius98'
    password = 'SQLvinny1998'

    # CREATING THE FULL CONNECTION STRING FOR AZURE
    connection_string = textwrap.dedent(f'''
        Driver={driver};
        Server={server};
        Database={db_name};
        Uid={username};
        Pwd={password};
        Encrypt=yes;
        TrustServerCertificate=no;
        Connection Timeout=30;
    ''')

    # CREATING PYODBC NEW CONNECTION OBJECT AND NEW CURSOR
    conn: pyodbc.Connection = pyodbc.connect(connection_string)
    cursor: pyodbc.Cursor = conn.cursor()

    # DEFINE NEW SQL QUERIES AND EXECUTING THEM
    try:
        cursor.execute(f'''CREATE TABLE {list_repos.username}_repos (id VARCHAR(50) PRIMARY KEY, repo_name VARCHAR(50), URL VARCHAR(255));''')

        for i in range(list_repos.repo_qty):
            cursor.execute(f'''INSERT INTO {list_repos.username}_repos (id, repo_name, URL) VALUES ({list_repos.id_list[i]},'{list_repos.repo_list[i]}','{list_repos.url_list[i]}');''')

        print('\nSuccesfully inserted data in Azure Database! :)\n')
    except Exception as e:
        print('''\n\n
        ERROR: We couldnt create a new table for this particular user :(
        Maybe the table already exists in this Azure Database, or the user doesnt exists...
        Try again by typing another GitHub username.
        \n''')

    # CLOSING AND COMMITING THE CONNECTION WHEN DONE
    conn.commit()
    cursor.close()
    conn.close()

else:
    print(f'''\n\n
    ERROR: Could not connect to Azure using the requested user '{list_repos.username}' repositories.
    Maybe this github user doesnt have any repository or it doesnt exists.\n''')
