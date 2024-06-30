import datetime
import json



with open('sample_data.txt', mode="r") as file:
    data = file.readline()
    js = json.loads(data)
    print(js["results"]["sunset"])