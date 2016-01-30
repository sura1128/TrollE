#ProductList File
#Contains a list of products, mapped by key {UID} to Product {Name, Price, UID}

class ProductList:
    
    def set_prod_map(self, prodMap):
        print("Setting map");
        self.__prodMap = prodMap

    def populate_map(self, name, product):
        self.__prodMap[name] = product;

    def get_product_map(self):
        return self.__prodMap
