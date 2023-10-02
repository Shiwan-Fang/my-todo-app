import streamlit as st
import functions

# 在终端中streamlit run web.py 运行这个code的方式，而不是直接run
# 刷新网页就可以看到更新的代码，就像写前端一样
# the script is executed from top to bottom with any load of the page
# st.session_state always exist. Add it on the script, and it will show on the webpage

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # session_state type, looks like dictionary
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

#  show the info in todos.txt on the web
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # iterate todos.txt, and add the key of its own
    if checkbox:
        #  if you check/click the checkbox, the "value" in session_state will turn to "true"
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", label_visibility="hidden",  placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
# placeholder as a hint in the input box



