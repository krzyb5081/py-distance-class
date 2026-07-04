from typing import Any


class Distance:
    def __init__(self, km: int | float):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other: Any):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int | float):
            return Distance(self.km + other)
        else:
            return None

    def __iadd__(self, other: Any):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int | float):
            self.km += other
        return self

    def __mul__(self, other: Any):
        if isinstance(other, int | float):
            return Distance(self.km * other)
        else:
            return None

    def __truediv__(self, other: Any):
        if isinstance(other, int | float):
            return Distance(round(self.km / other, 2))
        else:
            return None

    def __lt__(self, other: Any):
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int | float):
            return self.km < other
        return None

    def __le__(self, other: Any):
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int | float):
            return self.km <= other
        return None

    def __gt__(self, other: Any):
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int | float):
            return self.km > other
        return None

    def __ge__(self, other: Any):
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int | float):
            return self.km >= other
        return None

    def __eq__(self, other: Any):
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int | float):
            return self.km == other
        return None
