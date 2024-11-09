from fastapi import APIRouter, Depends
from schemas import Item, Items
from service import predict_item_service, predict_items_service
router = APIRouter(
    responses={404: {"description": "Not found"}},
)




@router.post("/predict_item")
def predict_item(item: Item) -> float:
    return predict_item_service(item)


@router.post("/predict_items")
def predict_items(items: Items) -> list[float]:
    return predict_items_service(items)