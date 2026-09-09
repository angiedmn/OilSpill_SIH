from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
INPUT = BASE / "data" / "processed" / "candidate_tracks_sorted.csv"
OUTPUT = BASE / "data" / "processed" / "vessel_features.csv"
if not INPUT.exists():
    raise FileNotFoundError(f"File not found: {INPUT}")

df = pd.read_csv(INPUT)

# CONVERT TIMESTAMP
df["base_date_time"] = pd.to_datetime(
    df["base_date_time"],
    utc=True,
    errors="coerce"
)

# SORT
df = df.sort_values(
    ["mmsi", "base_date_time"]
).reset_index(drop=True)
# TIME DIFFERENCE
df["time_diff_seconds"] = (
    df.groupby("mmsi")["base_date_time"]
    .diff()
    .dt.total_seconds()
)
# AIS GAPS
df["ais_gap"] = (
    df["time_diff_seconds"] > 600
)
# STOPPED OBSERVATIONS
df["stopped"] = (
    df["sog"].fillna(0) <= 0.5
)
# VESSEL-LEVEL FEATURES
features = (
    df.groupby("mmsi")
    .agg(
        observations=("mmsi", "size"),
        first_seen=("base_date_time", "min"),
        last_seen=("base_date_time", "max"),
        min_sog=("sog", "min"),
        max_sog=("sog", "max"),
        mean_sog=("sog", "mean"),
        mean_cog=("cog", "mean"),
        ais_gap_count=("ais_gap", "sum"),
        max_gap_minutes=(
            "time_diff_seconds",
            lambda x: 0 if x.dropna().empty else x.max() / 60
        ),
        stopped_observations=("stopped", "sum")
    )
    .reset_index()
)
# SAVE
features.to_csv(
    OUTPUT,
    index=False
)
# SUMMARY
print("Vessel feature extraction complete.")
print(f"Vessels: {len(features):,}")
print(f"Output: {OUTPUT}")

print("\nFeatures:")
print(features.head())