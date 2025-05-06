def main():
    n, k, x,y = 5, 2, 0, 0
    b = [['0' for _ in range(n)] for _ in range(n)]
    dx = (2, 1, -1, -2, -2, -1, 1, 2)
    dy = (1, 2, 2, 1, -1, -2, -2, -1)

    def bt(d, xx, yy):
        if 0<= xx <n and 0<= yy < n:
            if d == 0:
                b[xx][yy] = "X"
                return
            for dxx, dyy in zip(dx, dy):
                bt(d-1, xx+dxx, yy+dyy)

    bt(k,x,y)
    for row in range(len(b)):
        print(f"{''.join(b[row])}")


if __name__ == "__main__":
    main()
