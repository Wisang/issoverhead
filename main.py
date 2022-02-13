import requests
from datetime import datetime
import smtplib

MY_LAT = 37.566536 # Your latitude
MY_LONG = 126.977966 # Your longitude

my_email = "testwisangeom@gmail.com"
my_password = "eomm9409"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_close():
    return  abs(MY_LAT - iss_latitude) < 5.0 and abs(MY_LONG - iss_longitude) < 5.0

def is_dark():
    return time_now.hour > sunset


def send_mail(mail_body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr="testwisangeom@gmail.com",
            to_addrs="testwisangeom@yahoo.com",
            msg=f"Subject:Python Exercise\n\n{mail_body}")


if is_dark() and is_close():
    send_mail("Look up!")



