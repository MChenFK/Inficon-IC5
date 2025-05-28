def parse_ic5_output(line):
    """
    Parses a line of text from the IC5.
    Example line: "TIME=12:34:56 VALUE=1.23 UNIT=mbar"
    """
    data = {}
    parts = line.split()
    for part in parts:
        if '=' in part:
            key, val = part.split('=', 1)
            data[key] = val
    return data
