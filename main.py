from flask import Flask, request
from tarefa import Tarefa

app = Flask(__name__)

tarefas = [
    Tarefa(task_id=1,
           titulo="Estudar Java",
           descricao="Estudar Java para aprender construir tarefas",
           status="Em andamento",
           data_inicio="20/07/25",
           professor="Moises",
           observacoes="Materia complicada").to_json(),
    Tarefa(task_id=2,
           titulo="Estudar Flask",
           descricao="Estudar Flask para aprender sobre Web Services",
           status="Nao iniciado",
           data_inicio="16/01/2025",
           professor="Moises",
           observacoes="Materia fundamental").to_json()
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            return tarefa
    return {'message': 'Tarefa não encontrada'}, 404

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('task_id') + 1 if tarefas else 1
    task['task_id'] = ultimo_id
    tarefas.append(task)
    return task, 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            task_search = tarefa
            break

    if not task_search:
        return {'message': 'Tarefa não encontrada'}, 404

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo', task_search['titulo'])
    task_search['descricao'] = task_body.get('descricao', task_search['descricao'])
    task_search['status'] = task_body.get('status', task_search['status'])
    task_search['data_inicio'] = task_body.get('data_inicio', task_search['data_inicio'])
    task_search['professor'] = task_body.get('professor', task_search['professor'])
    task_search['observacoes'] = task_body.get('observacoes', task_search['observacoes'])

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            tarefas.remove(tarefa)
            return {'message': 'Tarefa foi deletada'}, 200
    return {'message': 'Tarefa não encontrada'}, 404

if __name__ == '__main__':
    app.run(debug=True)
