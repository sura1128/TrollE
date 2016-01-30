#Product File
#Contains Product {Name, Price, UID}

class Product:
    def __init__(self, name, price, uid, index):   
        self.__name = name
        self.__price = price
        self.__uid = uid
        self.__index = index

    def get_uid(self):
        return self.__uid

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_index(self):
        return self.__index
