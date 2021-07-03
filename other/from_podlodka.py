def max_salary_sum(costs):
    max_sum = 0
    max_cost = 0
    for cost in costs[::-1]:
        max_cost = max(max_cost, cost)
        max_sum += max_cost
        print(max_sum)
    return max_sum


if __name__ == '__main__':
    costs = [int(value) for value in input().split()]
    print(max_salary_sum(costs))

