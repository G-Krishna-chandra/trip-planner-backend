from fastapi import APIRouter
from app.schemas import TripRequest, TripResponse
from app.integrations.tiber_agent import generate_itinerary_with_tiber

router = APIRouter()

@router.post("/plan-trip/", response_model=TripResponse)
async def plan_trip(trip: TripRequest):
    return await generate_itinerary_with_tiber(trip)

