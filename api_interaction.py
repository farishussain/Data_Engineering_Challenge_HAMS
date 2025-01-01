import requests

API_URL = "https://api.ihc-attribution.com/v1/compute_ihc"
API_KEY = "your_api_key"
CONV_TYPE_ID = "data_engineering_challenge"

def call_ihc_api(journeys):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    results = []
    for chunk in [journeys[i:i+10] for i in range(0, len(journeys), 10)]:
        response = requests.post(
            f"{API_URL}?conv_type_id={CONV_TYPE_ID}",
            headers=headers,
            json={"customer_journeys": chunk}
        )
        if response.status_code == 200:
            results.extend(response.json().get("value", []))
        else:
            print(f"API Error: {response.text}")
    return results

if __name__ == "__main__":
    from transform_data import build_customer_journeys
    from query_data import fetch_data

    session_sources, conversions = fetch_data()
    customer_journeys = build_customer_journeys(session_sources, conversions)
    api_results = call_ihc_api(customer_journeys)
    print("API Results:", api_results[0])