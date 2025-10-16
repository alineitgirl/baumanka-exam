def minimum_path_elements(triangle):
    n = len(triangle)
    if n == 0:
        return []
    
    dp = [row[:] for row in triangle]
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
    
    path = []
    i, j = 0, 0
    while i < n:
        path.append(triangle[i][j])  
        if i == n - 1:
            break
        if dp[i + 1][j] < dp[i + 1][j + 1]:
            pass
        else:
            j += 1
        i += 1
    
    return path

if __name__ == "__main__":
    n = int(input("Введите количество строк в треугольнике: "))

    triangle = [
        [int(x) for x in input().split()] for _ in range(n) 
    ]
    elements = minimum_path_elements(triangle)
    path = "->".join([str(i) for i in elements])
    print(f"Минимальный путь: {path}")
    print(f"Результат: {sum(elements)}")