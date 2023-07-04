from flask import Flask, request, jsonify
from python_backend import backend_python   

app = Flask(__name__)

@app.route('/process_form', methods=['POST'])      #fetches the post request from JS, converts FORM object to dictionary; and passes on to backend python object
def process_form():
    form_data = request.form.to_dict()
    result = backend_python(form_data)  
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)