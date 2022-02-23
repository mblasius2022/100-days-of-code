from matplotlib.axis import XAxis
from numpy import append
import requests

from plotly.graph_objects import Bar
from plotly import offline

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

# process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels, repo_links = [], [], [], []
for repo_dict in repo_dicts:
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_dict['name']}</a>"
    stars.append(repo_dict['stargazers_count'])
    label = f"{owner} <br />{description}"
    labels.append(label)
    repo_links.append(repo_link)

#make visualisation
data = [{
    'type': 'bar',
    #'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25,25)'}
        },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most Starred Python projects on GitHub ',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
        },
    }


fig = {'data': data,'layout': my_layout}
offline.plot(fig, filename='python_repos.html')