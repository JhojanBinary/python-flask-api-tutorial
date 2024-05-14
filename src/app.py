from flask import Flask, jsonify,request

app = Flask(__name__)


todos =[
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False},
    {"label": "My third task", "done": False},
    {"label": "My fourth task", "done": False},
    {"label": "My five task", "done": False}

]

@app.route('/todos',methods=['GET'])
def hello_world():

    task = jsonify(todos)
    return task





@app.route('/todos', methods=['POST'])
def  add_new_todo():
    request_body = request.json
    

    if 'label'and 'done' in request_body:
        todos.append(request_body)
        return jsonify(todos)
    else:
         return({'error': 'LABEL and DONE is requerid'})




@app.route('/todos/<int:position>', methods = ['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    position = int (position)
    
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos)

    else:
        return ({'error' : 'value no valid'})





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)