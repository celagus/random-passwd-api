from flask import Flask, request
from flask_restful import Resource, Api
import random
import string

app = Flask(__name__)

@app.route('/generate-password/', methods=['GET'])

def get_params():
	#get params from uri
	lowercase = int(request.args.get('lowercase'))
	uppercase = int(request.args.get('uppercase'))
	digits = int(request.args.get('digits'))
	length = int(request.args.get('length'))

	#requisite 1: min length cannot be less than 30 chars
	#requisite 2: number of lc, uc and digits cannot be less than 10 each one
	if length>=(lowercase+uppercase+digits) and length>=8 and lowercase>=2 and uppercase>=2 and digits>=2:
		passwd = generate_passwd(length, uppercase, lowercase, digits)
		return { "password": passwd }
	else:
		return {"statusCode":400, "body":"""Bad Request
    	Total number of password characters cannot be less than 30
    	The number of lowercase letters cannot be lower than 10
    	The number of uppercase letters cannot be lower than 10
		The number of digits cannot be lower than 10"""}	

def generate_passwd(minlen, minuchars, minlchars, minnumbers):
	#random sample lists for each char type
	uc_list = random.sample(string.ascii_uppercase, minuchars)
	lc_list = random.sample(string.ascii_lowercase, minlchars)
	n_list = random.sample(string.digits, minnumbers)
	#join them in one list
	all_list = uc_list+lc_list+n_list
	#if total chars is less than min len, full with printables
	if len(all_list)<minlen:
		diff = minlen - len(all_list)
		diff_list = random.sample(string.printable, diff)
		passwd = all_list + diff_list
	else:	
		passwd = all_list[:]
	random.shuffle(passwd) #shuffle'em
	return ''.join(passwd)

def get_status():
	try:
		get_params()
	except:
		return {"statusCode":404, "body":"""Sorry the requested URL cannot be found.
			If you entered the URL manually please check your
			spelling and try again."""}

if __name__ == '__main__':
	app.run(debug=False)
