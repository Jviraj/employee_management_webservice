from flask import Flask, request, jsonify

import json

global employeeid, employees, data_glbl, filename
employeeid = 0

filename = "data.json"


def emptyJsonFile():
    with open(filename, 'w') as json_file:
        pass


# Load initial data from JSON file
try:
    with open(filename, "r") as json_file:
        employees = json.load(json_file)

        # Loop through employees to find the highest employee ID
        for employee in employees:
            if int(employee["employeeId"]) > employeeid:
                employeeid = int(employee["employeeId"])
except:
    employees = []

app = Flask(__name__)

# Greeting


@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

# Create Employee


@app.route('/employee', methods=['POST'])
def create_employee():
    global employeeid, employees, data_glbl, filename
    employeeid += 1
    data = request.json
    city = data.get('city', 'City not provided')
    name = data.get('name', 'Name not provided')
    new_employee = {"employeeId": str(
        employeeid), "name": str(name), "city": str(city)}
    employees.append(new_employee)
    emptyJsonFile()
    with open(filename, "w") as json_file:
        json.dump(employees, json_file)
    response = {
        "employeeId": str(employeeid)
    }
    return jsonify(response), 201

# Get all Employee details


@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    global employees
    response = employees
    return jsonify(response), 200

# Get Employee details


@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    global employees
    for employee in employees:
        if employee["employeeId"] == id:
            return employee
    return {"error": "Employee not found"}

# Update Employee


@app.route('/employee/<id>', methods=['PUT'])
def update_employee(id):
    global employees
    found = False
    data = request.json
    for employee in employees:
        if employee["employeeId"] == id:
            employee["name"] = data.get("name", employee["name"])
            employee["city"] = data.get("city", employee["city"])
            response = employees
            found = True
    if found == True:
        with open(filename, "w") as json_file:
            json.dump(employees, json_file)
        return jsonify(response), 201

    response = {"message": "Employee with "+str(id)+" was not found"}
    return jsonify(response), 404

# Delete Employee


@app.route('/employee/<id>', methods=['DELETE'])
def delete_employee(id):
    global employees, filename
    newlist = []
    found = False
    for employee in employees:
        if employee["employeeId"] == id:
            found = True
        else:
            newlist.append(employee)
    if found == True:
        response = newlist
        employees = newlist
        with open(filename, "w") as json_file:
            json.dump(employees, json_file)
        return jsonify(response), 200
    response = {"message": "Employee with id: "+id+" was not found"}
    return jsonify(response), 404


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
