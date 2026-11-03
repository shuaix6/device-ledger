with open("mode_test.txt", "w", encoding="utf-8") as fout:
    fout.write("第一行\n")

with open("mode_test.txt", "w", encoding="utf-8") as fout:
    fout.write("第二行\n")

with open("mode_test.txt", "a", encoding="utf-8") as fout:
    fout.write("第三行\n")

with open("mode_test.txt", "w", encoding="utf-8") as fout:
    pass