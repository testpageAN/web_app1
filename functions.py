FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    """

    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """

    :param todos_arg:
    :param filepath:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print("hello from functions")