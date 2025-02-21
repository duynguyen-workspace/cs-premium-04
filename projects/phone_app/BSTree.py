class Node:
    def __init__(self, iphone):
        self.key = iphone["price"]
        self.info = [iphone]
        self.left = None
        self.right = None


def insert(root, iphone):
    if root is None:
        return Node(iphone)

    if root.key < iphone["price"]:
        root.right = insert(root.right, iphone)
    elif root.key > iphone["price"]:
        root.left = insert(root.left, iphone)
    else:
        root.info.append(iphone)

    return root

def find_phone(root, min_price, max_price, results=None):
    if results is None:
        results = []
        
    if root is None:
        return results

    #* Current price larger than minimum price -> traverse to left node
    if root.key > min_price:
        find_phone(root.left, min_price, max_price, results)
        
    #* Current price smaller than maximum price -> traverse to right node
    if root.key < max_price:
        find_phone(root.right, min_price, max_price, results)
        
    #* take out product in the price range
    if root.key >= min_price and root.key <= max_price:
        results.extend(root.info)
        
    return results