class Item():
    def __init__(self, type, model_num,details):
        self._type = type
        self._model_num = model_num
        self._details = details
    
    def get_type(self):
        return self._type

    def set_type(self,type):
        self._type = type
    
    def get_model_number(self):
        return self._model_num
    
    def set_model_number(self, model_number):
        self._model_number = model_number

    def get_details(self):
        return self._details

    def set_details(self,details):
        self._details = details

class Others(Item):
    def __init__(self, type, model_num, details):
        super().__init__(type, model_num, details)