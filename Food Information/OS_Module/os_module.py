import os
# if (not os.path.exists('data')):
#     os.mkdir('data')

# for i in range(100):
    # os.mkdir(f"data/days{i+1}")
    # os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")

folders = os.listdir("data")

# print(folders)
# for folder in folders:
#     print(os.listdir(f"data/{folder}"))

# for deleting .....
for i in range(100):
    os.removedirs(f"data/Tutorial {i+1}")
