
import re

print('Greet to Madlib competition')

"""
create a function  called a  read_template that take a path
and open text file and read the content inside the file  and return the file 

"""
def read_template(path):
    fileOpen=open(path)
    fileRead =fileOpen.read()
    return fileRead

"""
create a function  called a  parse_template
convert the string to array by return the 2 things 1st part is text and 2ed is  the tuple
"""


def parse_template(input):

    strippd=''

    original_text=[]

    new=input.split(' ')

    print(new)

    regulare=r"^{\w+}|\.$"

    for input1 in new:

        if re.match(regulare,input1)==None :

            strippd+=f"{input1} "

        else :

            if input1==new[-1] :

                strippd+= '{}.' 

                original_text+=[input1[1:-2]]

                
            else :

                original_text+=[input1[1:-1]]

                strippd+='{} '

    actual_parts=tuple(original_text)

    return (strippd,actual_parts)








"""
make  function named is marge that  tack string and tuple as par
ameter 

and  what the tuple has  included the string like  format
"""

def merge(input_text,tub) :

    return  input_text.format(*tub)




    """
     create a function that creat a file named newFile in assets folder
    
    """

def create_file(newFile):


    with open("assets/new_file.txt", "w") as f:

        f.write(newFile)


