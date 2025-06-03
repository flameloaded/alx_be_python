
weather = input("what's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear sunglasses and stay hydrated!")
elif weather == "rainy":
    print("Take an umbrella with you.")
elif weather == "cold":
    print("Wear a warm jacket.")
else:
    print("Sorry, I don't have advice for that weather.")
