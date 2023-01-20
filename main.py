from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Machine(BaseModel):
    id: int
    name: str
    location: str
    stock: dict

machines = []

@app.post("/vm")
def createVm(vm: Machine):
    vm.id = len(machines) + 1
    machines.append(vm)
    return {"id": vm.id}

@app.delete("/vm/{id}")
def deleteVm(id: int):
    for i, machine in enumerate(machines):
        if machine.id == id:
            del machines[i]
            return {"message": "vm deleted."}
    return {"message": "vm not found."}

@app.put("/vm/{id}")
def updateVm(id: int, vm: Machine):
    for machine in machines:
        if machine.id == id:
            machine.name = vm.name
            machine.location = vm.location
            machine.stock = vm.stock
            return {"id": id}
    return {"message": "vm not found."}

@app.get("/vm/{id}")
def getVm(id: int):
    for machine in machines:
        if machine.id == id:
            return machine
    return {"message": "vm not found."}

@app.post("/vm/{id}/add-item")
def addItemToVm(id: int, item: str, quantity: int):
    for machine in machines:
        if machine.id == id:
            if item in machine.stock:
                machine.stock[item] += quantity
            else:
                machine.stock[item] = quantity
            return {"message": f"{quantity} {item} added to vm."}
    return {"message": "vm not found."}

@app.put("/vm/{id}/edit-item")
def editItemInVm(id: int, item: str, quantity: int):
    for machine in machines:
        if machine.id == id:
            if item in machine.stock:
                machine.stock[item] = quantity
                return {"message": f"{item} in vm stock set to {quantity}."}
            else:
                return {"message": f"{item} not found in vm stock."}
    return {"message": "vm not found."}

@app.delete("/vm/{id}/remove-item")
def removeItemFromVm(id: int, item: str):
    for machine in machines:
        if machine.id == id:
            if item in machine.stock:
                del machine.stock[item]
                return {"message": f"{item} removed from vm stock."}
            else:
                return {"message": f"{item} not found in vm stock."}
