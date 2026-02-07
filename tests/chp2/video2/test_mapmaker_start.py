from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    """
    Create a point for the city of San Francisco,
    which is located at 37.77 degrees latitude and -122.42 degrees longitude.
    """
    point1 = Point("San Francisco", 37.77, -122.42)
    assert point1.get_lat_log() == (37.77, -122.42)
