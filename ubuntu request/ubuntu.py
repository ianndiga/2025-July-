import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for URL
    url = input("Enter the URL of the image: ").strip()
    
    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Try fetching the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError if bad response

        # Extract filename from URL, or generate one if not found
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save image to the folder
        filepath = os.path.join(folder, filename)
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image saved successfully as: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("⚠️ Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ An error occurred: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image()