from app.integrations.tiber_agent import get_activity_estimate

def generate_itinerary(destination: str, start_date: str, end_date: str, preferences: list, budget: float):
    from datetime import datetime

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    days = (end - start).days + 1

    itinerary = []
    total_cost = 0.0

    for i in range(days):
        pref = preferences[i % len(preferences)]
        description, cost = get_activity_estimate(destination, pref)
        total_cost += cost
        itinerary.append({
            "day": f"Day {i + 1}",
            "activity": description,
            "cost": cost
        })

    remaining = max(0, budget - total_cost)
    return {
        "itinerary": itinerary,
        "total_cost": total_cost,
        "remaining_budget": remaining
    }

