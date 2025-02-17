import statistics

def process_temperatures(temp_list):
    """
    Process the list of temperatures and return min, max, and avg with specific error handling:
    1) If the list is empty -> "Error: No input provided."
    2) If any input is non-numeric -> "Error: No valid input provided."
    3) If any numeric input is out-of-bound -> "Error: Out-of-bound values detected."
    4) Otherwise -> Return min, max, avg.
    """
    # 1) Check if list is empty
    if not temp_list:
        return "Error: No input provided."

    # Flags to track input problems
    invalid_non_numeric_found = False
    out_of_bound_found = False
    valid_temps = []

    # 2) Validate each input
    for item in temp_list:
        # Attempt to parse
        try:
            value = float(item)
            # Check range
            if -50 <= value <= 150:
                valid_temps.append(value)
            else:
                out_of_bound_found = True
        except ValueError:
            # Non-numeric input
            invalid_non_numeric_found = True

    # 3) Decide which error (if any) to return
    if invalid_non_numeric_found:
        return "Error: No valid input provided."
    if out_of_bound_found:
        return "Error: Out-of-bound values detected."
    if not valid_temps:
        return "Error: No valid input provided."  # covers case if everything was invalid or out-of-bound

    # 4) All inputs are valid and within range -> calculate min, max, avg
    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"