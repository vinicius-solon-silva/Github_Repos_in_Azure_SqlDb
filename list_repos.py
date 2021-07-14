import requests


# -----LISTING GITHUB REPOSITORIES-----


# STABLISHING CONNECTIONS WITH GITHUB USING REQUESTS
username = input('''\nType the GitHub username to list his repositories and
store them in a Azure SQL Database: ''')
username.lower()

r = requests.get(f'http://api.github.com/users/{username}/repos')

# CONVERTING DATA INTO JSON() DICTIONARY
repos = r.json()

# DEFINING LISTS OF ACQUIRED DATA (Repo name, id, url)
repo_list = []
id_list = []
url_list = []
repo_qty = 0

# PRINTING REPOS AND APPENDING DATA TO DEFINED LISTS
print(f'\n{username} repos:\n')
for index in repos:
    print(index["name"])
    repo_list.append(index["name"])
    id_list.append(index["id"])
    url_list.append(index["html_url"])
    repo_qty += 1

# DEFINING SECTION OF THE 'INSERT' SQL QUERY COMMAND

print('\n\n')
