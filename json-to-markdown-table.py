import json


markdown_string = '''
| Country     | City            | Organisation                                                         | Repositories |
| ----------- | --------------- | -------------------------------------------------------------------- | ------------ |
'''
with open("all-libs.json", 'r') as json_file:
    data = json.load(json_file)
    for org in data["organisations"]:
        markdown_string += "|" + org['country'] + "|" + org['city'] + "|[" + org['name'] + "](" + org['url'] + ")|" + str(len(org['repositories'])) + "|\n"

print(markdown_string)

with open('libraries.md', 'w', encoding='utf8') as markdown_file:
    markdown_file.write(markdown_string)
