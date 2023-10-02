FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        # file = open('todos.txt', 'r')
        # get the item from the user, rather than create an empty list防止txt中原来内容被下面的w覆盖，因此先
        # todos = file.readlines()
        # 此时游标cursor到文件的最末端
        # return a list of lines, if we use read() ,return the content
        # file.close()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    write the to-do items in the text file.
    """
    # different from get_todos() function, write_todos() don't have a return, more like a procedure
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # new todos overwrite the old one
        # file.close()
