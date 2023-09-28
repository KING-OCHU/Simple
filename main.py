import requests
from bs4 import BeautifulSoup
import time

# Define the URL to scrape
url = input("Enter your pushing link:  ")

# Initial data
previous_data = ""

# Function to scrape and print data
def scrape_and_print_data():
    global previous_data

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract phone manufacturer, phone name, battery charger parameters, and IP address based on HTML structure
        manufacturer = soup.find("span", {"class": "manufacturer"}).text
        phone_name = soup.find("span", {"class": "phone-name"}).text
        charger_parameters = soup.find("span", {"class": "charger-params"}).text
        ip_address = soup.find("span", {"class": "ip-address"}).text

        # Construct the data string
        data = f"Phone Manufacturer: {manufacturer}\nPhone Name: {phone_name}\nCharger Parameters: {charger_parameters}\nIP Address: {ip_address}\n"

        # Check if the data has changed
        if data != previous_data:
            print(data)
            # Save data to a file
            with open('infoga.tex', 'a') as f:
                f.write(data)

            previous_data = data

# Add a loop to continuously check for changes and print data
while True:
    scrape_and_print_data()
    time.sleep(5)  # Wait for 5 seconds before checking again
