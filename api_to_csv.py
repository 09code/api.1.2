import requests
import csv

api_url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(api_url)
api_data = response.json()

csv_file_name = "api_data.csv"
with open(csv_file_name, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=api_data[0].keys())
    writer.writeheader()
    writer.writerows(api_data)

print("Data loaded and saved into '{}' successfully.".format(csv_file_name))

