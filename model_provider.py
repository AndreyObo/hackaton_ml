from catboost import CatBoostClassifier
from .utils import QueryParams, ModelParams
from datetime import datetime
import json
import re

NONE_TAG = 'NaN'

# Класс для загрузки модели
# трансформации запроса к классу типа входных признаков
# выполнения предсказаний модели

class ModelProvider:
    def __init__(self):
        self.model = None
        self.model_info = None
        
    def load_model(self, model_name:str):
        self.model = CatBoostClassifier()
        self.model.load_model(f'./models/{model_name}.cbm')

        with open(f'./models/{model_name}_info.json', 'r', encoding='utf-8') as f:
            self.model_info = json.load(f)

    # В ходе исследований мы заменили все None на класс NaN. Для входных признаков делаем тоже самое 
    def _check_Nan(self, value):
        return NONE_TAG if value is None else value
    

    from datetime import datetime

    def _get_day_part(self, visit_time: str) -> str:
        try:
            dt_obj = datetime.strptime(visit_time, '%H:%M:%S')
        except:
            return NONE_TAG
        
        hour = dt_obj.hour
        
        if 0 <= hour < 7:
            return 'night'
        elif 7 <= hour < 10:
            return 'morning'
        elif 10 <= hour < 14:
            return 'day'
        elif 14 <= hour < 18:
            return 'afternoon'
        elif 18 <= hour < 22:
            return 'evening'
        else:
            return 'l_evening'
        
    def _is_weekend(self, visit_date: str) -> str:
        try:
            dt_obj = datetime.strptime(visit_date, '%Y-%m-%d') 
        except:
            return NONE_TAG
        return str(dt_obj.weekday() in [5, 6])


    def _transform_data(self, data:QueryParams)->ModelParams:
        #Скоприуем все совпадающие поля
        model_data = ModelParams(**data.model_dump())

        #По остальным выполним трансформацию в ручную

        model_data.device_os_filled = str(data.device_os)

        reg = re.search(r'utm_source_initial=([^&]+)', data.hit_page_path)
        if reg:
            model_data.utm_source_initial = reg.group(1)
        else:
            model_data.utm_source_initial = NONE_TAG

        model_data.direct_cat_link = str(bool(re.search(r'/cars/all/', data.hit_page_path)))

        model_data.day_part = self._get_day_part(data.visit_time)
        model_data.is_weekend = self._is_weekend(data.visit_date)

        return model_data
        

    def predict(self, params:QueryParams):
        if self.model is None:
            raise "Модель не загружена"
        
        model_params = self._transform_data(params)
        model_data = model_params.model_dump()
        
        try:
            #Для восстановления порядка признаков воспользуемся сохраненным json конфигом
            features = [model_data[col] for col in self.model_info['feature_names']]

            prediction = self.model.predict([features])
            print(prediction)
            return str(prediction[0])
        except BaseException as e:
            raise Exception(f'Возникла ошибка при загрузке праметров в модель: {e}')
        

    def get_model_info(self):
        return self.model_info

        
            