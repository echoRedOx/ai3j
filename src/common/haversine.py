import math

def haversine(lat1, lon1, lat2, lon2):
    """This is an as-the-crow-flies distance formula. I promise it is useful for something cool."""
    # Convert lat/long to radians because math.
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371  # Radius of Earth in kilometers
    distance_km = r * c

    # Convert kilos to nautical miles (1 nautical mile = 1.852 km)
    distance_nm = distance_km / 1.852

    # Convert distance in nautical miles to degrees, minutes, and seconds
    total_seconds = distance_nm * 3600  # Total seconds in the distance
    degrees = int(total_seconds // 3600)
    total_seconds %= 3600
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60

    return degrees, minutes, seconds


def main():
    lat1, lon1 = 31.30568457478846, -85.40946691943792  # Dothan
    lat2, lon2 = 35.913408485670935, -86.83865575321478  # Franklin

    degrees, minutes, seconds = haversine(lat1, lon1, lat2, lon2)
    
    print(f"Distance: {degrees}° {minutes}' {seconds:.2f}''")


if __name__ == "__main__":
    main()