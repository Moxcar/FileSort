import glob
import os
import shutil

src_folder = input("Insert a folder path to sort files: ")
files_extension = ["txt", "pdf", "docx", "xlsx", "pptx", "exe", "doc", "mp4", "png", "jpg", "xls"]

files_moved = 0
for extension in files_extension:
    print("Extension: " + extension)
    files = glob.glob(src_folder + "\*." + extension)
    for file in files:
        file_name = os.path.basename(file)
        dst_folder = src_folder + "\\" + extension
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)
        shutil.move(file, dst_folder + "\\" + file_name)
        print(file + " moved to " + dst_folder + "\\" + file_name)
        files_moved += 1
print(files_moved)