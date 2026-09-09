import math
import pandas as pd


def haversine_distance_km(lat1, lon1, lat2, lon2):
    """
    Calculate great-circle distance between two
    latitude/longitude coordinates.

    Returns distance in kilometers.
    """

    R = 6371.0  # Earth radius in km

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    dlat = lat2 - lat1
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c


def spatial_score(distance_km, scale_km=10):
    """
    Convert distance from spill origin into a 0-100 score.
    """

    if distance_km is None:
        return 0.0

    score = 100 * math.exp(
        -distance_km / scale_km
    )

    return max(0.0, min(100.0, score))


def temporal_score(
    first_seen,
    last_seen,
    spill_time,
    tolerance_hours=2
):
    """
    Score whether the vessel was observed around
    the estimated spill time.
    """

    first_seen = pd.to_datetime(
        first_seen,
        utc=True
    )

    last_seen = pd.to_datetime(
        last_seen,
        utc=True
    )

    spill_time = pd.to_datetime(
        spill_time,
        utc=True
    )

    if first_seen <= spill_time <= last_seen:
        return 100.0

    if spill_time < first_seen:
        delta_hours = (
            first_seen - spill_time
        ).total_seconds() / 3600

    else:
        delta_hours = (
            spill_time - last_seen
        ).total_seconds() / 3600

    if delta_hours >= tolerance_hours:
        return 0.0

    return 100 * (
        1 - delta_hours / tolerance_hours
    )