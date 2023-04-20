def class_to_json(obj):
    """Return a dictionary description of a simple object for JSON serialization."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("object has no attribute '__dict__'")

    data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, tuple)):
            data[key] = [class_to_json(item) if hasattr(item, '__dict__') else item for item in value]
        elif isinstance(value, dict):
            data[key] = {k: class_to_json(v) if hasattr(v, '__dict__') else v for k, v in value.items()}
        elif isinstance(value, (str, int, bool)):
            data[key] = value
        else:
            data[key] = class_to_json(value) if hasattr(value, '__dict__') else None

    return data

