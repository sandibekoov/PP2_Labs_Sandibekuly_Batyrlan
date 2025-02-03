def spy_game():
    nums = list(map(int, input().split()))
    pattern = [0, 0, 7]
    index = 0

    for num in nums:
        if num == pattern[index]:
            index += 1
            if index == len(pattern):
                print(True)
                return
    print(False)

spy_game()
