import streamlit as st

def read_todos():
    try:
        with open("todos.txt", 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_todos(todos):
    with open("todos.txt", 'w') as file:
        file.writelines(todos)

todos = read_todos()

st.title("TODOs App")


user_input = st.selectbox("Choose an action", ["add", "show", "edit", "completed","exit"])


if user_input == 'add':
    todo = st.text_input("Enter a todo:")
    if st.button("Add Todo"):
        if todo:
            todos.append(todo + "\n")
            write_todos(todos)
            st.success("Todo added!")
            st.experimental_rerun()

elif user_input == 'show':
    if st.button("Show Todos"):
        todos = read_todos()
        st.write("Your Todos:")
        for index, item in enumerate(todos):
            row = f"{index + 1} - {item.strip()}"
            st.write(row)

elif user_input == 'completed':
    if todos:
        number = st.number_input("Number of the todo to complete:", min_value=1, max_value=len(todos), step=1)
        if st.button("Completed Todo"):
            index = number - 1
            todos.pop(index)
            write_todos(todos)
            st.success("Todo completed and removed!")
            st.experimental_rerun()
    else:
        st.warning("No todos to complete.")           

elif user_input == 'edit':
    if todos:
        number = st.number_input("Number of the todo to edit:", min_value=1, max_value=len(todos), step=1)
        new_todo = st.text_input("Enter the new todo:")
        if st.button("Edit Todo"):
            todos[number - 1] = new_todo + "\n"
            write_todos(todos)
            st.success("Todo edited!")
            st.experimental_rerun()
    else:
        st.warning("No todos to edit.")

elif user_input == 'exit':
    st.stop()
