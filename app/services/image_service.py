import requests

from app.config.settings import UNSPLASH_ACCESS_KEY


def fetch_images(topic, count=3):

    url = "https://api.unsplash.com/search/photos"

    params = {
        "query": topic,
        "per_page": count
    }

    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers
        )

        data = response.json()

        images = []

        for item in data["results"]:

            image_url = item["urls"]["regular"]

            images.append(image_url)

        return images

    except Exception as e:

        print("Image Fetch Error:", e)

        return []