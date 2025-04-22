#Here exceptions related to the Google sheets service are defined

class DataFetchException(Exception):
    """High-level exception to represent fetch failure."""
    pass

class OperationException(Exception):
    """High-level exception to represent operation failure. For example: Failed to append, Failed to delete, Failed to find"""
    pass