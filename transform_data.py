def build_customer_journeys(session_sources, conversions):
    journeys = []
    for _, conv in conversions.iterrows():
        print(f"Processing conversion: {conv['conv_id']}")
        user_sessions = session_sources[
            (session_sources["user_id"] == conv["user_id"]) &
            (session_sources["event_date"] + " " + session_sources["event_time"] <
             conv["conv_date"] + " " + conv["conv_time"])
        ]
        print(f"Found {len(user_sessions)} sessions for user {conv['user_id']} before conversion")
        customer_journey = user_sessions.to_dict("records")
        journeys.append({
            "conversion_id": conv["conv_id"],
            "customer_journey": customer_journey
        })
    return journeys

if __name__ == "__main__":
    from query_data import fetch_data
    session_sources, conversions = fetch_data()
    print(f"Fetched {len(session_sources)} session sources and {len(conversions)} conversions")
    customer_journeys = build_customer_journeys(session_sources, conversions)
    print("Sample Customer Journey:", customer_journeys[0])