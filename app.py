from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for to-do items
todo_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_todo():
    item = request.form.get('item')
    if item:
        todo_items.append(item)
        return jsonify({'items': todo_items})
    return jsonify({'error': 'No item provided'}), 400

@app.route('/remove', methods=['POST'])
def remove_todo():
    item = request.form.get('item')
    if item in todo_items:
        todo_items.remove(item)
        return jsonify({'items': todo_items})
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': todo_items})

if __name__ == '__main__':
    app.run(debug=True)
