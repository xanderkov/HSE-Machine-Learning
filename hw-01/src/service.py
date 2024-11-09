from loguru import logger
from fastapi import HTTPException
from schemas import Item, Items
from model import model, columns
import numpy as np

def transform_input(item: Item):
    input_data = {
        'year': int(item.year),
        'km_driven': float(item.km_driven),
        'mileage': float(item.mileage),
        'engine': float(item.engine),
        'max_power': float(item.max_power),
    }
    for column in columns:
        if "name_" or "fuel_" or "seller_type_" or "transmission_" or "owner_" or "seats_" in column:
            input_data[column] = 1 if item.name.startswith(item.name) else 0

    feature_array = np.array([list(input_data.values())])
    return feature_array

def predict_item_service(item: Item) -> float:
    try:
        prediction = model.predict(transform_input(item))
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=422, detail="Bad input")
    return prediction[0]


def predict_items_service(items: Items) -> list[float]:
    predictions = []
    try:
        for item in items.objects:
            prediction = model.predict(transform_input(item))
            predictions.append(prediction[0])
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=422, detail="Bad input")

    
    return predictions