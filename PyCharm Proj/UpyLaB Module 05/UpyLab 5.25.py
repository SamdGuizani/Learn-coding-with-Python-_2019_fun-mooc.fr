def trace(M):
    trace = 0
    if M == []:
        trace = trace
    else:
        for i in range(len(M)):
            trace += M[i][i]
    return trace


# Code principal
print(trace([]))
print(trace([[1, 2, 3, 4] for i in range(4)]))
