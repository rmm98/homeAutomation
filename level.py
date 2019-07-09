import json,time,requests
from boltiot import Bolt 
mybolt = Bolt("API Key","Device ID")
while True:
    response = requests.request("GET","https://cloud.boltiot.com/remote/API Key/serialWR?data=getAnalogValues&deviceName=Device ID")
    data = json.loads(response.text)
    csv = data["value"]
    temp = csv.split(",")
    arr=[]
    for i in range(len(temp)-1):
        arr.append(int(temp[i]))
    print(arr)

    if arr[0] < 100:
        print("Water Level below 20%. Turning pump on")
        requests.request("GET","https://cloud.boltiot.com/remote/API Key/serialWR?data=pumpOn&deviceName=Device ID")
    elif arr[4] > 100:
        print("Water level 100%. Turning pump off")
        requests.request("GET","https://cloud.boltiot.com/remote/API Key/serialWR?data=pumpOff&deviceName=Device ID")
    else:
        if arr[3] > 100:
            print("Water level is at 80%")
        elif arr[2] > 100:
            print("Water level is at 60%")
        elif arr[1] > 100:
            print("Water level is at 40%")
        elif arr[0] > 100:
            print("Water level is at 20%")
        else:
            print("Error")
    time.sleep(10)