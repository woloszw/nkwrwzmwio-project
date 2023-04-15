map = [[8, 5, 7, 3, 1],
[5, 5, 6, 7, 3],
[1, 4, 2, 4, 4],
[2, 3, 5, 5, 6],
[2, 3, 2, 4, 4]]


def check_sea_level(map):
    n = len(map)
    min_height = min(map[0][0], map[0][n-1], map[n-1][0], map[n-1][n-1])
    max_height = max([max(row) for row in map])
    
    left = min_height
    right = max_height
    result = None
    
    while left <= right:
        mid = (left + right) // 2
        
        flooded = set()
        for i in range(n):
            for j in range(n):
                if map[i][j] <= mid:
                    flooded.add((i, j))
        
        for i in range(n):
            flooded.add((0, i))
            flooded.add((i, 0))
            flooded.add((n-1, i))
            flooded.add((i, n-1))
        be=0
        while True:
            be = be +1
            new_flooded = set()
            for i, j in flooded:
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and map[ni][nj] > mid:
                        new_flooded.add((ni, nj))
            if not new_flooded:
                break
           
            flooded |= new_flooded
            if be>50:
                break
        
        components = []
        visited = set()
        for i in range(n):
            for j in range(n):
                if map[i][j] > mid and (i, j) not in visited:
                    component = set()
                    stack = [(i, j)]
                    while stack:
                        ni, nj = stack.pop()
                        if (ni, nj) not in component:
                            component.add((ni, nj))
                            visited.add((ni, nj))
                            for di, dj  in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                                        
                                            ti, tj = ni + di, nj + dj
                                            if 0 <= ti < n and 0 <= tj < n and map[ti][tj] > mid and (ti, tj) not in visited:
                                                stack.append((ti, tj))
                    components.append(component)
    
        if len(components) >= 2:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    if result is not None:
        return result
    else:
        return "Wyspa nie zostanie podzielona."                           
 
if __name__ == '__main__':
    result = check_sea_level(map)
    print(result)