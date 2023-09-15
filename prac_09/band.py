class Band:
    """Band class for storing details of a band and its musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_info = ", ".join([str(musician) for musician in self.musicians])
        return f"{self.name} ({musician_info})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument (if available)."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
