import requests
import json
import csv
import urllib2
import random
import string


def randomPassword():
    """Generate a random password """
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    for i in range(4):
        password += random.choice(randomSource)
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

# Get the Url
github_url = 'https://api.github.com/gists/6bb69329f50efb7b79f7e5a2bf31597d'

get_csv = requests.get(github_url).json()['files']['users.csv']['raw_url']

github_csv = urllib2.urlopen(get_csv)


# Read the csv contents from the url
reader = csv.DictReader(github_csv)

# Sort the list by Firstname
sorted = sorted(reader, key=lambda k: (k['Firstname']))

# Add password and UPN
for i in sorted:
    i['UPN'] = i['Firstname'] + '.' + i['Lastname'] + '@spr_test.com'
    i['Password'] = randomPassword()

# Order the keys
keys = ['Id','Firstname','Lastname','UPN','Password']

# Write out csv file
with open('github.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(sorted)

