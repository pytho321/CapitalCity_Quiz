import requests

def random_city_capitals():
    url = 'https://countriesnow.space/api/v0.1/countries/capital'
    response = requests.get(url)
    data = response.json()
    
    if data.get('success'):
        country_data = data.get("data")[0]
        return country_data['name'], country_data['capital']
    
    return None, None
        
    