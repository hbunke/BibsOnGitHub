import re
import json
import requests
import sys

# fill in username and token to get 5000 instead of 60 requests per hour
username = ""
token = ""

github_session = requests.Session()
github_session.auth = (username, token)

libraries = open("libraries.csv", "rt")
lines = libraries.readlines()
json_result_string ='''
{
  "organisations" : [
'''
for line in lines:
    json_result_string += "    {\n"
    parts = line.split(";")
    country = parts[0]
    city = parts[1]
    name = parts[2]
    link = parts[3]
    json_result_string += "      \"name\": \"" + name + "\",\n"
    json_result_string += "      \"country\": \"" + country + "\",\n"
    json_result_string += "      \"city\": \"" + city + "\",\n"
    json_result_string += "      \"url\": \"" + link.replace("\n","") + "\",\n"
    json_result_string += "      \"repositories\": "
    github_orga = re.findall("\/([^\/^$]+)$", link)[0].replace("\n","")
    print(github_orga)

    api_url = "https://api.github.com/orgs/" + github_orga + "/repos?per_page=500"
    print(api_url)
    repo_data = github_session.get(url=api_url).json()
    json_result_string += json.dumps(repo_data, indent=4, ensure_ascii=0) + "\n"
    json_result_string += "    },\n"

json_result_string = json_result_string[:-2]
json_result_string += '''
  ]
}
'''

with open("all-libs.json", "w") as json_file:
    json_file.write(json_result_string)
