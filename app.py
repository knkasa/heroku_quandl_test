from flask import Flask, render_template, request, redirect

import pandas as pd
import numpy as np
import quandl

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import io
import base64

# instead matplotlib, use bokeh
# https://github.com/realpython/flask-bokeh-example/blob/master/tutorial.md

#main = Flask(__name__, static_url_path="/static", static_folder="static")
app = Flask(__name__)


#  The route_name should match xxxx=Flask(__name__)
@app.route('/home', methods=['GET','POST']  )
def home():
	if request.method=='GET':
		return  render_template('input.html')
	else:
		#this is after hitting submit botton
		name1 = request.form['var1']
		
		quandl.ApiConfig.api_key='B39qwgtFcsscasryHsKi'
		# WIKI/PRICES is Quandl ID name, ticker=AAPL
		data = quandl.get_table('WIKI/PRICES', ticker=name1 )
		
		data.plot(x='date', y='close' ) #panda frame
		img = io.BytesIO()
		plt.savefig(img, format='png')
		img.seek(0)

		plot_url = base64.b64encode(img.getvalue()).decode()

		#return 'done'
		return '<img src="data:image/png;base64,{}">'.format(plot_url)

	
		
#if __name__ == '__main__':
#    app.run(debug=True)

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)




