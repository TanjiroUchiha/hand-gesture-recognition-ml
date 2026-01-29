import os
ans="y"
while ans== "y":
    gesture_name = input("Enter gesture name to delete: ")
    file_path = f"data/{gesture_name}.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted gesture file: {file_path}")
    else:
        print("File not found.")
    ans=input("more? y/n")
    ans=ans.lower()
