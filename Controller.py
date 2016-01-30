#Controller File

class Controller:

    
    def __init__(self, prodMap):
        self.__prodMap = prodMap

    def setup(self):
        from ProductList import ProductList
        prodList = ProductList()
        prodList.set_prod_map({})

        with open("products.txt") as f:            
            lines = f.readlines()
        f.closed

        for x in range(0,len(lines)-1):
            words = lines[x].rstrip().split(',')
            from Product import Product
            prod = Product(words[0], words[1], words[2],x)
            prodList.populate_map(words[0], prod)
        
        self.__prodMap = prodList.get_product_map()

    def get_product_map(self):        
        return self.__prodMap
