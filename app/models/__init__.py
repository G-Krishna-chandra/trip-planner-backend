from pydantic import BaseModel
from typing import List, Optional

class TripRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    preferences: List[str]
    budget: float

class ItineraryItem(BaseModel):
    day: str
    activity: str
    cost: float

class TripResponse(BaseModel):
    itinerary: List[ItineraryItem]
    total_cost: float

