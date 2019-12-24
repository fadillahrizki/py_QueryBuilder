from config.Model import Model

class UserModel(Model):
    def __init__(self):
        super().__init__()
        self.table = "users"
