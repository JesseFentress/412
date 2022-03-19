class Student:

    def __init__(self, list):
        self.id = list[0]
        self.first_name = list[1]
        self.last_name = list[2]
        self.email = list[3]
        self.major = list[4]

    def get_id(self):
        return self.id
    
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_major(self):
        return self.major

    def get_all(self):
        return [self.id, self.first_name, self.last_name, self.email, self.major]