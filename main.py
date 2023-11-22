import os

file_path = 'D:\\example_for_recursion'


def rec_folder(path, level=1):
    print(f"Level = {level}, Content: {os.listdir(path)}")
    print()

    for i in os.listdir(path):
        rec_path = f'{path}\\{i}'
        if os.path.isdir(rec_path):
            print('Move to ', rec_path)
            rec_folder(rec_path, level + 1)
            print('Back to', path)


rec_folder(file_path)
