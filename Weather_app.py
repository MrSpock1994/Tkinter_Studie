from tkinter import *
import requests
import json


root = Tk()
root.title("Weather app")
root.geometry("300x120")


def weather():
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/"
                                   "json&zipCode="+str(zipcode.get())+"&distance=5&API_KEY=0A439353-009B-45F3-B0A1-"
                                                                      "05411EB9DD13")
    api = json.loads(api_request.content)
    city = api[0]["ReportingArea"]
    category = api[0]["Category"]["Name"]
    quality = api[0]["AQI"]

    if category == "Good":
        back_color = "green"
    elif category == "Moderate":
        back_color = "yellow"
    elif category == "Unhealthy for Sensitive Groups":
        back_color = "Orange"
    else:
        back_color = "Red"

    root.configure(background=back_color)
    mylabel = Label(root, text="City: " + city, background=back_color)
    mylabel.grid(row=3, column=0)
    mylabel = Label(root, text="Air Quality: " + str(quality), background=back_color)
    mylabel.grid(row=4, column=0)
    mylabel = Label(root, text="Category: " + category, background=back_color)
    mylabel.grid(row=5, column=0)


label_code = Label(root, text="Zipcode ->")
label_code.grid(row=1, column=0)
zipcode = Entry(root, width=10)
zipcode.grid(row=1, column=1)
weather_btn = Button(root, text="Insert the zipcode below", command=weather)
weather_btn.grid(row=0, column=0, columnspan=2)

root.mainloop()
