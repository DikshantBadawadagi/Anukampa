from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    pin : int

class Patient(BaseModel):
    name : str
    age : int
    address : Address

address_dict = {'street': '123 Main St', 'city': 'New York', 'pin': 10001}

address1 = Address(**address_dict)

patient_dict = {'name': 'John Doe', 'age': 30, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)

temp = patient1.model_dump(include=['name'], exclude={'address': {'pin'}})

print(temp)
print(type(temp))

temp1 = patient1.model_dump_json()
print(temp1)