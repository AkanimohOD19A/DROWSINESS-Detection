import os
import shutil


def main():
    folders = ["./awake", "./drowsy"]
    if not os.path.exists("./images"):
        os.makedirs("./images")
        trg_folder = "./images"
        for src_folder in folders:
            file_names = os.listdir(src_folder)
            for file_name in file_names:
                shutil.copy(os.path.join(src_folder, file_name), trg_folder)
    # elif os.path.exists("./images"):
    #     ## code to update

if __name__ == '__main__':
    main()
