def get_line(x0, y0, x1, y1):
    points = [(x0, y0)]
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    xk = x0
    yk = y0

    directionX = 1 if x1 > x0 else -1
    directionY = 1 if y1 > y0 else -1

    if dx > dy:
        Pk = 2 * dy - dx
        while xk != x1:
            xk += directionX
            if Pk < 0:
                Pk += 2 * dy
            else:
                yk +=   directionY
                Pk += 2 * dy - 2 * dx
            points.append((xk, yk))
    else:
        Pk = 2 * dx - dy
        while yk != y1:
            yk +=   directionY
            if Pk < 0:
                Pk += 2 * dx
            else:
                xk += directionX
                Pk += 2 * dx - 2 * dy
            points.append((xk, yk))

    return points


if __name__ == "__main__":
    x0 = 3
    y0 = 2
    x1 = 15
    y1 = 11
    points = get_line(x0, y0, x1, y1)
    print(points)
