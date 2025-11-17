from dataclasses import dataclass

@dataclass
class event_basic:
    event_id : str
    event_type: str
    timestamp: str
    user_id: str
    session_id: str

@dataclass
class event_pageView(event_basic):
    product_id: str
    product_name: str
    product_price: float

@dataclass
class event_Purchase(event_basic):
    product_id: str
    product_name: str
    product_price: float
