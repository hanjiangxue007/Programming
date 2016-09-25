

# ref    : https://stackoverflow.com/questions/10973766/understanding-the-map-function


# map creates a new list by applying a function to every element of the source:

xs = [1, 2, 3]

# all of those are equivalent — the output is [2, 4, 6]

# 1. map
ys = map(lambda x: x * 2, xs)

# 2. list comprehension
ys = [x * 2 for x in xs]

# 3. explicit loop
ys = []
for x in xs:
    ys.append(x * 2)

# n-ary map is equivalent to zipping input iterables together and then
# applying the transformation function on every element of that
# intermediate zipped list. It's not a Cartesian product:

xs = [1, 2, 3]
ys = [2, 4, 6]

def f(x, y):
    return (x * 2, y // 2)  # // is floor division 9//2 is 4  and 9.0//2.0 is 4.0, -11//3 is -4, -11.0//3=-4.0

# output: [(2, 1), (4, 2), (6, 3)]

# 1. map
zs = map(f, xs, ys)

# 2. list comp
zs = [f(x, y) for x, y in zip(xs, ys)]

# 3. explicit loop
zs = []
for x, y in zip(xs, ys):
    zs.append(f(x, y))

# I've used zip here, but map behaviour actually differs slightly when
# iterables aren't the same size — as noted in its documentation,
# it extends iterables to contain None.




