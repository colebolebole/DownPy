import requests
import os
from tqdm import tqdm

def download_file(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Auto-detect file extension from the URL or provided save path
            _, file_extension = os.path.splitext(url) if '.' in url else os.path.splitext(save_path)
            # Generate a unique file name if save_path is a directory
            if os.path.isdir(save_path):
                file_name = url.split('/')[-1] if '/' in url else 'downloaded_file'
                save_path = os.path.join(save_path, file_name)
            # Get the total file size
            total_size = int(response.headers.get('content-length', 0))
            # Initialize the progress bar
            progress = tqdm(total=total_size, unit='B', unit_scale=True)
            # Open a file in binary write mode and write the downloaded content
            with open(save_path, 'wb') as f:
                for data in response.iter_content(chunk_size=1024):
                    # Write data to file
                    f.write(data)
                    # Update progress bar
                    progress.update(len(data))
            # Close the progress bar
            progress.close()
            print("\nFile downloaded successfully!")
            print("File saved as:", save_path)
            print("File size:", round(total_size / 1024, 2), "KB")
        else:
            print("Failed to download file. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

def main():
    url = input("Enter the URL of the file you want to download: ")
    save_path = input("Enter the path where you want to save the file")

    download_file(url, save_path)

if __name__ == "__main__":
    main()
