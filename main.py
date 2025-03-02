import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Step 1: Send a GET request to the webpage URL
url = 'https://example.com'  # Replace with the URL you want to scrape
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Create a directory to save downloaded files
os.makedirs('downloaded_files', exist_ok=True)

# Step 4: Extract all links and download the files
for link in soup.find_all('a', href=True):
    file_url = link['href']
    
    # Check if the link is to a downloadable file (like an image, pdf, etc.)
    if file_url.endswith(('.jpg', '.png', '.gif', '.pdf', '.zip')):
        
        # Make the file URL absolute if it's a relative link
        file_url = urljoin(url, file_url)
        
        # Get the file name from the URL
        file_name = file_url.split('/')[-1]
        
        # Step 5: Download the file and save it to the 'downloaded_files' directory
        file_response = requests.get(file_url)
        
        # Step 6: Check if the request was successful (status code 200)
        if file_response.status_code == 200:
            with open(os.path.join('downloaded_files', file_name), 'wb') as f:
                f.write(file_response.content)
            print(f"Downloaded {file_name}")
        else:
            print(f"Failed to download {file_name}")
    else:
        # Just print the links that are not downloadable files
        print(f"Link found: {file_url}")

print("File download process complete!")
