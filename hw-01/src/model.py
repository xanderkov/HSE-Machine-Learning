from loguru import logger
import pickle
from sklearn.linear_model import Ridge



def load_model(path: str) -> tuple[Ridge, list]:
    with open(path, 'rb') as file:
        loaded_data = pickle.load(file)

    loaded_model = loaded_data['model']
    loaded_metric = loaded_data['business_metric']

    logger.info(f"Загруженная модель: {loaded_model}")
    logger.info(f"Загруженная метрика: {loaded_metric}")
    logger.info(f"Тренировочные столбцы: {loaded_data['columns']}")

    return loaded_model, loaded_data['columns']

model, columns = load_model("./data/best_ridge_model.pkl")