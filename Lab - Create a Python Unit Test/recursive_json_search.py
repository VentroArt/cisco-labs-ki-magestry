def json_search(key, input_object):
    """
    Search a key from JSON object, return nothing if key is not found.
    
    key : "keyword" to be searched, case-sensitive
    input_object : JSON object to be parsed
    Returns a list of key:value pairs where the key matches.
    """
    ret_val = []

    def inner_function(key, input_object):
        if isinstance(input_object, dict):
            # Iterate dictionary
            for k, v in input_object.items():
                if k == key:
                    # If key matches, append to the result
                    ret_val.append({k: v})
                # If value is another dictionary, recurse
                if isinstance(v, dict):
                    inner_function(key, v)
                # If value is a list, iterate through the list
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str, int)):  # Check if item is complex
                            inner_function(key, item)
        elif isinstance(input_object, list):
            # Handle case where input_object itself is a list
            for item in input_object:
                if not isinstance(item, (str, int)):
                    inner_function(key, item)

    inner_function(key, input_object)
    return ret_val
