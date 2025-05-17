from pydantic import BaseModel
from typing import List

class ItineraryItem(BaseModel):
    day: str
    activity: str
    cost: float

class TripRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    preferences: List[str]
    budget: float

class TripResponse(BaseModel):
    itinerary: List[ItineraryItem]
    total_cost: float

