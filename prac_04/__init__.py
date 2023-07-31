def parse_query_string(query_string):
    query_params = query_string.strip('?').split('&')
    result = []

    for param in query_params:
        name_value = param.split('=')
        name = name_value[0]
        value = name_value[1]

        if value.isnumeric():
            value = int(value)

        result.append((name, value))

    return result


# Test the function with the provided example:
query_string = "?name=Bob&age=99&day=Wed"
result = parse_query_string(query_string)
print(result)
