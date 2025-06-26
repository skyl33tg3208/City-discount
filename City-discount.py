cities = ["Miami", "Arizona", "Los Angeles", "Boston"]

user_city = input('Please enter the name of your city:')

if user_city in cities:
    response = f"Yes, {user_city} is in our list of cities, so you get a discount!"
    print(response)
else:
    print("Sorry you are not eligible for a discount")