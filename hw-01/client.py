import requests

predict_item = 'http://0.0.0.0:7777/predict_item'
predict_items = 'http://0.0.0.0:7777/predict_items'

data = {"objects":
    [
        {
        "name": "string",
        "year": 0,
        "selling_price": 0,
        "km_driven": 0,
        "fuel": "string",
        "seller_type": "string",
        "transmission": "string",
        "owner": "string",
        "mileage": "1",
        "engine": "1",
        "max_power": "1",
        "torque": "string",
        "seats": 0
        }
    ]
}

x = requests.post(predict_item, json=data["objects"][0])
y = requests.post(predict_items, json=data)

print(x.text)
print(y.text)