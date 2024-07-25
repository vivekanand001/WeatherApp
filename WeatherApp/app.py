from flask import Flask,render_template,request
from geocoding import geocoding
from weather import forecastweather
from kelvin import tocelsius

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        cityname=request.form['search']
        try:
            lat,lon=geocoding(cityname)
            if lat==None and lon==None:
                return render_template('index.html',error=True)
        except Exception as e:
            return f'oops{e}'
        weatherdata=forecastweather(lat,lon)
        weatherdata=tocelsius(weatherdata)
        return render_template('index.html',output=True,weatherData=weatherdata,cityname=cityname)
    return render_template('index.html',output=False)
        
if __name__=='__main__':
    app.run(debug=True)    