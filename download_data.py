import requests
import os

# Define the URL and local folder
url = "https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv"
folder_path = "data"
file_path = os.path.join(folder_path, "AB_NYC_2019.csv")

# Create the folder if it doesn’t exist
os.makedirs(folder_path, exist_ok=True)

# Download and save the file
response = requests.get(url)
with open(file_path, "wb") as file:
    file.write(response.content)

print(f"File downloaded successfully and saved as {file_path}")
