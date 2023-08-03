import os

pythonfile_path = os.getcwd()
excel_folder = os.path.join(pythonfile_path, 'excel_file')

file_list = os.listdir(excel_folder)

for f in file_list:
    print(f)


# print(os.listdir(excel_folder))