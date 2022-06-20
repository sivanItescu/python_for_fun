import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE)
# print(response.json())

response = requests.put(BASE+'/jobs/1', data={'job_title': 'Senior SW Engineer at Goggle'})
print(response.json())

response = requests.put(BASE+'/jobs/2', data={'job_title': 'Junior SW Engineer at Goggle'})
print(response.json())

response = requests.put(BASE+'/jobs/3', data={'job_title': 'Senior SW Engineer at Amazon'})
print(response.json())

response = requests.put(BASE+'/jobs/4', data={'job_title': 'Senior SW Engineer at Apple'})
print(response.json())

# response = requests.get(BASE+'/jobs/1')
# print(response.json())
response = requests.get(BASE+'/alljobs')
print(response.json())

response = requests.get(BASE+'/about')
print(response.json())