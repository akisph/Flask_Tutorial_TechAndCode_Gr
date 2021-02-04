from flask import Flask,render_template,request,url_for
import json
from datetime import datetime


# initialize a flask object
app = Flask(__name__) 

# if we have a todo list
# that we want to appear to template


def getTodos():
    with open('todos.json',encoding="utf8") as json_file:
        todos = json.load(json_file)
        return todos

def addTodo(todo):
    todos = getTodos()
    todos.append(todo)
    with open('todos.json','w',encoding='utf8') as json_file:
        json.dump(todos,json_file,ensure_ascii=False)


@app.route('/home',methods = ['GET', 'POST'])
@app.route('/',methods = ['GET', 'POST'])
def index():
    if flask.request.method =='POST':
        todo = request.form.get('todo_name','') # Make a request
        now = datetime.now()
        todoDict = {
            "id": int(datetime.timestamp(now)),
            "name":todo_name,
            "status" : 0 ,
            "created_at": now.strftime("%d-%m-%Y %H:%M:%S"),
            "deadline":null}
        addTodo(todoDict)
    # if we write request.values.get() it takes the variable from wherever it migth come.
    return render_template('index.html',todos=getTodos(),todo=todo) # send this variable inside. 



@app.route('/todolist/<name>') # By defining the todo list we can say that we will see this page ins http://localhost/todolist
def todolist(name):
    return render_template('todolist.html',name=name)    

if __name__ == '__main__':
    app.run(debug = True) # start flask if we want to run through python    
    # with debug True each time we make a change the page refresh by itself.
