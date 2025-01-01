import sqlite3

DB_FILE = "challenge.db"

def insert_results(results):
    with sqlite3.connect(DB_FILE) as conn:
        for result in results:
            for session in result["sessions"]:
                conn.execute("""
                    INSERT INTO attribution_customer_journey (conv_id, session_id, ihc)
                    VALUES (?, ?, ?);
                """, (result["conversion_id"], session["session_id"], session["ihc"]))
        conn.commit()
        print("Results inserted successfully.")

if __name__ == "__main__":
    from api_interaction import call_ihc_api
    from transform_data import build_customer_journeys
    from query_data import fetch_data

    session_sources, conversions = fetch_data()
    customer_journeys = build_customer_journeys(session_sources, conversions)
    api_results = call_ihc_api(customer_journeys)
    insert_results(api_results)