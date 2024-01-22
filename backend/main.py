from fastapi import FastAPI, HTTPException, BackgroundTasks
from typing import List
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import googlemaps
import time
from fastapi.middleware.cors import CORSMiddleware

load_dotenv('.env')

API_KEY = os.getenv("API_KEY")
gmaps = googlemaps.Client(key=API_KEY)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlaceDetails(BaseModel):
    name: str
    address: str
    phone_number: str
    url: str

# Define a list to store the scraped place details
Places: List[PlaceDetails] = []

def clear_places_list():
    # Clear the Places list after some time (e.g., 30 seconds)
    time.sleep(30)
    Places.clear()

@app.get("/api", response_model=List[PlaceDetails])
def scrape_places(location: str, keyword: str, background_tasks: BackgroundTasks):
    try:
        geocode_result = gmaps.geocode(location)
        location = geocode_result[0]['geometry']['location']

        places_result = gmaps.places_nearby(
            location=location,
            radius=10 * 1000,
            keyword=keyword,
        )

        for place in places_result.get('results', []):
            place_id = place['place_id']
            
            # Fetch details for the current place ID
            place_details = gmaps.place(place_id=place_id, fields=['formatted_phone_number', 'url'])
            
            # Extract details
            name = place['name']
            address = place['vicinity']
            phone_number = place_details['result'].get('formatted_phone_number', '')
            url = place_details['result'].get('url', '')

            # Create PlaceDetails instance and add to the list
            Places.append(PlaceDetails(name=name, address=address, phone_number=phone_number, url=url))

        while 'next_page_token' in places_result:
            next_page_token = places_result['next_page_token']

            time.sleep(2)

            places_result = gmaps.places_nearby(
                location=location,
                radius=10 * 1000,
                keyword=keyword,
                page_token=next_page_token
            )

            for place in places_result.get('results', []):
                place_id = place['place_id']
                
                # Fetch details for the current place ID
                place_details = gmaps.place(place_id=place_id, fields=['formatted_phone_number', 'url'])
                
                # Extract details
                name = place['name']
                address = place['vicinity']
                phone_number = place_details['result'].get('formatted_phone_number', '')
                url = place_details['result'].get('url', '')

                # Create PlaceDetails instance and add to the list
                Places.append(PlaceDetails(name=name, address=address, phone_number=phone_number, url=url))

        # Schedule the background task to clear the Places list after some time
        background_tasks.add_task(clear_places_list)

        # Return the list if needed
        return Places

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
