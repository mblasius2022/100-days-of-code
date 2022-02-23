from traceback import print_tb
import requests
import json

file_path = '/home/marioblasius/git/100-days-of-code/projects/chapter_17_apis/data'
file_name = file_path + 'readable_hn_data.json'
#make an api call
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status Code = {r.status_code}")

# explore the structure of the data
response_dict = r.json()
readable_file = file_name
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)