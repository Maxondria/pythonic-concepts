import itertools

# Count
# - Begins from 0 if no args are passed, counts infinitely
counter = itertools.count()

next_value = next(counter)
# print(next_value)

data = [100, 200, 300, 400, 500]

daily_data = zip(itertools.count(start=1, step=4), data)

# for pair in daily_data:
    #print(pair)  # (0, 100), (5, 200), (9, 300)

# More on: https://www.youtube.com/watch?v=Qu3dThVy6KQ
