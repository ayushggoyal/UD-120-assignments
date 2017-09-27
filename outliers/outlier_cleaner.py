#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    import numpy as np

    ### your code goes here
    """index = []
    for i in range(len(ages)):
    	index.append(i)
    print index[1]
    print len(index)
    #print len(ages)"""
    check =  [abs(p-n) for p, n,  in zip(predictions, net_worths)]
    #index = heapq.nlargest(9, range(len(check)), check.take)
    #print index
    cleaned_data = zip((ages), (net_worths), (check))
    cleaned_data.sort(key = lambda tup: tup[2])
    for i in range(0, int(len(check)*0.1)):
    	cleaned_data.pop()
    return cleaned_data

