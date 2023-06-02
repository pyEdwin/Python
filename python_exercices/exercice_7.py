class Todo:
    
    status ={False:'Incomplete' , True:'Complete'}
    def __init__(self , name , description , points , completed=False):
        self.name = name
        self.description = description
        self.points = points
        self.completed = completed
    def __repr__(self) :
        return f"Name:{self.name}\nStatus:{self.status[self.completed]}\nPonts:{self.points}\nDescription:{self.description}"

class TodoList:

    def __init__(self, todos):
        self.todos = todos

    def average_points(self):
        total = 0
        for todo in self.todos:
            total +=todo.points
        return total / len(self.todos)

    def completed(self):
        results = []
        for todo in self.todos:
            if todo.completed:
                results.append(todo)
        return results
      
    def incompleted(self):
        results = []
        for todo in self.todos:
            if not todo.completed:
                results.append(todo)
        return results

user  = Todo("Pierre" , "wash clothes" , 1 )
print(repr(user))