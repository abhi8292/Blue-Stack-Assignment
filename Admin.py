import credentials


class Admin:
    ROLE_TYPE = 'ADMIN'
    ACCESS_Type = ['READ', 'WRITE', 'UPDATE', 'DELETE']

    def __init__(self, name):
        self.name = name
        self.ROLE_TYPE = Admin.ROLE_TYPE
        self.ACCESS_Type = Admin.ACCESS_Type

    def getRole(self):
        return self.ROLE_TYPE

    def getAccess(self):
        return self.ACCESS_Type

    def showMe(self):
        print('Role Type : ', self.ROLE_TYPE)
        print('Access Type : ', self.ACCESS_Type)

    def showUsers(self):
        if self.getRole() != 'ADMIN':
            return False
        else:
            return credentials.userPassword
