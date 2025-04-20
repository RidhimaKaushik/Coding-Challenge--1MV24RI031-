def star_triangle(n):
    for i in range(n+1):
        stars = i * 2 -1
        whitespace = n - i
        print(" "*whitespace + "*"*stars)

print(star_triangle(4))