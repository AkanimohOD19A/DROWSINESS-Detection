import os

## Function to rename
def main():
    folders = ["awake", "drowsy"]
    for folder in folders:
        for count, filename in enumerate(os.listdir(folder)):
            dst = f"{str(folder)}_{str(count)}.jpg"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"

            os.rename(src, dst)

if __name__ == '__main__':
    main()