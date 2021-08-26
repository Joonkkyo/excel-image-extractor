import zipfile
import argparse
import shutil
import time
import uuid
import os

parser = argparse.ArgumentParser(description='Extract all images from excel files.')
parser.add_argument('--dir', help='Directory of the files')
args = parser.parse_args()

file_list = os.listdir(args.dir)
excel_list = []

for file_name in file_list:
    ext = os.path.splitext(file_name)[-1]
    if ext in ['.xlsx', '.xlsm', '.xls']:
        excel_list.append(file_dir + '/' + file_name)
print(excel_list)

for excel_file in excel_list:
    print("org_name :", excel_file)
    if not os.path.exists("./xlsx_zip_extract"):
        os.mkdir("./xlsx_zip_extract")
    org_file_name, org_ext = os.path.splitext(excel_file)
    zip_name = org_file_name + '.zip'
    print("zip_name :", zip_name)
    os.rename(excel_file, zip_name)

    try:
        zipfile.ZipFile(zip_name).extractall("./xlsx_zip_extract")
    except:
        os.rename(zip_name, org_file_name + org_ext)
        continue

    if not os.path.exists("./xlsx_zip_extract/xl/media"):
        print("no images")
    else:
        img_files = os.listdir("./xlsx_zip_extract/xl/media")
        for images in img_files:
            file_name, ext = os.path.splitext(images)
            if ext == ".png":
                shutil.move("./xlsx_zip_extract/xl/media/" + images, "./tf_xlsx_img/" + str(uuid.uuid4()) + ".png")
                
    os.rename(zip_name, org_file_name + org_ext)
    shutil.rmtree("./xlsx_zip_extract")

    
