# Map Guesser Backend

## Setup

Make sure you are using Python 3.14 or above

Install the following:
```
pip install fastapi uvicorn geopy certifi pycountry geopandas matplotlib motor
```

Now run the following for Macbook:
```
/Applications/Python\ 3.14/Install\ Certificates.command
```
If you are using another version of Python, then replace 3.14 with your Python version in the above command.

## Run

Run the following command on Terminal from the root folder:
```
python3 -m uvicorn main:app --reload
```

Navigate to your browser and search for the following:
```
http://127.0.0.1:8000/docs
```

Use Swagger to test and play around with the API

## Map Update

If maps outlines change, download the data from the below website:
https://www.naturalearthdata.com/downloads/110m-cultural-vectors/
