
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
employees = [
    {"id": 1, "name": "John", "role": "Data Scientist"},
    {"id": 2, "name": "David", "role": "AI Engineer"}
]

# GET -  Retrieve all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees), 200


# GET - Retrieve employee by ID
@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = next((e for e in employees if e["id"] == emp_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee), 200


# POST - Create a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("role"):
        return jsonify({"error": "Name and role are required"}), 400

    new_employee = {
        "id": max((e["id"] for e in employees), default=0) + 1,
        "name": data["name"],
        "role": data["role"]
    }

    employees.append(new_employee)

    return jsonify(new_employee), 201


# PUT - Update an employee
@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    employee = next((e for e in employees if e["id"] == emp_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    employee["name"] = data.get("name", employee["name"])
    employee["role"] = data.get("role", employee["role"])

    return jsonify(employee), 200


# DELETE - Remove an employee
@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    global employees

    employee = next((e for e in employees if e["id"] == emp_id), None)

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    employees = [e for e in employees if e["id"] != emp_id]

    return jsonify({"message": "Employee deleted successfully"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
