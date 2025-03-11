class Tarefa:

    def __init__(self, task_id, titulo, descricao, status, data_inicio, professor, observacoes):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_inicio = data_inicio
        self.professor = professor
        self.observacoes = observacoes

    def to_json(self):
        return {
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_inicio": self.data_inicio,
            "professor": self.professor,
            "observacoes": self.observacoes
        }