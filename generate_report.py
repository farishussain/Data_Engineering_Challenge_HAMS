import sqlite3
import pandas as pd

DB_FILE = "challenge.db"
OUTPUT_CSV = "channel_reporting.csv"

def generate_report():
    query = """
    SELECT
        s.channel_name,
        s.event_date AS date,
        SUM(sc.cost) AS cost,
        SUM(acj.ihc) AS ihc,
        SUM(acj.ihc * c.revenue) AS ihc_revenue
    FROM session_sources s
    JOIN session_costs sc ON s.session_id = sc.session_id
    JOIN attribution_customer_journey acj ON s.session_id = acj.session_id
    JOIN conversions c ON acj.conv_id = c.conv_id
    GROUP BY s.channel_name, s.event_date;
    """
    with sqlite3.connect(DB_FILE) as conn:
        df = pd.read_sql(query, conn)
    df["CPO"] = df["cost"] / df["ihc"]
    df["ROAS"] = df["ihc_revenue"] / df["cost"]
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Report exported to {OUTPUT_CSV}.")

if __name__ == "__main__":
    generate_report()