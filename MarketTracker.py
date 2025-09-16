from datetime import datetime
from PriceTracker import PriceTracker

class MarketTracker:
    """
    A class to track prices for multiple assets.

    Attributes:
        _trackers (dict): A dictionary mapping asset names to PriceTracker instances.
    """

    def __init__(self):
        """
        Initialises a new MarketTracker instance.
        """
        self._trackers = {}

    def add_price(self, name: str, time: datetime, price: float):
        """
        Add a new price for the specified asset.

        Args:
            name (str): Name of the asset.
            time (datetime): Time of the price.
            price (float): Price of the asset.
        """
        if name not in self._trackers:
            self._trackers[name] = PriceTracker()
        self._trackers[name].add_price(time, price)

    def get_price_data(self, name: str, start: datetime, end: datetime):
        """
        Retrieve price data for the specified asset in the given time range.

        Args:
            name (str): Name of the asset.
            start (datetime): Start time (inclusive).
            end (datetime): End time (inclusive).

        Returns:
            list: List of (time, (price, ten_day_min, ten_day_max, ten_day_avg)) tuples, ordered by time.

        Raises:
            KeyError: If the asset name is not found.
        """
        if name not in self._trackers:
            raise KeyError(f"Asset {name} not found")
        return self._trackers[name].get_price_data(start, end)

