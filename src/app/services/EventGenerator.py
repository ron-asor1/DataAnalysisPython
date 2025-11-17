from app.Events import event_pageView, event_Purchase
import time
import random

usedEvenetIds = set()
usedUserIds = set()
usedSessionIds = set()


class EventGenerator:
    def __init__(self):
        pass

    def generate_pageview_event(self):
        return event_pageView(
            event_id=get_unique_event_id(),
            event_type="page_view",
            timestamp=time.time(),
            user_id=get_unique_used_id(),
            session_id=get_unique_used_id(),
            product_id='5',
            product_name='product_5',
            product_price=99.99
        )

    def generate_purchase_event(self):
        return event_Purchase(
            event_id=get_unique_event_id(),
            event_type="purchase",
            timestamp=time.time(),
            user_id=get_unique_used_id(),
            session_id=get_unique_session_id(),
            product_id='5',
            product_name='product_5',
            product_price=99.99
        )

def get_unique_event_id():
    while True:
        event_id=random.randint(0000, 9999)
        if (event_id not in usedEvenetIds):
            usedEvenetIds.add(event_id)
            return str(event_id)

def get_unique_used_id():
    while True:
        user_id=random.randint(0000, 9999)
        if (user_id not in usedUserIds):
            usedUserIds.add(user_id)
            return str(user_id)
        
def get_unique_session_id():
    while True:
        sessions_id=random.randint(0000, 9999)
        if (sessions_id not in usedSessionIds):
            usedSessionIds.add(sessions_id)
            return str(sessions_id)
