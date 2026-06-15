import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo.capitalize())
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Add and remove todos as you complete them.")
st.write("This app is to increase productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter new todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")