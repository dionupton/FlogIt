import os
import requests
import time
import json
from datetime import datetime, timedelta
import random
import pandas as pd
import schedule
import pytz

GATEWAY_API_URL = os.getenv('GATEWAY_API_URL') or 'http://localhost:6001'
IDENTITY_URL = os.getenv('IDENTITY_URL') or 'http://localhost:5000'

auctions_data = None  # Initial declaration of fetched auctions

# Initial setup for token request
token_url = IDENTITY_URL + "/connect/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Separate function to get access token for a specific user
def get_access_token_for(username):
    token_data = {
        "grant_type": "password",
        "username": username,
        "password": "Pass123$",
        "client_id": "pybot",
        "client_secret": "NotASecret",
        "scope": "auctionApp openid profile"
    }

    while True:
        response = requests.post(token_url, headers=headers, data=token_data)
        if response.status_code == 200:
            return response.json().get("access_token")
        print(f"Failed to retrieve the token for {username}. Retrying in 1 minute...")
        time.sleep(60)
        
# Getting both tokens initially
bob_token = get_access_token_for("bob")
alice_token = get_access_token_for("alice")

# Function to generate a random auction end datetime
def random_auction_end():
    one_hour = timedelta(hours=1)
    one_day = timedelta(days=1)
    random_duration = one_hour + timedelta(seconds=random.randint(0, int((one_day - one_hour).total_seconds())))
    return (datetime.utcnow() + random_duration).isoformat() + "Z"

# Read image URLs from the file
with open('resources/image_urls.txt', 'r') as file:
    # strip() to remove whitespace and newlines, replace() to remove quotes and commas
    links = [line.strip().replace('"', '').replace(',', '') for line in file.readlines()]

# Extract key and information from link
def extract_key_from_link(link):
    parts = link.split("/")[-1].split("_")[0].split("-")
    colour = parts[-1]
    make = parts[0]
    model = '-'.join(parts[1:-1])
    return f"{make}-{model}-{colour}", link

# Extract make, model, and colour from the dictionary key
def extract_info_from_key(key):
    parts = key.split("-")
    colour = parts[-1]
    make = parts[0]
    model_parts = parts[1:-1]
    model = ' '.join(model_parts)
    return make, model, colour


link_dict = {extract_key_from_link(link)[0]: extract_key_from_link(link)[1] for link in links}

for key, link in link_dict.items():
    make, model, colour = extract_info_from_key(key)
    print(f"Make: {make}, Model: {model}, Colour: {colour}")


def fetch_auctions_and_store():
    global auctions_data  # Reference the global variable
    response = requests.get(GATEWAY_API_URL + '/auctions')
    response.raise_for_status()
    auctions_data = pd.DataFrame(response.json())

# Initially call the fetch_auctions_and_store to populate the auctions_data variable
fetch_auctions_and_store()
print(auctions_data.head())

def create_auction():
    auction_url = GATEWAY_API_URL + "/auctions"
    dateString = random_auction_end()
    chosen_key, chosen_link = random.choice(list(link_dict.items()))
    make, model, colour = extract_info_from_key(chosen_key)
    make, model, colour = make.lower().capitalize(), model.lower().capitalize(), colour.lower().capitalize()
    
    headers_for_create = {
        "Authorization": f"Bearer {bob_token}",
        "Content-Type": "application/json"
    }

    # Raw JSON body for the auction request with random values
    body = {
        "make": make,
        "model": model,
        "colour": colour,
        "year": str(random.randint(2000, 2023)),  # Random year between 2000 and 2023
        "mileage": str(random.randint(5000, 100000)),  # Random mileage between 5,000 and 100,000
        "imageUrl": chosen_link,
        "reservePrice": random.randint(1000, 50000),  # Random reserve price between 1,000 and 50,000
        "auctionEnd": dateString
        }

    response = requests.post(auction_url, headers=headers_for_create, data=json.dumps(body))

    if response.status_code == 403 | 401:  # Forbidden, meaning the token might have expired or is not valid
        print("Access denied. Re-obtaining token...")
        token = get_access_token_for('bob')
        headers["Authorization"] = f"Bearer {token}"

    print(response.status_code)
    print(response.text)

def place_bid():
    print('in place bid')
    global auctions_data  # Reference the global variable
    
    # It's possible that the function is called before the auctions_data is populated. So, check for its existence.
    if auctions_data is None:
        print("No auctions data available yet.")
        return
    
    # Convert current UTC time to a timezone-aware datetime object
    current_utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)

    # Convert 'auctionEnd' column to datetime format
    auction_end_dates = pd.to_datetime(auctions_data['auctionEnd'], format='ISO8601')
    
    # Filter the auctions based on the provided conditions
    valid_auctions = auctions_data[(auctions_data['seller'] != 'alice') & (auction_end_dates > current_utc_time)]
    
    # If no valid auctions, print a message and return
    if valid_auctions.empty:
        print("No valid auctions to bid on!")
        return

    # Randomly choose an auction from the filtered auctions
    auction = valid_auctions.sample(n=1).iloc[0]
    
    # Calculate the bid amount
    current_high_bid = auction['currentHighBid']
    bid_amount = current_high_bid + random.randint(1, 10)
    
    headers_for_bid = {
        "Authorization": f"Bearer {alice_token}",
        "Content-Type": "application/json"
    }
    
    # Construct the URL and make the POST request
    url = f"{GATEWAY_API_URL}/bids?auctionId={auction['id']}&amount={bid_amount}"
    response = requests.post(url, headers=headers_for_bid)
    
    # Print the response
    if response.status_code == 200:
        print(f"Successfully placed a bid of £{bid_amount} for auction {auction['id']}")
    else:
        print(f"Failed to place bid. Status code: {response.status_code}. Response: {response.text}")
        if(response.status_code == 401 | 403) : get_access_token_for('alice')

    
# schedule the functions
random_time_for_place_bid = random.randint(10, 24)
schedule.every(random_time_for_place_bid).seconds.do(place_bid)

schedule.every(600).seconds.do(create_auction)

schedule.every(3).minutes.do(fetch_auctions_and_store)

while True:
    schedule.run_pending()
    time.sleep(1)
