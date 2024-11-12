from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Manish Pandey"
    username = "codespace_user"  # Temporary placeholder
    
    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    # Simplified HTML response without top command output
    response = f"""
    <h1>Name: {name}</h1>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
