from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent.parent

INPUT = BASE / "data" / "processed" / "candidate_tracks.csv"
OUTPUT = BASE / "data" / "processed" / "candidate_tracks_sorted.csv"

if not INPUT.exists():
    raise FileNotFoundError(f"File not found: {INPUT}")

df = pd.read_csv(INPUT)
# CONVERT TIMESTAMP
df["base_date_time"] = pd.to_datetime(
    df["base_date_time"],
    utc=True,
    errors="coerce"
)
# SORT EACH VESSEL CHRONOLOGICALLY
df = df.sort_values(
    ["mmsi", "base_date_time"]
).reset_index(drop=True)
# CALCULATE TIME BETWEEN AIS OBSERVATIONS
df["time_diff_seconds"] = (
    df.groupby("mmsi")["base_date_time"]
    .diff()
    .dt.total_seconds()
)
df["trajectory_start"] = (
    df["time_diff_seconds"].isna()
)
df.to_csv(
    OUTPUT,
    index=False
)
print("Trajectory reconstruction complete.")
print(f"Observations: {len(df):,}")
print(f"Vessels: {df['mmsi'].nunique():,}")
print(f"Output: {OUTPUT}")