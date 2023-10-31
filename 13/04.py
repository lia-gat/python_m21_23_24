num = int(input('Enter number: '))
points = []

for _ in range(num):
    x, y = input("Enter coordinates: ").split()
    points.append((int(x), int(y)))

result = []

while len(points) > 0:
    same_route = []
    a = points[0][0] // 10 * 10
    b = points[0][1] // 10 * 10
  
    for i in range(len(points)):
        x = points[i][0] // 10 * 10
        y = points[i][1] // 10 * 10
        if x == a and y == b:
            same_route.append(points[i])
  
    result.append(same_route)
  
    filtered_points = []
    for p in points:
        if p not in same_route:
            filtered_points.append(p)
    points = filtered_points

quant = []
for r in result:
    quant.append(len(r))
qmax = max(quant)
print(qmax)
