import unittest

cache = {}
num_cache_hits = 0

def num_ways(n, step_sizes):
    global cache
    global num_cache_hits
    key = (n, str(step_sizes))
    if key in cache:
        num_cache_hits += 1
        # print(num_cache_hits)
        return cache[key]

    ways = 0

    if n < 0:
        cache[key] = 0
        return cache[key]

    # Recursion
    for step_size in step_sizes:
        if n == step_size:
            ways += 1
        else:
            ways += num_ways(n-step_size, step_sizes)

    cache[key] = ways
    return cache[key]
    



class TestNumWays(unittest.TestCase):
    
    def test_num_ways(self):
        n = 0
        step_sizes = {1, 2}
        ways = num_ways(n, step_sizes)
        self.assertEqual(ways, 0)

        n = 1
        step_sizes = {1, 2}
        ways = num_ways(n, step_sizes)
        self.assertEqual(ways, 1)

        n = 2
        step_sizes = {1, 2}
        ways = num_ways(n, step_sizes)
        self.assertEqual(ways, 2)

        n = 3
        step_sizes = {1, 2}
        ways = num_ways(n, step_sizes)
        self.assertEqual(ways, 3)

        n = 4
        step_sizes = {1, 2}
        ways = num_ways(n, step_sizes)
        self.assertEqual(ways, 5)

        n = 100
        step_sizes = {1, 2}
        ways = num_ways(n, step_sizes)
        self.assertEqual(ways, 573147844013817084101)


def main():
    unittest.main()

if __name__ == '__main__':
    main()