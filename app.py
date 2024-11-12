from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Manish Pandey"  # Replace with your full name
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Execute the 'top' command and get its output
    top_output = subprocess.getoutput("top -bn1")
    
    # Render the output in HTML format
    return f"""
    <h1>Name: {name}</h1>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
