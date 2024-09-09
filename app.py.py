# webapp : Programming language, HTML, server, Logic Building

from flask import Flask, render_template,request
from views import views

app = Flask(__name__)
app.register_blueprint(blueprint=views,url_prefix="/")

@app.route('/home')
def home():
    return render_template('index.html')


class Convert:
    def __init__(self, value, from_unit, to_unit, unit_type):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.unit_type = unit_type
    
    def convert_length(self):
        conversion_factors = {
            'meters': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.34
        }
        print(f"Converting length from {self.from_unit} to {self.to_unit}")
        if self.from_unit not in conversion_factors or self.to_unit not in conversion_factors:
            raise ValueError(f"Invalid unit for length conversion: {self.from_unit} or {self.to_unit}")
        
        value_in_meters = self.value * conversion_factors[self.from_unit]
        return value_in_meters / conversion_factors[self.to_unit]
    
    def convert_weight(self):
        conversion_factors = {
            'Gram': 1.0,
            'kilogram': 1000.0,
            'milligram': 0.001,
            'microgram': 0.000001,
            'Ton': 1000000.0,
            'Pound': 453.592,
            'Ounce': 28.3495,
            'Stone': 6350.29
        }
        print(f"Converting weight from {self.from_unit} to {self.to_unit}")
        if self.from_unit not in conversion_factors or self.to_unit not in conversion_factors:
            raise ValueError(f"Invalid unit for weight conversion: {self.from_unit} or {self.to_unit}")
        
        value_in_grams = self.value * conversion_factors[self.from_unit]
        return value_in_grams / conversion_factors[self.to_unit]
    
    def convert_temperature(self):
        print(f"Converting temperature from {self.from_unit} to {self.to_unit}")
        if self.from_unit == 'Celsius' and self.to_unit == 'Fahrenheit':
            return (self.value * 9/5) + 32
        elif self.from_unit == 'Fahrenheit' and self.to_unit == 'Celsius':
            return (self.value - 32) * 5/9
        elif self.from_unit == 'Celsius' and self.to_unit == 'Kelvin':
            return self.value + 273.15
        elif self.from_unit == 'Kelvin' and self.to_unit == 'Celsius':
            return self.value - 273.15
        elif self.from_unit == 'Fahrenheit' and self.to_unit == 'Kelvin':
            return (self.value + 459.67) * 5/9
        elif self.from_unit == 'Kelvin' and self.to_unit == 'Fahrenheit':
            return (self.value * 9/5) - 459.67
        else:
            raise ValueError(f"Invalid temperature conversion: {self.from_unit} to {self.to_unit}")
    
    def conversion(self):
        if self.unit_type == 'length':
            return round(self.convert_length(),2)
        elif self.unit_type == 'weight':
            return round(self.convert_weight(),2)
        elif self.unit_type == 'temperature':
            return round(self.convert_temperature(),2)
        else:
            raise ValueError(f"Invalid unit type: {self.unit_type}")

@app.route('/',methods=['GET','POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        unit_type = request.form['unit_type']

        converter = Convert(value,from_unit,to_unit,unit_type)
        result = converter.conversion()
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
'''
Flask App (1.py): The Flask server handles form submissions, processes the conversion through the Convert class, and renders the result on the webpage.
Conversion Logic: For now, only the length conversion is implemented. You can extend the Convert class to support other unit types like weight and temperature.
HTML Form (index.html): The form captures user input and sends it to the server for processing. The result is displayed after the form is submitted.
Error handling: If an invalid temperature conversion is attempted (like converting from Celsius to Pounds), the function raises a ValueError.
'''

'''
{ # the{{ }} syntax in Flask and Jinja2 templates is used for template expressions. It is a way to embed Python variables or expressions directly into the HTML being rendered by the server.

Meaning of {{ }}
The double curly braces {{ }} are used to output the value of a variable or an expression in an HTML template.
When Flask renders the HTML template, it replaces everything inside the {{ }} with the corresponding value or result of the expression. #}
'''