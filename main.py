import textwrap
import pyodbc
import list_repos

main_exit = False
while main_exit is False and list_repos.list_exit is False:
    if (list_repos.repo_qty != 0):

        list_repos.username = list_repos.username.replace('-', '')
        wish = ''

        # DEFINE AZURE USERNAME & PASSWORD
        print("--Enter your Azure username and password--")
        username = input('Username: ')
        password = input('Password: ')

        # DEFINE AZURE SERVER NAME AND DATABASE NAME
        print("\n--Enter your Azure server and database name--")
        server_name = input('Server name: ')
        db_name = input('Database name: ')

        # SPECEFYING DRIVER AND CREATING SERVER "URL"
        driver = '{ODBC Driver 17 for SQL Server}'
        server = f'tcp:{server_name}.database.windows.net,1433'

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
        try:
            conn: pyodbc.Connection = pyodbc.connect(connection_string)
            cursor: pyodbc.Cursor = conn.cursor()

        except Exception:
            print("\nERROR: Could not connect to Azure :(\n" +
                  "Username, password, server name or database name are incorrect!\n" +
                  "Try again by typing everything correctly!\n")
            break

        # DEFINE NEW SQL QUERIES AND EXECUTE THEM
        while wish == '' or wish == 'yes':
            try:
                print("\nTrying to create new table and inserting repos id's, names and URLs to Azure SQL Database...\n")

                cursor.execute(f'''
                CREATE TABLE {list_repos.username}_repos
                (id VARCHAR(50) PRIMARY KEY, repo_name VARCHAR(255), URL VARCHAR(255));
                ''')

                try:
                    for i in range(list_repos.repo_qty):
                        cursor.execute(f'''
                        INSERT INTO {list_repos.username}_repos (id, repo_name, URL) 
                        VALUES ({list_repos.id_list[i]},'{list_repos.repo_list[i]}','{list_repos.url_list[i]}');
                        ''')

                    print('\nSuccesfully inserted data in Azure Database! :)\n')

                    break

                except Exception as e:
                    print("FATAL ERROR: Could not insert data in Azure Database!\n" +
                          "Report it to the owner of this code!\n" +
                          f"Error description: {e}\n")
                    wish = 0

                break

            except Exception as f:
                print(f"\n\nERROR: Could not create a new table or insert data for this user :(\n" +
                      "Maybe the table already exists in this Azure Database...\n" +
                      f"Error Description: {f}\n")

                wish = input("\nYou can delete the existing table if you want to try update it, is that your wish?\n" +
                             "Type 'yes' if you want to update it, or type anything else to leave it as it is: ")

                if (wish == 'yes'):
                    print("\nDropping existing table...\n")
                    cursor.execute(f'''DROP TABLE {list_repos.username}_repos''')

                else:
                    print("\nLeaving everything as it is...\n")
                    wish = 0

        # CLOSING AND COMMITING THE CONNECTION WHEN DONE
        conn.commit()
        cursor.close()
        conn.close()
        exit = True
        break

    else:
        print(f"\n\nERROR: Could not connect to Azure using the requested user '{list_repos.username}' repositories.\n" +
              "Maybe this github user doesnt have any repositories or it doesnt exists.\n")
