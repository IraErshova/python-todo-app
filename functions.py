def get_todos(filepath="todos.txt"):
    """ Get all todos from the file """
    with open(filepath, "r") as file_local:
        return file_local.readlines()


def write_todos(new_todos, filepath="todos.txt"):
    """ Write todos to the file """
    with open(filepath, "w") as file_local:
        file_local.writelines(new_todos)


# we see this output only if we run functions.py directly
if __name__ == "__main__":
    print("Hello World")
    print(get_todos())
