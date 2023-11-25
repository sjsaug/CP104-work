def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    fh.seek(0)
    i = 0
    while i < n:
        fh.readline()
        i += 1
    line = fh.readline()
    if line != "":
        result = line.strip().split(",")
    return result

def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    fh.seek(0)
    line = fh.readline()
    while line != "":
        record = line.strip().split(",")
        if record[0] == id_number:
            result = record
            break
        line = fh.readline()
    return result

def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    fh.seek(0)
    num = 0
    for line in fh:
        num = max(num, int(line.strip()))
    fh.write(str(num) + "\n")
    return num

def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0
    fh.seek(0)
    for line in fh:
        if int(line.strip()) == value:
            count += 1
    return count

def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    fh.seek(0)
    word = ""
    for line in fh:
        for w in line.strip().split():
            if len(w) >= len(word):
                word = w
    return word

def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    fh_1.seek(0)
    for i in range(n):
        line = fh_1.readline()
        if line != "":
            fh_2.write(line)
        else:
            break
    return