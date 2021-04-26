# 已知杯子容量X, Y
# 目前杯子还能装x, y
def successors(x, y, X, Y):
    return {
        (x, 0): '倒空y',
        (0, y): '倒空x',
        (x, Y): '装满y',
        (X, y): '装满x',
        (0, x + y) if x + y <= Y else (x + y - Y, Y): 'x=>y',
        (x + y, 0) if x + y <= X else (X, x + y - x): 'y=>x',
    }


# print(successors(30,20,90,40))

def search_solution(capacity1, capacity2, goal, start=(0, 0)):
    if goal in start: return [start]
    explored = set()
    paths = [[('init', start)]]
    while paths:
        path = paths.pop(0)
        (x, y) = path[-1][-1]

        for state, action in successors(x, y, capacity1, capacity2).items():
            if state in explored: continue
            new_path = path + [(action, state)]
            if goal in state:
                return new_path
            else:
                paths.append(new_path)
        explored.add((x, y))
    return []


if __name__ == '__main__':
    solution = search_solution(9, 4, 7)
    # print(solution)
    # print(list(enumerate(solution)))
    for i, s in enumerate(solution):

        print('step:{} {}'.format(i, s))
