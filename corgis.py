from flask import Flask, url_for, Markup, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/carBrand")
def render_brand():
    return render_template('carBrand.html', options = get_make_options())
    
@app.route("/response")
def render_brand_response():
    if 'make' in request.args:
        make = request.args['make']
        mod = get_car_model(make)
    return render_template('brandExtention.html', options = get_make_options(), mod = mod, make = make)

    
@app.route("/carYear")
def render_year():
    return render_template("carYear.html", options = get_year_options())
    
@app.route("/yearResponse")
def render_year_response():
    if 'year' in request.args:
        year = request.args['year']
        carz = get_year_models(year)
    return render_template('yearExtention.html', options = get_year_options(), carz = carz, year = year)
    
@app.route("/carTran")
def render_transsmison():
    return render_template("carTran.html", options = get_tran_options())
    
@app.route("/tran")
def render_tran_response():
    if 'tran' in request.args:
        tran = request.args['tran']
        t = get_tran_cars(tran)
    return render_template("tranExtention.html", options = get_tran_options(), t = t, tran = tran)
    
@app.route("/MPG")
def render_fuel():
    return render_template("carFuel.html")
    
def get_make_options():
    with open('cars.json') as cars_data:
        car = json.load(cars_data)
        makes = []
        options = ""
        for c in car:
            make = c["Identification"]["Make"]
            if (make not in makes):
                makes.append(make)
                options += Markup("<option value=\"" + (make) + "\">" + (make) + "</option>")
    return options
  
  
def get_car_model(make):
    with open('cars.json') as cars_data:
        car = json.load(cars_data)
        models = []
        mod = ""
        for m in car:
            model = m["Identification"]["ID"]
            if (model not in models and make == m["Identification"]["Make"]):
                models.append(model)
                mod += Markup("<mod value=\"" + (model) + "\">" + "<br>" + (model) + "</mod>")
    return mod
    
def get_year_options():
    with open('cars.json') as cars_data:
        car = json.load(cars_data)
        yrs = []
        options = ""
        for y in car:
            year = y["Identification"]["Year"]
            if (year not in yrs):
                yrs.append(year)
                options += Markup("<option value=\"" + str(year) + "\">" + str(year) + "</option>")
    return options
    
def get_year_models(year):
    with open('cars.json') as cars_data:
        car = json.load(cars_data)
    g = []
    carz = ""
    for m in car:
        h = m["Identification"]["Model Year"]
        if (h not in g and year == str(m["Identification"]["Year"])):
            g.append(h)
            carz += Markup("<carz value=\"" + (h) + "\">" + "<br>" + (h) + "<carz>")
    return carz
    
    
def get_tran_options():
    with open('cars.json') as cars_data:
        car = json.load(cars_data)
        tranz = []
        options = ""
        for t in car:
            tran = t["Engine Information"]["Transmission"]
            if (tran not in tranz):
                tranz.append(tran)
                options += Markup("<option value=\"" + (tran) + "\">" + (tran) + "</option>")
    return options
    
def get_tran_cars(tran):
    with open('cars.json') as cars_data:
        car = json.load(cars_data)
    e = []
    t = ""
    for p in car:
        k = p["Identification"]["Model Year"]
        if (k not in e and tran == p["Engine Information"]["Transmission"]):
            e.append(k)
            t += Markup("<t value=\"" + (k) + "\">" + "<br>" + (k) + "<t>")
    return t
    
if __name__=="__main__":
    app.run(debug=False)
    