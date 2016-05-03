b = [123,'afdsa',1.2]
c = [[1,2,3],[4,5,6],[7,8,9]]
print(c)
c1 = [row[2] for row in c]
print(c1)
c1 = [row[2] for row in c if row[2] % 2 == 0]
print(c1)
c1 = [c[i][i] for i in [0,1,2]]
print(c1)
c1 = (sum(row) for row in c)
print(next(c1))
print(next(c1))
print(next(c1))
print(list(map(sum, c)))
print({sum(row) for row in c})
print({i: sum(c[i]) for i in range(3)})
