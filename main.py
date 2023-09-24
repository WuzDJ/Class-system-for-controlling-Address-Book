from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
    # реалізація класу

class Phone(Field):
    def __init__(self, value=None):
        if value is None:
            self.value = None
        elif not value.isdigit() or len(value) != 10:
            raise ValueError
        else:
            self.value = value
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.pop(self.phones.index(p))

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones[self.phones.index(phone)] = Phone(new_phone)
                return None
        raise ValueError

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, user):
        self.data[user.name.value] = user
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data.keys():
            self.data.pop(name) 
    # реалізація класу