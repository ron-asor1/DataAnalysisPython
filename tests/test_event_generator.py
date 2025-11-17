from app.services.EventGenerator import EventGenerator

def test_generate_pageview_event():
    generator = EventGenerator()
    evnet = generator.generate_pageview_event()
    assert evnet.event_type == "page_view"
    assert evnet.product_id == '5'
    assert evnet.product_name == 'product_5'
    assert evnet.product_price == 99.99 

def test_generate_purchase_event():
    generator = EventGenerator()
    evnet = generator.generate_purchase_event()
    assert evnet.event_type == "purchase"
    assert evnet.product_id == '5'
    assert evnet.product_name == 'product_5'
    assert evnet.product_price == 99.99