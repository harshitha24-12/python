import requests
import os

def download_gh():
    date = "2023-03-01"
    hour = "10"
    url = f"https://data.gharchive.org/{date}-{hour}.json.gz"
    file_name = f"{date}-{hour}.json.gz"
    file_path = os.path.join(os.getcwd(), file_name)
    
    # Download the file
    try:
        response = requests.get(url)
        response.raise_for_status()  
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    except Exception as e:
        print(f"Error downloading file: {e}")
        return None
print(download_gh())

# Unit test function
def test_download_gh():
    file_path = download_gh()
    assert file_path is not None, "The file path should not be None."
    assert os.path.exists(file_path), "The downloaded file does not exist."
    assert os.path.getsize(file_path) > 0, "The downloaded file is empty."
    os.remove(file_path)

