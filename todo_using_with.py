""" user_prompt = "Enter a todo:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo) """

""" todos = []

while True:
    user_action = input("Type add, show, or exit: ")

    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif user_action == "show":
        print(todos)
    else:
        break """     


""" todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case 'exit':
            break """
        
todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt",'r')as file: # with open("todos.txt",r) as file:
                                         #  todos = file.readlines()S                  
                todos = file.readlines() 

            todos.append(todo)   
            with open("todos.txt",'w')as file: 
                                                           
                file.writelines(todos)        
        
        case 'show':
            with open("todos.txt",'r')as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            with open("todos.txt",'r')as file:
                todos = file.readlines()
            
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new todo: ") + "\n"
            todos[number] = new_todo
            
            with open('todos.txt','w')as file:
                todos = file.writelines(todos)
        case 'exit':
            break
