flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
]

city_codes = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur"
}

def search_by_city(flight_data, city):
    city_flights = [flight for flight in flight_data if flight["From"] == city or flight["To"] == city]
    return city_flights

def search_flights_from_city(flight_data, city):
    flights_from_city = [flight for flight in flight_data if flight["From"] == city]
    return flights_from_city

def search_flights_between_cities(flight_data, city1, city2):
    flights_between_cities = [flight for flight in flight_data if (flight["From"] == city1 and flight["To"] == city2) or (flight["From"] == city2 and flight["To"] == city1)]
    return flights_between_cities

print("Search Options:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    city = input("Enter the city code: ")
    city_flights = search_by_city(flight_data, city)
    for flight in city_flights:
        print(f"Flight ID: {flight['Flight ID']}, From: {city_codes[flight['From']]}, To: {city_codes[flight['To']]}, Price: {flight['Price']}")

elif choice == 2:
    city = input("Enter the city code: ")
    flights_from_city = search_flights_from_city(flight_data, city)
    for flight in flights_from_city:
        print(f"Flight ID: {flight['Flight ID']}, From: {city_codes[flight['From']]}, To: {city_codes[flight['To']]}, Price: {flight['Price']}")

elif choice == 3:
    city1 = input("Enter the first city code: ")
    city2 = input("Enter the second city code: ")
    flights_between_cities = search_flights_between_cities(flight_data, city1, city2)
    for flight in flights_between_cities:
        print(f"Flight ID: {flight['Flight ID']}, From: {city_codes[flight['From']]}, To: {city_codes[flight['To']]}, Price: {flight['Price']}")

else:
    print("Invalid choice")
