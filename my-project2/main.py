import requests

response = requests.get("https://github.com/selcanatakk?tab=repositories")
my_projects = response.json()
print(my_projects)
print(type(my_projects))


for project in my_projects:
    print(f"Project name : {project['name']}")
