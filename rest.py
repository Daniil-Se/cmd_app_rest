from flask import Flask
from flask import request, json
app = Flask(__name__)


@app.route('/post', methods=['POST'])
def test():
	print('Данные успешно получены')
	data = request.get_json()
	print(data)
	return json.dumps({
                "status": "success"
            })


if __name__ == '__main__':
	app.run(debug=True)
