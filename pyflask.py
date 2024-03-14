from flask import Flask, request
import io
import sys

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute():
    print("Received request:", request)
    print("Form data:", request.form)
    try:
        code = request.form['code']
    except KeyError:
        return "No 'code' key found in the form data", 400
    
    stdout = sys.stdout
    sys.stdout = io.StringIO()  # Redirect stdout
    try:
        exec(code)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = stdout  # Restore stdout
    return output

if __name__ == '__main__':
    app.run(debug=True,port=5454,host='0.0.0.0')
