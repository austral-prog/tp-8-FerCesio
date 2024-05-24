
def get_coordinate(x):
    return x[1]
get_coordinate(("hola", "2A"))


def convert_coordinate(x):
    return (x[0],x[1])
convert_coordinate("2A")

def create_record(x,y):
    a,b = y[1]
    if x[1] ==  (a+b):
        return x+y
    else:
        return "not a match"
create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))


