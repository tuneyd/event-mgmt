from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# mock data
events_data = [
                      {"event_id": 1, "category": "Academic", "registrations": 150, "date": "2023-03-15"},
                      {"event_id": 2, "category": "Professional Development", "registrations": 100,
                       "date": "2023-04-20"},
                      {"event_id": 3, "category": "Workshop", "registrations": 80, "date": "2023-05-11"},
                      {"event_id": 4, "category": "Seminar", "registrations": 90, "date": "2023-06-05"},
                      {"event_id": 5, "category": "Webinar", "registrations": 200, "date": "2023-07-19"},
                      {"event_id": 6, "category": "Networking", "registrations": 160, "date": "2023-08-12"},
                      {"event_id": 7, "category": "Team Building", "registrations": 50, "date": "2023-09-30"},
                      {"event_id": 8, "category": "Product Launch", "registrations": 180, "date": "2023-10-16"},
                      {"event_id": 9, "category": "Panel Discussion", "registrations": 75, "date": "2023-11-04"},
                      {"event_id": 10, "category": "Career Fair", "registrations": 300, "date": "2023-11-20"},
                      {"event_id": 11, "category": "Round Table", "registrations": 40, "date": "2023-12-01"},
                      {"event_id": 12, "category": "Academic", "registrations": 120, "date": "2024-01-15"},
                      {"event_id": 13, "category": "Professional Development", "registrations": 110,
                       "date": "2024-02-18"},
                      {"event_id": 14, "category": "Workshop", "registrations": 90, "date": "2024-03-21"},
                      {"event_id": 15, "category": "Seminar", "registrations": 85, "date": "2024-04-10"},
                      {"event_id": 16, "category": "Webinar", "registrations": 250, "date": "2024-05-25"},
                      {"event_id": 17, "category": "Networking", "registrations": 175, "date": "2024-06-30"},
                      {"event_id": 18, "category": "Team Building", "registrations": 60, "date": "2024-07-28"},
                      {"event_id": 19, "category": "Product Launch", "registrations": 190, "date": "2024-08-15"},
                      {"event_id": 20, "category": "Panel Discussion", "registrations": 65, "date": "2024-09-10"}
]


@app.route('/api/report/events-overview')
def events_overview():
    # For now, it's just returning the mock data as-is without partner's end point.
    return jsonify(events_data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)