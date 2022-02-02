import os
import time
import shutil

def main():
    deleted_folder_count = 0
    deleted_file_count = 0
    path = input("enter path name for files to be removed: ")
    days = 30
    sec = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if(sec >= get_file_folder(root_folder)):
                remove_folder(root_folder)
                deleted_folder_count +=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if(sec >= get_file_folder(folder_path)):
                        remove_folder(root_folder)
                        deleted_folder_count +=1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if(sec >= get_file_folder(file_path)):
                        remove_file(file_path)
                        deleted_file_count +=1
        else:
            if sec >= get_file_folder(path):
                remove_file(path)
                deleted_file_count+=1
    else:
        print(f"{path} is defined")
        deleted_file_count+=1
    print(f"Total Folders Deleted: "+{deleted_folder_count})
    print(f"Total Files Deleted: "+{deleted_file_count})
    
def remove_folder(path):
    if not os.remove(path):
        print(f"{path} is removed succesfully")
    else:
        print("Unable to delete"+path)
        
def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed succesfully")
    else:
        print("Unable to delete"+path)

def get_file_folder(path):
    ctime = os.stat(path).st_ctime
    return ctime


if __name__=="__name___":
    main()