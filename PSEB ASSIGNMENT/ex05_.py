temp =int(input("Enter temperature in celcius: "))
if temp < 10:
    print("Cold,wear a jacket")
elif temp > 10 and temp < 25:
        print("pleasant")
elif temp > 26 and temp < 35:
        print("warm")
else:
       print("Very hot,stay hydrated")