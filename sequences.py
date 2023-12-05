def remove_duplicates(sequence):
    seen = set()
    new_sequence = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            new_sequence.append(item)

    return new_sequence