import copy
def check_sea_level(map_):
    islands=0   #ilosc wysp

#utwórz kopie mapy
    map=copy.deepcopy(map_)

    for water_level in range (50):

# zwróć zalane obszary
        flooded = get_flooded(map, water_level)

# sprawdź czy jest więcej niż 1 wyspa
        if(is_map_divided(flooded)):
            break

    printmaps(map, flooded)
    print("sea level: ",water_level,"\n")
    print()
    return water_level

def printmap(map):
    for row in map:
        for element in row:
            print(element, end=" ")
        print("")
    print()

def printmaps(map1,map2):
    for i in range (len(map1)):
        print(map1[i],map2[i])


def count_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] >0 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count

def get_flooded(map_, mid):
    map = copy.deepcopy(map_)
    n=len(map)
    m=len(map[0])

# pusta lista punktów odwiedzonych i zalanych
    flooded = []
    visited = []

# przechodzenie po krawędziach
# krawędź lewa
    for i in range(n):
        j = 0
        if map[i][j] <= mid:
            if (i, j) not in visited:
                flooded.append((i, j))

# krawędź górna
    for j in range(m):
        i = 0
        if map[i][j] <= mid:
            if (i, j) not in visited:
                flooded.append((i, j))

# krawędź prawa
    for i in range(n):
        j = m - 1
        if map[i][j] <= mid:
            if (i, j) not in visited:
                flooded.append((i, j))

# krawędź dolna
    for j in range(m):
        i = n - 1
        if map[i][j] <= mid:
            if (i, j) not in visited:
                flooded.append((i, j))

# przechodzenie po wszystkich sąsiadach zalanych punktów
    while (len(flooded)>0):
        index = flooded.pop(0)
        i,j=index
        map[i][j] = 0
        visited.append(index)
#        print("zalano ", index)

# nie sprawdzaj w górę na górze
        if (index[0] > 0):
            i = index[0] - 1;
            j = index[1];
            if (map[i][j] <= mid):
                if (i,j) not in visited:
                    flooded.append((i, j))
                    #print("zalany powyżej\n")

# nie sprawdzaj w prawo po prawej
        if (index[1] > 0):
            i = index[0]
            j = index[1] - 1;
            if (map[i][j] <= mid):
                if (i,j) not in visited:
                    flooded.append((i, j))
                    #print("zalany po prawej\n")

# nie sprawdzaj w dół na dole
        if (index[0] < n - 1):
            i = index[0] + 1;
            j = index[1];
            if (map[i][j] <= mid):
                if (i,j) not in visited:
                    flooded.append((i, j))
                    #print("zalany poniżej\n")

# nie sprawdzaj w lewo po lewej
        if (index[1] < m - 1):
            i = index[0]
            j = index[1] + 1
            if (map[i][j] <= mid):
                if (i,j) not in visited:
                    flooded.append((i, j))
                    #print("zalany po lewej\n")
# zwróć zalaną mapę
    return map
def is_map_divided(map_):
    map = copy.deepcopy(map_)
    n = len(map)
    m = len(map[0])

    # pusta lista punktów odwiedzonych i zalanych

    flooded = []
    flooded_temp = []
    visited = []
    to_visit = []

    for i in range(n):
        # iterate over the columns of the matrix
        for j in range(m):
            # check if the element is non-zero
            if map[i][j] != 0:
                # if so, add the indices to the list
                flooded.append((i, j))
                flooded_temp.append((i, j))

    if(len(flooded_temp)==0):
        print("wyspa sie nie podzieli\n")
        return True
    index = flooded_temp.pop(0)
    to_visit.append(index)

    while (len(to_visit) > 0):
        index = to_visit.pop(0)
        i,j = index
        visited.append(index)

        a = i
        b = j + 1
        if(a, b) in flooded:
            if(a, b) not in visited:
                to_visit.append((a, b))
        a = i
        b = j - 1
        if(a, b) in flooded:
            if(a, b) not in visited:
                to_visit.append((a, b))
        a = i + 1
        b = j
        if(a, b) in flooded:
            if(a, b) not in visited:
                to_visit.append((a, b))
        a = i - 1
        b = j
        if(a, b) in flooded:
            if(a, b) not in visited:
                to_visit.append((a, b))

    print()
    if set(flooded) == set(visited):
        return False
    else:
        return True


if __name__ == '__main__':
    with open('island.txt', 'r') as f:
        lines = f.readlines()
        map = [list(map(int, line.strip().split())) for line in lines]

    check_sea_level(map)
    input("Press any key")
