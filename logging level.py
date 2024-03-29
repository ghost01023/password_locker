from sys import argv
import os, shutil

source = "C:\\Users\\Rosja Dostoyevsjky\\Downloads\\IDM\newp\\Negisaray_2022-09_compressed\\Negisaray 2022-09 compressed"
dest = "C:\\Users\\Rosja Dostoyevsjky\\Downloads\\IDM\\newp"

for root, folders, files in os.walk(source):
    print(files)
    print(root)
    print("hello")
    # for folder in folders:
    #     print(folder)
    for file in files:
        print(f"{file} is present in {folders}")
        # print(f"Moving {file} to Destination...")
        shutil.move(file, dest)
    print("File Moved.")

# print("Job Finished.")