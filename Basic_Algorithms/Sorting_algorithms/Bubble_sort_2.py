#Sam doesn't always go to sleep in the same hour. 
# Given the following times Sam has gone to sleep, sort the times from latest to earliest.
# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)

bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")