from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
import asyncio
import socket
from datetime import datetime
import CPU
import MEM
import Storage
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return "サーバーは平常運転です"
@app.route('/PC_info', methods=['GET'])
def PC_info():
    processer_name=CPU.name()
    Mem_value=MEM.Value()
    Storage_value=Storage.Value()
    print(processer_name,Mem_value,Storage_value)
    return f"{processer_name} {Mem_value} {Storage_value}"
@app.route('/use_rate', methods=['GET'])
def use_rate():
    processer_rate=CPU.Use_rate()
    Mem_rate=MEM.Use_rate()
    Storage_rate=Storage.useing_value()
    print(processer_rate,Mem_rate,Storage_rate)
    return f"{processer_rate} {Mem_rate} {Storage_rate}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)