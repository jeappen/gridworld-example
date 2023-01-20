def Grid(object):
    map = None
    def __init__(self, m, n):
        """Create the map"""
        self._build_map(m,n)

    def _build_map(self, m, n):
        """Make a grid being the map of the world"""
        pass

    def reset(self):
        """Move robot to starting"""
        pass

    def step(self, action):
        """Depending on action in 0-3, move up, down, left, or right"""
        pass
