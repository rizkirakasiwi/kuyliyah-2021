import requests
from datetime import datetime

base_url = "http://192.168.43.126:8080"

def name_by_email(email):
    url = f"{base_url}/user/name/{email}"
    response = requests.get(url)
    return response.json()['name']

def do_attendance(email):
    current_time = datetime.now()
    current_time = current_time.strftime("%H:%M:%S")
    url = f"{base_url}/attendance"
    content = {"email": email, "time": current_time}
    response = requests.post(url, content)
    return response.json()['message']
