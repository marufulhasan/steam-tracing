from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from calc import get_trace_result, calc_sat_temp

 
app = Flask(__name__)


app.debug = True
app.secret_key = 'okidofokido'



@app.route('/' , methods=['GET', 'POST'])

def set_project():
	return render_template('main.html')


@app.route('/calc_trace' , methods=['GET', 'POST'])

def get_calc_trace():
	input_data = request.get_json()
	output_data = get_trace_result(input_data)

	return jsonify(result=output_data)


@app.route('/sat_temp' , methods=['GET', 'POST'])

def get_sat_temp():
	input_data = request.get_json()
	if (input_data['steam_pressure']):
		steam_temp = calc_sat_temp ((input_data['steam_pressure']))
		return jsonify(result=steam_temp)

	
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
if __name__ == '__main__':
	app.run(port= 11000)