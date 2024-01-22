from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import googlemaps
import csv
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

@app.get("/api", response_model=List[PlaceDetails])
def scrape_places():
    try:
        area_name = 'Pimpri'
        place_keyword = 'diagnostic center'
        radius_in_km = 10

        geocode_result = gmaps.geocode(area_name)
        location = geocode_result[0]['geometry']['location']

        places_result = gmaps.places_nearby(
            location=location,
            radius=radius_in_km * 1000,
            keyword=place_keyword,
        )
        all_place_details = []

        all_place_details.extend([
            PlaceDetails(
                name=place['name'],
                address=place['vicinity'],
                phone_number='',
                url=''
            )
            for place in places_result.get('results', [])
        ])

        # Check if there are more pages and retrieve them
        while 'next_page_token' in places_result:
            next_page_token = places_result['next_page_token']

            # Pause for a short time to allow the next page to be generated
            time.sleep(2)

            # Make a request with the page token to get the next page of results
            places_result = gmaps.places_nearby(
                location=location,
                radius=radius_in_km * 1000,
                keyword=place_keyword,
                page_token=next_page_token
            )

            all_place_details.extend([
                PlaceDetails(
                    name=place['name'],
                    address=place['vicinity'],
                    phone_number='',
                    url=''
                )
                for place in places_result.get('results', [])
            ])

        return all_place_details

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
