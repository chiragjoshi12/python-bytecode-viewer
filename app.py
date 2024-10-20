from flask import Flask, render_template, request, jsonify
import dis
import io
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_bytecode', methods=['POST'])
def get_bytecode():
    source_code = request.form['source_code']
    bytecode_output = ""
    try:
        code_obj = compile(source_code, '<string>', 'exec')

        buffer = io.StringIO()
        sys.stdout = buffer

        dis.dis(code_obj)

        sys.stdout = sys.__stdout__
        bytecode_output = buffer.getvalue()
    except SyntaxError as e:
        bytecode_output = f"Syntax Error: {e}"

    return jsonify(bytecode=bytecode_output)

if __name__ == '__main__':
    app.run(debug=True)
