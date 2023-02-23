import math

N = int(input())
points = []
for i in range(N):
  points.append(tuple(map(int, input().split())))

area = 0
pivot = points[0]
a = points[1]
for p in points[2:]:
  b = p
  aa = math.sqrt((pivot[0]-a[0])**2 + (pivot[1]-a[1])**2)
  bb = math.sqrt((pivot[0]-b[0])**2 + (pivot[1]-b[1])**2)
  ang_a = math.atan2((pivot[1]-a[1]), (pivot[0]-a[0]))
  ang_b = math.atan2((pivot[1]-b[1]), (pivot[0]-b[0]))
  area += aa * bb * math.sin(ang_a-ang_b) /2
  a = p

print(round(abs(area), 1))