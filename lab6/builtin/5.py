def all_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(all_true(tuple1))  # true
print(all_true(tuple2))  # false