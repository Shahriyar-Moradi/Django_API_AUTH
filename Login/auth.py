import requests

url = 'http://localhost:8000/api/account/logged-in-user-email/'
headers = {
    'Authorization': f'Token 93fa4c21b3382edc39c6ae1a5a80fd49e70d5f64',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print('User Email:', data['email'])
else:
    print('Request failed with status code:', response.status_code)
