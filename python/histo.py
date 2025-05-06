
def main():
    #nums = [5, 3, 1, 5, 0, 2,]
    #nums = [3, 2, 1]
    nums = [1]
    n = len(nums)
    mn = max(nums)
    mc = mn
    for _ in range(mn):
        out = []
        for col in range(n):
            if nums[col] == mc:
                out.append("X")
                nums[col] -= 1
            else:
                out.append(" ")
        mc -= 1
        print(f"{''.join(out)}")


if __name__ == "__main__":
    main()
