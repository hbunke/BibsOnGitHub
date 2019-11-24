import json


csv_string = "Organisation,Repository,Stars,Forks,Forked,Last updated\n"
with open("all-libs.json", 'r') as json_file:
    data = json.load(json_file)
    for org in data["organisations"]:
        for repo in org['repositories']:
            # print(type(repo))
            if type(repo) is dict:
                csv_string += org['name'] + "," + repo['name'] + "," + str(repo['stargazers_count']) + "," + str(repo['forks_count']) + "," + str(repo['fork']) + "," + str(repo['forks_count']) + "," + repo['updated_at'] + ",\n"

with open('repositories.csv', 'w', encoding='utf8') as csv_file:
    csv_file.write(csv_string)
