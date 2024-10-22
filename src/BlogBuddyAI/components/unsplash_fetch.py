import requests

def fetch_unsplash_images(prompt, access_key, num_images):
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {access_key}",
    }
    
    params = {
        "query": prompt,
        "per_page": num_images
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error: {response.status_code}, {response.text}"}
