import urllib, json, ast
import math
from descriptions import *

#Categories of Political Parties
groups = {
	10:'Ecologist|4daf4a',
	20:'Socialist|a65628',
	30:'Social Democratic|e41a1c',
	40:'Liberal|ff7f00',
	50:'Christian Democrat|984ea3',
	60:'Conservative|377eb8',
	70:'Nationalist|000000',
	80:'Agrarian|4daf4a',
	90:'Ethnoregional|ffff33',
	95:'Special Issue|999999',
	98:'Diverse|999999',
	999:'NA'
}

#Loads in json databae
def load(url):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return data


#Indexes descriptions
variables_index = [x[0] for x in variables]
variables_describe = [x[1] for x in variables]
def f(item):
	return variables_index.index(item)

#Loads all the current datasets
data = load("https://manifesto-project.wzb.eu/tools/api_list_core_versions.json?api_key=7c5240a0a9d7a553e4d3aae4b659f465")

#Picks most recent dataset
current = data['datasets'][-1]['id']
data = load("https://manifesto-project.wzb.eu/tools/api_get_core.json?api_key=7c5240a0a9d7a553e4d3aae4b659f465&key="+current)

#Gets citation
citation = load("https://manifesto-project.wzb.eu/tools/api_get_core_citation?api_key=7c5240a0a9d7a553e4d3aae4b659f465&key="+current)['citation']

#data[0] is the list of keys
countries = []
data = data[1:]

#List all the countries
for country in data:
	name = country[f('countryname')]
	if name not in countries:
		countries.append(name)

#Gets the score of a variable, based on an average of it's positive and negative attributes 
def lr(item, scoring):
	total = 0
	for variable in scoring['pos']:
		total += float(item[f(variable)])
	for variable in scoring['neg']:
		total -= float(item[f(variable)])
	return total / (len(scoring['pos']) + len(scoring['neg']))

#Gets all the elections for a country
def getDates(country):
	dates = []
	for election in data:
		if election[f('countryname')] == countries[countries.index(country)]:
			if election[f('edate')] not in dates:
				dates.append(election[f('edate')])
	return dates

#Works out the election data for a country, based on a model x, y and z (pos/neg) and description (other description factors)
def elections_for(country, date, x, y, z, description):
	parties = []
	for election in data:
		if election[f('countryname')] == countries[countries.index(country)]:
			if election[f('edate')] == date:
				#if the data is for this election and country, get the grouping, x, y and z values
				grouping = groups[int(election[f('parfam')])].split("|")
				x_value = round(lr(election, x), 3)
				y_value = round(lr(election, y), 3)
				z_value = round(lr(election, z), 3)
				if z_value > 0:
					#Encoding so the string is readable in javascript
					party = {
						"x": x_value,
						"y": y_value,
						"z": z_value,
						"id": election[f('party')].encode('ascii','ignore'),
						"abbrev": election[f('partyabbrev')].encode('ascii','ignore'),
						"name": election[f('partyname')].encode('ascii','ignore'),
						"color": "#" + grouping[1].encode('ascii','ignore'),
						"grouping": grouping[0].encode('ascii','ignore')
					}
					#party[description of factor] = value of factor rounded
					factors = []
					print description
					for item in description['factors']:
						party[item[1].encode('ascii','ignore')] = round(float(election[f(item[0])]),1)
					parties.append(party)
	return parties