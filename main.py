import sys
import json
import os

TODO_FILE = 'todo.json'

def load_todos():
	if not os.path.exists(TODO_FILE):
		return []
	with open(TODO_FILE, 'r') as f:
		return json.load(f)

def save_todos(todos):
	with open(TODO_FILE, 'w') as f:
		json.dump(todos, f, indent=2)

def add_todo(task):
	todos = load_todos()
	todos.append({'task': task, 'completed': False})
	save_todos(todos)
	print(f'Added: {task}')

def list_todos():
	todos = load_todos()
	if not todos:
		print('No to-dos found.')
		return
	for idx, todo in enumerate(todos, 1):
		status = '[x]' if todo['completed'] else '[ ]'
		print(f'{idx}. {status} {todo["task"]}')

def complete_todo(index):
	todos = load_todos()
	if 0 <= index < len(todos):
		todos[index]['completed'] = True
		save_todos(todos)
		print(f'Marked as completed: {todos[index]["task"]}')
	else:
		print('Invalid to-do number.')

def print_help():
	print('To-Do List Usage:')
	print('  python main.py add "task description"')
	print('  python main.py list')
	print('  python main.py complete <number>')

def main():
	if len(sys.argv) < 2:
		print_help()
		return
	cmd = sys.argv[1]
	if cmd == 'add' and len(sys.argv) >= 3:
		add_todo(' '.join(sys.argv[2:]))
	elif cmd == 'list':
		list_todos()
	elif cmd == 'complete' and len(sys.argv) == 3 and sys.argv[2].isdigit():
		complete_todo(int(sys.argv[2]) - 1)
	else:
		print_help()

if __name__ == '__main__':
	main()
