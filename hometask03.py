def print_table(distances):
    # Верхній рядок таблиці
    print("{:<15} {:<15}".format("Вершина", "Відстань"))
    print("-" * 25)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        
        print("{:<15} {:<15}".format(vertex, distance))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    return distances


#'Київ', 'Варшава', 'Прага', 'Братислава', 'Відень', 
#'Будапешт', 'Рим', 'Париж', 'Берлін', 'Лондон', 'Мадрид'
graph = {
    'Київ': {'Будапешт': 1117, 'Братислава': 1330, 'Прага': 1409, 'Варшава': 794},
    'Варшава': {'Київ': 794, 'Прага': 640, 'Берлін': 574},
    'Прага': {'Варшава': 640, 'Київ': 1409, 'Відень': 340, 'Рим': 1300, 'Париж': 1031, 'Берлін': 351},
    'Братислава': {'Київ': 1330, 'Відень': 78, 'Будапешт': 200},
    'Відень': {'Братислава': 78, 'Прага': 340, 'Рим': 1134, 'Будапешт': 244},
    'Будапешт': {'Київ': 1117, 'Братислава': 200, 'Відень': 244, 'Рим': 1215},
    'Рим': {'Будапешт': 1215, 'Відень': 1134, 'Прага': 1300, 'Париж': 1422, 'Мадрид': 1957},
    'Париж': {'Рим': 1422, 'Мадрид': 1275, 'Лондон': 461, 'Берлін': 1057, 'Прага': 1031},
    'Берлін': {'Варшава': 574, 'Прага': 351, 'Париж': 1057, 'Лондон': 1101},
    'Лондон': {'Берлін': 1101, 'Париж': 461, 'Мадрид': 1721},
    'Мадрид': {'Рим': 1957, 'Париж': 1275, 'Лондон': 1721}
}

for city in graph.keys():
    print()
    print(f'Найкоротший шлях між вершиною {city} та іншими вершинами графу')
    print_table(dijkstra(graph, city))