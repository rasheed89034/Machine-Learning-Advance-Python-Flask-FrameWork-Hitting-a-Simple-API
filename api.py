from flask import Flask, request, jsonify

app = Flask(__name__)
## initial data in my to do list 
items = [
    {"id": 1, "itemName": "Apple","description":"Item One"},
    {"id": 2, "itemName": "Banana","description":"Item One"}
]
@app.route("/")
def home():
    return "Welcome To This Sample To Do List App"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods=['Get'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

# POST Method creating a task or adding a new item
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name" : request.json['name'],
        "descrition":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


#Put: Update an item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]== item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    
    # In-Case of put the post request will be just like this
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('descrition',item['descrition'])
    return jsonify(item)


# Deleting item
@app.route('/items/<int:id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result":"item deleted"})


if __name__ == "__main__":
    app.run(debug = True)