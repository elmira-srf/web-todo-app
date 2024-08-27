FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list
    of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)

if __name__ == "__main__":
    print("Inside the if") #This will not be printed when imported, it will only be printed when run directly.