from datetime import date

todo_list = []
done_list = []

def mymenu():
    print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
$ ./todo exit             # exit from program""")

# def mymenu():
#     print("""\n\nUsage :-
# $ add "todo item"  # Add a new todo
# $ ls               # Show remaining todos
# $ del NUMBER       # Delete a todo
# $ done NUMBER      # Complete a todo
# $ help             # Show usage
# $ report           # Statistics
# $ exit             # exit from program""")

def ls():
    i = 1
    for each in todo_list:
        print("[{0}] {1}".format(i,each))
        i = i+1;

def add(task):
    #task = input("\n\nEnter the task : ")
    todo_list.append(task)

def done(number):
    #number = eval(input("\nEnter the task number to mark as done : "))
    print("\n\nmarked to do #{0} as done.".format(number))
    done_list.append(todo_list[(number-1)])
    todo_list.remove(todo_list[(number-1)])

def report():
    count_in_todo_list = len(todo_list)
    count_in_done_list = len(done_list)
    print("\n\n{0} Pending : {1} completed : {2}".format(date.today(),count_in_todo_list,count_in_done_list))

def delete(num):
    #num = eval(input("\nEnter the number : "))
    todo_list.remove(todo_list[num-1])

def todo():
    while(True):
        choice = input("\n\n$ ./todo ")
        tstr=""
        for i in range(0,len(choice)):
            if choice[i]==" ":
                break
    
        tstr = choice[i+1:]
        if choice[:3] == 'add':
            add(tstr)
        elif choice[:4] == 'help':
            mymenu()
        elif choice[:2] == 'ls':
            ls()
        elif choice[:4] == 'done':
            done(int(tstr))
        elif choice[:6] == 'report':
            report()
        elif choice[:4] == 'exit':
            break
        elif choice[:3] == 'del':
            delete(int(tstr))
        else:
            print("Enter a valid choice!! ")


if __name__=="__main__":
    mymenu()
    todo()