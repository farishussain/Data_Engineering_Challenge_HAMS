from db_init import initialize_database
from query_data import fetch_data
from transform_data import build_customer_journeys
from api_interaction import call_ihc_api
from store_results import insert_results
from generate_report import generate_report

if __name__ == "__main__":
    initialize_database()
    session_sources, conversions = fetch_data()
    customer_journeys = build_customer_journeys(session_sources, conversions)
    api_results = call_ihc_api(customer_journeys)
    insert_results(api_results)
    generate_report()