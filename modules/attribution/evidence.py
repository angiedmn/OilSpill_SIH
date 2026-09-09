import pandas as pd


def build_vessel_evidence(
    candidate_vessels,
    candidate_tracks,
    vessel_features,
    vessel_gaps
):
    """
    Combine AIS outputs into one evidence record per candidate vessel.
    """

    evidence = []

    for _, vessel in candidate_vessels.iterrows():

        mmsi = vessel["mmsi"]

        # -----------------------------
        # Spatial evidence
        # -----------------------------

        spatial = {
            "min_distance_km": vessel["min_distance_km"],
            "observations": vessel["observations"]
        }

        # -----------------------------
        # Temporal evidence
        # -----------------------------

        temporal = {
            "first_seen": vessel["first_seen"],
            "last_seen": vessel["last_seen"]
        }

        # -----------------------------
        # Trajectory evidence
        # -----------------------------

        vessel_track = candidate_tracks[
            candidate_tracks["mmsi"] == mmsi
        ]

        trajectory = {
            "observations": len(vessel_track)
        }

        # -----------------------------
        # Vessel behavior evidence
        # -----------------------------

        feature_rows = vessel_features[
            vessel_features["mmsi"] == mmsi
        ]

        if len(feature_rows) > 0:
            feature = feature_rows.iloc[0]

            behavior = {
                "ais_gap_count": feature["ais_gap_count"],
                "max_gap_minutes": feature["max_gap_minutes"],
                "stopped_observations": feature["stopped_observations"],
                "mean_sog": feature["mean_sog"],
                "min_sog": feature["min_sog"],
                "max_sog": feature["max_sog"]
            }

        else:
            behavior = {
                "ais_gap_count": 0,
                "max_gap_minutes": 0,
                "stopped_observations": 0,
                "mean_sog": None,
                "min_sog": None,
                "max_sog": None
            }

        # -----------------------------
        # AIS gap records
        # -----------------------------

        vessel_gaps_for_mmsi = vessel_gaps[
            vessel_gaps["mmsi"] == mmsi
        ]

        gaps = vessel_gaps_for_mmsi[
            [
                "gap_start_time",
                "gap_end_time",
                "gap_minutes"
            ]
        ].to_dict(orient="records")

        evidence.append({
            "mmsi": mmsi,
            "spatial": spatial,
            "temporal": temporal,
            "trajectory": trajectory,
            "behavior": behavior,
            "gaps": gaps
        })

    return evidence