#Here exceptions related to the Google sheets service are defined

class DataFetchException(Exception):
    """High-level exception to representfetch failure."""
    pass