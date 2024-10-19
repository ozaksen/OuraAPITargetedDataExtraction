import sys
import os
import json
from datetime import datetime
import requests

TOKEN='YOUR_API_TOKEN_HERE'

def create_folder_and_save_response(folder_name):
    os.makedirs(folder_name, exist_ok=True)



def get_workout(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/workout'  
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "workout.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_tag(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/tag' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "tag.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_sleep_time(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/sleep_time' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "sleep_time.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_sleep(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/sleep' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "sleep.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_session(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/session'  
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "session.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_ring_confg(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/ring_configuration' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "ring_confg.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_daily_rest_mode(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/rest_mode_period' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_rest.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_daily_personal_info(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/personal_info' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_personal_info.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


def get_daily_heartrate(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/heartrate' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_heartrate.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_daily_spo2(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/daily_spo2' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_spo2.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


def get_daily_sleep(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/daily_sleep' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_sleep.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

def get_daily_readiness(start_date, end_date):
    url = 'https://api.ouraring.com/v2/usercollection/daily_readiness' 
    params={ 
        'start_date': start_date, 
        'end_date': end_date 
    }
    headers = { 
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.request('GET', url, headers=headers, params=params) 
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_readiness.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


def get_daily_activity(start_date, end_date):
    url = f'https://api.ouraring.com/v1/sleep?start={start_date}&end={end_date}'
    # params = {
    #     'start_date': start_date,
    #     'end_date': end_date
    # }
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        
        file_path = os.path.join(folder_name, "daily_activity.json")
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python oura_targeted_extraction.py <start_date> <end_date>")
        sys.exit(1)

    start_date = sys.argv[1]
    end_date = sys.argv[2]
        # Get the current date for the folder name
    current_date = datetime.now().strftime('%Y-%m-%d')
    folder_name = f"{current_date}_data"

    # Create folder and save the response
    create_folder_and_save_response(folder_name)

    get_daily_activity(start_date, end_date)
    get_daily_heartrate(start_date, end_date)
    get_daily_personal_info(start_date, end_date)
    get_daily_readiness(start_date, end_date)
    get_daily_sleep(start_date, end_date)
    get_daily_spo2(start_date, end_date)
    get_daily_rest_mode(start_date,end_date)
    get_workout(start_date, end_date)
    get_session(start_date, end_date)
    get_ring_confg(start_date, end_date)
    get_sleep(start_date, end_date)
    get_sleep_time(start_date, end_date)
    get_tag(start_date, end_date)



