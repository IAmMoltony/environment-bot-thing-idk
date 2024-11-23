import json

def is_valid_difficulty(difficulty):
    return difficulty == 'easy' or difficulty == 'normal' or difficulty == 'hard'

def is_valid_json_task(json_task):
    return isinstance(json_task, dict) and 'difficulty' in json_task.keys() and isinstance(json_task['difficulty'], str) and 'title' in json_task.keys() and isinstance(json_task['title'], str) and 'body' in json_task.keys() and isinstance(json_task['body'], str)

class Task:
    def __init__(self, difficulty, title, body):
        # title and body need to have periods preceded with a slash because of formatting
        self.title = title.replace('.', '\\.')
        self.body = body.replace('.', '\\.')

        self.difficulty = difficulty
        if not is_valid_difficulty(self.difficulty):
            raise Exception(f'{self.difficulty} is not a valid task difficulty.')

    def __str__(self):
        return f'Task: *{self.title}*\nDifficulty: *{self.difficulty}*\n\n{self.body}'

def load_tasks():
    tasks = []
    with open('./tasks.json', 'r') as tasks_file:
        tasks_json = json.load(tasks_file)
        for task in tasks_json['tasks']:
            if is_valid_json_task(task):
                tasks.append(Task(task['difficulty'], task['title'], task['body']))
            else:
                print('Found invalid task in tasks.json file. Skipping.')
    return tasks
