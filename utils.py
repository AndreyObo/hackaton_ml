from typing import Optional
from pydantic import BaseModel


#Модель для передачи признаков в ml модель
class ModelParams(BaseModel):
    utm_source: str
    utm_medium: str
    utm_campaign: str
    utm_adcontent: str
    device_category: str
    device_brand: Optional[str] = None
    device_browser: str
    utm_source_initial: Optional[str] = None
    device_os_filled: Optional[str] = None
    day_part: Optional[str] = None
    direct_cat_link: Optional[str]= None
    is_weekend: Optional[str] = None


#Модель для http запроса
class QueryParams(BaseModel):
    utm_source: str
    utm_medium: str
    utm_campaign: str
    utm_adcontent: str
    device_category: str
    device_brand: Optional[str] = None
    device_browser: str
    device_os: str
    hit_page_path: str
    visit_time:str
    visit_date:str
