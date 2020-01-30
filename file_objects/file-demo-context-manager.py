with open('test.txt', 'r') as f:
    # print(f.name, f.mode)

    # READ ALL CONTENT AT ONCE
    # f_contents = f.read()
    # print (f_contents, end='')

    # READ LINES INSTEAD - (Somehow efficient for big files)
    # f_lines = f.readlines()
    # print(f_lines, end='')

    # READ ONLY THE FIRST LINE
    # f_line = f.readline()
    # print(f_line, end='')

    # LOOP THROUGH EACH LINE
    # for line in f:  # Iterating thru these lines one by one - Efficient
    #     print(line, end='')

    # READ FILES IN CHUNKS - (Most Efficient)
    # first_hundred_chars = f.read(100)  # 100 is the number of chars to read
    # print(first_hundred_chars, end='')

    # next_hundred_chars = f.read(100)  # 100 is the number of chars to read
    # print(next_hundred_chars, end='')

    # MORE EFFICIENT CHUNKS - READ SLOWLY UNTIL NOTHING IN FILE
    size_to_read = 100
    f_contents = f.read(size_to_read)

    # print(f.tell())  # Tells the position where the cursor is at the time in the file
    # print(f.seek(0)) # Reads well, pushes the cursor back to position 0 on next read()

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)
