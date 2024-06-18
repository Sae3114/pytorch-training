from pathlib import Path

if __name__=="__main__":
    data_directory = "./data"
    data_directory_path = Path(data_directory).resolve()
    print("===== problem1 =====")
    print(data_directory_path) 

    directory_list = list(data_directory_path.glob("*"))
    print("===== problem2 =====")
    for directory in directory_list:
        print(directory)

    n = 0
    for directory in directory_list:
        image_list = list(directory.glob("*"))
        for image in image_list:
            if image.exists():
                n += 1
    print("===== problem3 =====")
    print(n)