from BST import range_query
from AVLTree import AVLTree
from datetime import datetime, timedelta
from Heap import MinHeap
from collections import deque

class PriceTracker:
    """
    A class to track asset prices and maintain 10-day minimum, maximum, and average prices.

    Attributes:
        _price_tree (AVLTree): An AVL tree storing price data with timestamps as keys
            and tuples of (price, ten_day_min, ten_day_max, ten_day_avg) as values.
        _price_min_heap (MinHeap): A min-heap storing (price, time) tuples to track the
            minimum price within a 10-day window.
        _price_max_heap (MinHeap): A min-heap storing (-price, time) tuples to track the
            maximum price within a 10-day window.
        _heap_node_map_min (dict): Maps timestamps to min-heap nodes for efficient deletion.
        _heap_node_map_max (dict): Maps timestamps to max-heap nodes for efficient deletion.
        _price_queue (deque): Stores (time, price) tuples to track prices in the 10-day window.
        _window_sum (float): Sum of prices in the current 10-day window.
        _window_count (int): Number of prices in the current 10-day window.
        _latest_time (datetime or None): The most recent timestamp added.
    """

    def __init__(self):
        """
        Initialises a new PriceTracker instance.
        """
        self._price_tree = AVLTree()
        self._price_min_heap = MinHeap()
        self._price_max_heap = MinHeap()
        self._heap_node_map_min = {}
        self._heap_node_map_max = {}
        self._price_queue = deque()
        self._window_sum = 0.0
        self._window_count = 0
        self._latest_time = None

    def add_price(self, time: datetime, price: float):
        """
        Add a new price and update the 10-day minimum, maximum, and average.

        Args:
            time (datetime): Time of the price.
            price (float): Price of the asset.
        """
        if self._latest_time is None:
            self._latest_time = time

        window_start = time - timedelta(days=10)

        self._price_queue.append((time, price))
        self._window_sum += price
        self._window_count += 1

        while self._price_queue and self._price_queue[0][0] < window_start:
            old_time, old_price = self._price_queue.popleft()
            self._window_sum -= old_price
            self._window_count -= 1


        while self._price_min_heap._size > 0:
            min_price, min_time = self._price_min_heap.root.key
            if min_time < window_start:
                heap_node = self._heap_node_map_min[min_time]
                self._price_min_heap.delete_node(heap_node)
                del self._heap_node_map_min[min_time]
            else:
                break


        while self._price_max_heap._size > 0:
            neg_max_price, max_time = self._price_max_heap.root.key
            if max_time < window_start:
                heap_node = self._heap_node_map_max[max_time]
                self._price_max_heap.delete_node(heap_node)
                del self._heap_node_map_max[max_time]
            else:
                break


        heap_node_min = self._price_min_heap.insert((price, time))
        self._heap_node_map_min[time] = heap_node_min

        heap_node_max = self._price_max_heap.insert((-price, time))
        self._heap_node_map_max[time] = heap_node_max

        # Calculate 10-day stats
        ten_day_min = self._price_min_heap.root.key[0] if self._price_min_heap._size > 0 else price
        ten_day_max = -self._price_max_heap.root.key[0] if self._price_max_heap._size > 0 else price
        ten_day_avg = self._window_sum / self._window_count if self._window_count > 0 else price


        self._price_tree.insert(time, (price, ten_day_min, ten_day_max, ten_day_avg))
        self._latest_time = time

    def get_price_data(self, start: datetime, end: datetime):
        """
        Retrieve price data in the given time range.

        Args:
            start (datetime): Start time (inclusive).
            end (datetime): End time (inclusive).

        Returns:
            list: List of (time, (price, ten_day_min, ten_day_max, ten_day_avg)) tuples, ordered by time.
        """
        return range_query(self._price_tree, start, end)