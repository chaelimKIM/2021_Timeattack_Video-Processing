def convert_values(result):
    converted_result = []

    for i in result:
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        converted_result.append("%02d:%02d:%02d" % (h, m, s))

    return converted_result
