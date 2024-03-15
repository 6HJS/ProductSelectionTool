class Item():
    def __init__(self, type, model_num):
        self.type = type
        self.model_num = model_num
    
    @classmethod
    def get_type(self):
        return self.type

    @classmethod
    def set_type(self,type):
        self.type = type
    
    @classmethod
    def get_model_number(self):
        return self.model_num
    
    @classmethod
    def set_model_number(self, model_number):
        self.model_number = model_number