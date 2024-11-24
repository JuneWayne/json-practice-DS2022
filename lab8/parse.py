#!/usr/bin/env python3.
import json

with open('data/schacon.repos.json', 'r')as file:
    data = json.load(file)

with open('chacon.csv', 'w')as chacon:
    for i in data[0:5]:
        name = i.get('name')
        html_url = i.get('html_url')
        updated_at = i.get('updated_at')
        visibility = i.get('visibility')

        inline_csv = f'{name}, {html_url}, {updated_at}, {visibility} \n'
        chacon.write(inline_csv)

