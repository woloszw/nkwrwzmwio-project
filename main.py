import copy
def check_sea_level(map_):
    islands=0   #ilosc wysp

#utwórz kopie mapy
    map=copy.deepcopy(map_)

    for water_level in range (50):

# zwróć zalane obszary
        flooded = get_flooded(map, water_level)

    #DO ZROBIENIA - liczenie wysp
        islands=count_islands(flooded);
    # jesli się pojawiły wyspy to kończ
        if(islands>1):
            break
    printmaps(map, flooded)
    print("sea level: ",water_level,"\tislands: ",islands)
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

if __name__ == '__main__':

    print("map 1")
    map =  [[8, 5, 7, 3, 1],
            [5, 5, 6, 7, 3],
            [1, 4, 2, 4, 4],
            [2, 3, 5, 5, 6],
            [2, 3, 2, 4, 4]]
    check_sea_level(map)

    print("map 2")
    map = [[7, 2, 3],
           [5, 1, 5],
           [3, 2, 8]]
    check_sea_level(map)

    print("map 3")
    map =  [[8, 5, 7, 3],
            [5, 5, 6, 7],
            [1, 4, 2, 4],
            [2, 3, 5, 5],
            [2, 3, 2, 4]]
    check_sea_level(map)
