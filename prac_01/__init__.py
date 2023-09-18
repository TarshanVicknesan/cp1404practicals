# def main():
#     for i in range(5):
#         print(do_thing(i))
#
#
# def do_thing(i):
#     return '**' * i
#
#
# main()


text = "O when THE Saints"
parts = text.lower().split()
for i, part in enumerate(sorted(parts)):
    print(part, i)