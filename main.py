from flask import Flask, render_template, g, request, json
import flask_sijax
import os, sys, time, ast
from urllib import unquote
from manifesto import *

path = os.path.join('.', os.path.dirname(__file__), '../')
sys.path.append(path)

app = Flask(__name__)
app.config["SIJAX_STATIC_PATH"] = os.path.join('.', os.path.dirname(__file__), 'static/sijax/')
flask_sijax.Sijax(app)

citations = [citation, "Chris Hanretty, Professor of Politics at Royal Holloway: https://twitter.com/chrishanretty/status/1096160622423744513"]

default_x = {
    "name":"Economic L-R",
    "pos":[
        "per401",
        "per402",
        "per414",
        "per505",
        "per702",
        "per704"],
    "neg":[
        "per404",
        "per405",
        "per409",
        "per412",
        "per413",
        "per415",
        "per504",
        "per701"]
}

default_y = {
    "name":"Cultural L-R",
    "pos": [
        "per109",
        "per305",
        "per601",
        "per603",
        "per605",
        "per608"],
    "neg": [
        "per103",
        "per107",
        "per503",
        "per602",
        "per604",
        "per607"]
}

default_z = {
    "name":"Percentage Vote",
    "pos": ["pervote"],
    "neg": []
}

default_description = {
    "xDescription": "Economic Score",
    "yDescription": "Cultural Score",
    "factors": [["pervote"]],
    "xScale": [-6, 6],
    "yScale": [-6, 6]
}
#Gets all election results, sets them to the parties variable, sets the date, then calls draw
def draw(obj, country, date, x, y, z, description):
    parties = elections_for(country, date, x, y, z, description)
    obj.script('parties = %s' % parties)
    obj.script('date = "' + date + '"')
    obj.script('draw()')

@flask_sijax.route(app, "/")
def main():

    x = default_x
    y = default_y
    z = default_z
    description = default_description

    #Establishes chart with x,y,z setup
    def init(obj):
        print description['factors']
        if len(description['factors'][0]) == 1:
            factors = []
            for factor in description['factors']:
                index = f(factor[0])
                full = variables[index]
                factors.append(full)
            description['factors'] = factors
        print description['factors']
        obj.script('init(%s, %s, %s, %s)' % (x, y, z, description))

    #Gets election data for the country and count (the election)
    def getElections(obj, country, count):
        dates = getDates(country)

        #If there are more elections to show, increment the count
        if count < len(dates):
            if count < 0:
                obj.script('count+=1')
            else:
                date = dates[count]
                draw(obj, country, date, x, y, z, description)
        #Else, reset count
        else:
            date = dates[0]
            obj.script("count=0;")
            draw(obj, country, date, x, y, z, description)

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('init', init)
        g.sijax.register_callback('getElections', getElections)
        return g.sijax.process_request()

    #Pass time so cache of css/js is reset
    return render_template('index.html', last_updated=str(int(round(time.time() * 1000))), countries=sorted(countries), citations=citations)

@flask_sijax.route(app, "/modify")
def modify():
    return render_template("modify.html", last_updated=str(int(round(time.time() * 1000))), variables = variables, info=[str(default_x).replace("'", '"'), str(default_y).replace("'", '"'), str(default_z).replace("'", '"'), str(default_description).replace("'", '"')])

if __name__ == '__main__':
    app.run()