import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['todo'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state['todo'] = ''

def complete_todo():
    new_todo = st.session_state['todo'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state['todo'] = ''

st.title('My todo app')
st.subheader('This is my todo app')
st.write('This app is created ny using python')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Enter a todo',
              placeholder='',
              on_change=add_todo,
              key='todo')

# st.session_state


