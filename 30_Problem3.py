# for i in range(2, 21):
#     with open(f"Table/Multiplication_Tables_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}\n")
#             if j!=10:
#                 f.write('\n')
#     #break



# with open("Sample.txt") as f:
#     content = f.read()

# content = content.replace("donkey" and "Donkey", "######")

# with open("Sample.txt", "w") as f:
#     f.write(content)

# with open("log.txt", "r") as f:
#     content = f.read()

# if "python" in content.lower():
#     print("Yes python is present")
# else:
#     print("No python is not present")

content = True
i = 1

with open('log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line no. {i}")
            #print(i)
        i+=1

