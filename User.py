import credentials
import Admin
import NormalUser


class UserClass(Admin.Admin, NormalUser.NormalUser):

    def __init__(self, name, username, password, flag):
        if flag:
            NormalUser.NormalUser.__init__(name)
            self.id = NormalUser.NormalUser.id
        else:
            Admin.Admin.__init__(name)
            self.id = Admin.Admin.id
        self.username = username
        self.password = password
        Admin.Admin.id = Admin.Admin.id + 1
        NormalUser.NormalUser.id = NormalUser.NormalUser.id + 1

    def __str__(self):
        return '{} {}'.format(self.name, self.id)

    @staticmethod
    def createAdminUser(name=None, username=None, password=None, userObj=None):
        if credentials.Credential.getId() > 0 and userObj.getRole() != 'ADMIN':
            return False
        else:
            if name is None or username is None or password is None:
                name = input('Enter Name')
                username = input('Enter username')
                password = input('Enter password')

            if username in credentials.userPassword.keys():
                return False
            else:
                newAdmin = Admin.Admin(name)
                # newAdmin = UserClass(name,username,password,False)
                credentials.users[credentials.Credential.getId()] = newAdmin
                credentials.userPassword[username] = {"password": password, "id": credentials.Credential.getId()}
                credentials.Credential.increaseID()
                return True

    @staticmethod
    def createNormalUser(name=None, username=None, password=None, userObj=None):
        if userObj.getRole() != 'ADMIN':
            return False
        else:
            if name is None or username is None or password is None:
                name = input('Enter Name')
                username = input('Enter username')
                password = input('Enter password')

            if username in credentials.userPassword.keys():
                return False
            else:
                newAdmin = NormalUser.NormalUser(name)
                credentials.users[credentials.Credential.getId()] = newAdmin
                credentials.userPassword[username] = {"password": password, "id": credentials.Credential.getId()}
                credentials.Credential.increaseID()
                return True

    @staticmethod
    def set_id():
        UserClass.id = UserClass.id + 1

    @staticmethod
    def info(obj):
        print("Name : ", obj.name)
        obj.showMe()

    @staticmethod
    def login():
        print('You are into login module ')
        username = input('Enter Your UserName')
        password = input('Enter you Password')
        print(len(credentials.users))
        print(credentials.userPassword)
        if credentials.userPassword.get(username) and credentials.userPassword[username]["password"] == password:
            user = credentials.users[credentials.userPassword.get(username).get("id")]
            print('User is logged in as ' + user.getRole())
            return user
        else:
            print('user is not loged in')
            return None
        # if username == 'abhi' and password == '1234':
        #     print('User is logged in')
        # else:
        #     print('User Credential is wrong')

    @staticmethod
    def logout():
        print('User is logout')

    @staticmethod
    def giveAdminRole(adminUser, user):
        ROLE_TYPE = 'ADMIN'
        ACCESS_Type = ['READ', 'WRITE', 'UPDATE', 'DELETE']
        if adminUser.getRole() == 'ADMIN':
            if user.getRole() == 'ADMIN':
                return "This User is already an Admin"
            else:
                user.ROLE_TYPE = ROLE_TYPE
                user.ACCESS_Type = ACCESS_Type
                return True

        else:
            return False

    @staticmethod
    def removeAdminRole(adminUser, user):
        ROLE_TYPE = 'USER'
        ACCESS_Type = ['READ']
        if adminUser.getRole() == 'ADMIN':
            user.ROLE_TYPE = ROLE_TYPE
            user.ACCESS_Type = ACCESS_Type
            return True
        else:
            return False
