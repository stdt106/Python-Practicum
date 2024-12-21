def merge(sequence_1, sequence_2):
    queue_1 = list(sequence_1)
    queue_2 = list(sequence_2)
    sequence = []
    while queue_1 and queue_2:
        if queue_1[0] > queue_2[0]:
            sequence.append(queue_2.pop(0))
        else:
            sequence.append(queue_1.pop(0))
    sequence.extend(queue_1)
    sequence.extend(queue_2)
    return tuple(sequence)