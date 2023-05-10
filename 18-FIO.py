datas = ["a", "b", "c"]

some_text = "hello world"

with open("sample.txt", "a") as file:
    for data in datas:
        file.writelines(data)

