print('Greet to Madlib competition')

"""
create a function  called a  read_template that take a path
and open text file and read the content inside the file  and return the file 

"""
def read_template(path):
    fileOpen=open(path)
    fileRead =fileOpen.read()
    return fileRead
