from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Manish Pandey"
    
    # System username
    username = os.getlogin()
    
    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    # HTML content
    response = f"""
    <h1>Name: {name}</h1>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>TOP output:\n{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

