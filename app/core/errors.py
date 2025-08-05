"""Custom Exception"""


class TaskNotFoundException(Exception):

    def __init__(self, model_id: str):
        super().__init__(f"Item {model_id} not found.")
