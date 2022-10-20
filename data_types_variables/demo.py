import time

counter = 0
tic = time.perf_counter()


while True:
    toc = time.perf_counter()
    if toc - tic > 1:
        counter += 1
        print(counter)
        tic = toc