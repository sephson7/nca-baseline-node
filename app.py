import sqlite3
import os
from datetime import datetime
from flask import Flask, render_template_string, redirect, url_for
from gpiozero import OutputDevice

# Define GPIO interface pins with inverted logic handling (Active Low Relays)
bulb_relay = OutputDevice(23, active_high=False, initial_value=False)
fan_relay = OutputDevice(24, active_high=False, initial_value=False)

app = Flask(__name__)
DB_NAME = "nelson_core_logs.db"

def initialize_database():
    """Builds the local operational ledger table if not present inside the database file."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS event_ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            element_id TEXT NOT NULL,
            state_requested INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def log_system_event(element, state):
    """Writes strict time-stamped parameters into the local database schema for tracking."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
        INSERT INTO event_ledger (timestamp, element_id, state_requested)
        VALUES (?, ?, ?)
    """, (timestamp_str, element, state))
    conn.commit()
    conn.close()

# Modular local UI layer requiring zero internet accessibility to serve layout
HTML_UI = """
<!DOCTYPE html>
<html>
<head>
    <title>NCA Local Node Panel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; background: #060913; color: #f8fafc; padding: 20px; text-align: center; }
        .card { background: #0f1524; border: 1px solid #1e293b; border-radius: 8px; padding: 20px; margin: 15px auto; max-width: 400px; }
        .btn { display: inline-block; padding: 10px 20px; margin: 10px; border-radius: 5px; text-decoration: none; font-weight: bold; color: #fff; }
        .btn-on { background: #10b981; }
        .btn-off { background: #ef4444; }
        .status { color: #38bdf8; font-weight: bold; }
    </style>
</head>
<body>
    <h2>NCA Control Console</h2>
    <p>System Engine: <span class="status">ONLINE</span></p>
    
    <div class="card">
        <h3>Element 01: Heating Load (Bulb)</h3>
        <p>Current State: <span class="status">{{ 'ON' if bulb_state else 'OFF' }}</span></p>
        <a href="/toggle/bulb/1" class="btn btn-on">ON</a>
        <a href="/toggle/bulb/0" class="btn btn-off">OFF</a>
    </div>

    <div class="card">
        <h3>Element 02: Air Flow (Fan)</h3>
        <p>Current State: <span class="status">{{ 'ON' if fan_state else 'OFF' }}</span></p>
        <a href="/toggle/fan/1" class="btn btn-on">ON</a>
        <a href="/toggle/fan/0" class="btn btn-off">OFF</a>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(
        HTML_UI, 
        bulb_state=bulb_relay.value, 
        fan_state=fan_relay.value
    )

@app.route('/toggle/<element>/<int:state>')
def toggle_device(element, state):
    if element == 'bulb':
        if state == 1:
            bulb_relay.on()
        else:
            bulb_relay.off()
        log_system_event('bulb', state)
        
    elif element == 'fan':
        if state == 1:
            fan_relay.on()
        else:
            fan_relay.off()
        log_system_event('fan', state)
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    initialize_database()
    # Runs locally on port 5000, visible to devices on your local Wi-Fi net
    app.run(host='0.0.0.0', port=5000)
