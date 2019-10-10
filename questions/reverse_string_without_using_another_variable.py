def reverse_without_variable(string):
    import ipdb
    ipdb.set_trace()
    end = len(string) - 1
    start = 0

    # while (start < end):
    #     if string[start] == '':
    #         continue
    #     start_tmp = bytearray(string[start].encode())
    #     end_tmp = bytearray(string[end].encode())

    #     start_tmp[0] ^= end_tmp[0]
    #     end_tmp[0] ^= start_tmp[0]
    #     start_tmp[0] ^= end_tmp[0]

    #     string[start] = start_tmp.decode()
    #     string[end] = end_tmp.decode()

    #     start = start + 1
    #     end = end - 1

    i = 0

    while (i < end):
        j = i + 1
        while (string[j] != ' ' or j > end):
            start_tmp = bytearray(string[i].encode())
            end_tmp = bytearray(string[j].encode())

            start_tmp[0] ^= end_tmp[0]
            end_tmp[0] ^= start_tmp[0]
            start_tmp[0] ^= end_tmp[0]

            string[i] = start_tmp.decode()
            string[j] = end_tmp.decode()
            j = j+1

        i = i + 1

    return string


i = 0
while (i < end):
    j = i + 1
    while (string[j] != ' '):
        start_tmp = bytearray(string[i].encode())
        end_tmp = bytearray(string[j].encode())

        start_tmp[0] ^= end_tmp[0]
        end_tmp[0] ^= start_tmp[0]
        start_tmp[0] ^= end_tmp[0]

        string[i] = start_tmp.decode()
        string[j] = end_tmp.decode()
        j = j+1

    i = i + 1
