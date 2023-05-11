datas = ["a", "b", "c"]

some_text = "hello world"

with open('sample.txt', 'w') as file:
    for data in datas:
        file.write(data)

    file.write('\n')
