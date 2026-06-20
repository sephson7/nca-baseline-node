import sqlite3
import time
from datetime import datetime
from gpiozero import OutputDevice

# Mirror the physical hardware assignments from app.py
bulb_relay = OutputDevice(23, active_high=False, initial_value=False)
fan_relay = OutputDevice(24, active_high=False, initial_value=False)

DB_NAME = "nelson_core_logs.db"

def get_historical_pattern(current_hour, element_id):
    """
    Analyzes past entries in the SQLite ledger for the current hour.
    Returns 1 if the element is historically used more than 50% of the time, else 0.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Query logs where the timestamp hour matches the current wall-clock hour
        cursor.execute("""
            SELECT state_requested FROM event_ledger 
            WHERE element_id = ? AND strftime('%H', timestamp) = ?
        """, (element_id, f"{current_hour:02d}"))
        
        results = cursor.fetchall()
        conn.close()
        
        if not results:
            return None
            
        # Calculate frequency
        states = [r[0] for r in results]
        average_state = sum(states) / len(states)
        
        return 1 if average_state >= 0.5 else 0
        
    except sqlite3.OperationalError:
        # If app.py hasn't created the database yet, pass safely
        return None

def execute_autonomous_loop():
    print("NCA Predictive Engine initialized. Monitoring telemetry patterns...")
    
    while True:
        current_hour = datetime.now().hour
        
        # Evaluate Element 01 (Heating Load / Bulb)
        bulb_prediction = get_historical_pattern(current_hour, 'bulb')
        if bulb_prediction is not None:
            if bulb_prediction == 1 and not bulb_relay.value:
                print(f"[{datetime.now()}] Pattern Detected: Automating Bulb ON for hour {current_hour}")
                bulb_relay.on()
            elif bulb_prediction == 0 and bulb_relay.value:
                print(f"[{datetime.now()}] Pattern Detected: Automating Bulb OFF for hour {current_hour}")
                bulb_relay.off()
                
        # Evaluate Element 02 (Air Flow / Fan)
        fan_prediction = get_historical_pattern(current_hour, 'fan')
        if fan_prediction is not None:
            if fan_prediction == 1 and not fan_relay.value:
                print(f"[{datetime.now()}] Pattern Detected: Automating Fan ON for hour {current_hour}")
                fan_relay.on()
            elif fan_prediction == 0 and fan_relay.value:
                print(f"[{datetime.now()}] Pattern Detected: Automating Fan OFF for hour {current_hour}")
                fan_relay.off()
        
        # Sleep for 10 minutes before polling the database ledger patterns again
        time.sleep(600)

if __name__ == '__main__':
    execute_autonomous_loop()
