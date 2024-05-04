import csv

def add_todo(file_name):
    todo_name = input("Enter a todo item: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo():
    print("Remove todo")

def mark_todo():
    print("View todo")

def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is completed.")
                else:
                    print(f"{row[0]} is not complete.")
    except FileNotFoundError:
        print("The todo file does not exist")