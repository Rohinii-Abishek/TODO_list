To_do_list =[]
try:
    with open('TODO.txt',"r")as file:
        todos = file.readlines()
        for todo in todos:
            To_do_list.append(todo.strip())
except FileNotFoundError:  
    pass          
while True:  
    user_input = input("Enter the action to perform (add,display,edit,exit): ").strip()
    match user_input:
        case "add":
            action = input("Enter a action to perform : ")
            To_do_list.append(action)
        case "display":
            for index,item in enumerate(To_do_list):
                print(f"{index+1}.{item}")
        case "edit":
            index_to_edit = int(input("Enter the index of the action to be edited: "))  
            index_to_edit = index_to_edit-1
            edited_action = input("You've replaced the action by: ")
            To_do_list[index_to_edit] = edited_action
        case "_":
            print("Enter only the specified action!! Try again!!")
        case "exit":
            with open('TODO.txt','w')as file:
                for todo in To_do_list:
                    file.write(todo + "\n")
            break                      