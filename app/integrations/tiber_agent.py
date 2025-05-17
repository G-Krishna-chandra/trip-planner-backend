from intel_extension_for_transformers.transformers import DeepSeekModel
import json

# Load the model once (make sure the model is available in your Tiber notebook)
model = DeepSeekModel.from_pretrained("deepseek-ai/deepseek-coder-6.7b-instruct")

def generate_itinerary_with_tiber(trip_request):
    prompt = (
        f"Create a detailed travel itinerary for a trip to {trip_request.destination}.\n"
        f"Start date: {trip_request.start_date}\n"
        f"End date: {trip_request.end_date}\n"
        f"Budget: ${trip_request.budget}\n"
        f"Preferences: {', '.join(trip_request.preferences)}\n"
        "Make cost estimates realistic based on the type of activity, and break it down day by day. "
        "Return the output in JSON format with 'day', 'activity', and 'cost'. Also include a 'total_cost' at the end."
    )

    try:
        result = model.generate(
            prompt=prompt,
            max_new_tokens=500,
            temperature=0.7
        )
        return json.loads(result)
    except Exception as e:
        return {
            "itinerary": [],
            "total_cost": 0,
            "error": str(e)
        }

