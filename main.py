import User
import credentials

"""
hi! you are logged in as admin
press 1 for login as another user
press 2 for create user
press 3 for edit role
"""


def errorhandler():
    print('Invalid Option !!! Enter valid option')


class Main:
    flagLogin = False
    currentUser = None

    def __init__(self):
        Main.currentUser = User.UserClass.createAdminUser('Abhimanyu', 'Abhi', '1234')
        Main.options()

    @classmethod
    def options(cls):
        while True:
            if Main.flagLogin:
                print('''
                1 : Logout
                2 : Create Admin User
                3 : Create Normal User
                4 : InFo about me
                5 : Show All Users
                6 : Assign Admin Role To User
                7 : Remove Admin Role
                8 : Exit
                ''')
            else:
                print('''
                1 : Login
                2 : Exit
            ''')

            try:
                choice = int(input('Enter Your choice'))
                if choice == 8 and Main.flagLogin:
                    print('Bye Bye user')
                    break
                elif choice == 3 and Main.flagLogin:
                    if User.UserClass.createNormalUser(userObj=Main.currentUser):
                        print('User Created successfully')
                    else:
                        print("Either you don't have permission or username already exist")
                elif choice == 2 and Main.flagLogin:
                    if User.UserClass.createAdminUser(userObj=Main.currentUser):
                        print('Admin Created Successfully')
                    else:
                        print("Either you don't have permission or username already exist")

                elif choice == 2 and (not Main.flagLogin):
                    print('Bye Bye user')
                    break
                elif choice == 1 and (not Main.flagLogin):
                    Main.currentUser = User.UserClass.login()
                    if Main.currentUser:
                        Main.flagLogin = True
                elif choice == 1 and Main.flagLogin:
                    User.UserClass.logout()
                    Main.flagLogin = False
                    Main.currentUser = None
                elif choice == 4 and Main.flagLogin:
                    User.UserClass.info(Main.currentUser)

                elif choice == 7 and Main.flagLogin:
                    username = input('Enter UserName of user , whome you want to change')
                    if username in credentials.userPassword.keys():
                        userObj = credentials.users[credentials.userPassword.get(username).get("id")]
                        res = User.UserClass.removeAdminRole(Main.currentUser, userObj)

                        if isinstance(res, str):
                            print(res)
                        else:
                            if res:
                                print("Roles has changes successfully")
                            else:
                                print("User is not authorized to change")
                    else:
                        print('UserName is incorrect')

                elif choice == 6 and Main.flagLogin:
                    username = input('Enter UserName of user , whome you want to change')
                    userObj = None
                    if username in credentials.userPassword.keys():
                        userObj = credentials.users[credentials.userPassword.get(username).get("id")]
                        res = User.UserClass.giveAdminRole(Main.currentUser, userObj)

                        if isinstance(res, str):
                            print(res)
                        else:
                            if res:
                                print("Roles has changes successfully")
                            else:
                                print("User is not authorized to change")
                    else:
                        print('UserName is incorrect')

                elif choice == 5 and Main.flagLogin:
                    data = Main.currentUser.showUsers()
                    if data:
                        print(data)
                    else:
                        print("You don't have permission to access this ")
            except ValueError:
                print('Invalid Input')
                Main.options()


m1 = Main()
