from flask import Flask, render_template, jsonify
from src.app.main import EventManager

event_manager = EventManager()  # shared instance

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/trigger_pageview', methods=['POST'])
    def trigger_pageview():
        event = event_manager.generate_pageview()
        return jsonify({"status": "Pageview event generated", "event": event.__dict__})

    @app.route('/trigger_purchase', methods=['POST'])
    def trigger_purchase():
        event = event_manager.generate_purchase()
        return jsonify({"status": "Purchase event generated", "event": event.__dict__})

    return app
