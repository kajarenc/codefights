def climbingStaircase(n, k):
    result = []

    def discover_unique_ways(n, k, current_way):
        if n == 0:
            result.append(current_way)
        else:
            for i in range(1, k+1):
                if i <= n:
                    discover_unique_ways(n-i, k, current_way + [i])
    discover_unique_ways(n, k, [])
    return result


print(climbingStaircase(4, 2))
