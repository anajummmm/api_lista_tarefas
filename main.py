from flask import Flask, request

app = Flask(__name__)

tarefas = [
    {
        "id":1,
        "titulo": "Estudar Java",
        "descricao":"Estudar Java para aprender construir tarefas ",
        "status":"Em andamento ",
        "data_inicio":"20/02/2025",
        "professor":"Moises",
        "observacoes": "Materia complicada"
    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para aprender sobre Web services ",
        "status": "Nao iniciado ",
        "data_inicio":"16/01/2025",
        "professor":"Moises",
        "observacoes": "Materia fundamental"
    }
]
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id')== task_id:
            return tarefa
    return 'Tarefa nao encontrada '

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['data_inicio'] = task_body.get('data_inicio')
    task_search['professor'] = task_body.get('professor')
    task_search[('observacoes')] = task_body.get('observacoes')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
            return {'message': 'Tarefa foi deletada'}
    return {'message': 'Tarefa não encontrada, arquivo excluido'}


if __name__ == '__main__':
    app.run(debug=True)