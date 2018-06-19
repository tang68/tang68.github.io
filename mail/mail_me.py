from flask import Flask,render_template, request,json, jsonify

app = Flask(__name__)

@app.route('/background_process')
def background_process():
	try:
		name = request.args.get('name', 0, type=str)
		email = request.args.get('email', 0, type=str)
		phone = request.args.get('phone', 0, type=str)
		message = request.args.get('message', 0, type=str)
		return jsonify(result=email)
	except Exception as e:
		return str(e)