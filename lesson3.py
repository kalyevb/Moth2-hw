class PassaordManager():
    old_password = ['asdasd', '12312', 'qwe123']

    def set_password(self, password):
        self.old_password.append(password)

    def get_password(self):
        return self.old_password[-1]

    def get_iscorrect(self, password1):
        pass #Доделать


passw = PassaordManager()
passw.set_password(password=input("enter password"))
print(passw.get_password())
passw.get_iscorrect(password1=input("Enter number"))
print(passw.get_iscorrect())