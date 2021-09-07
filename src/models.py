from flask_sqlalchemy import SQLAlchemy
from random import randint 

db = SQLAlchemy()

class FamilyTree:
    def __init__(self, last):
        self.last = last

        self.members = [ { 
            'id' : 1,
            'first' : 'Tato',
            'last' : self.last,
            'age' : 89,
            'parent' : None,
            'child' : [3, 4, 5, 6, 7],
            'URL' : os.environ.get('BACKEND_URL')
        } ,
        {
            'id' : 2,
            'first' : 'Tata',
            'last' : self.last,
            'age' : 82,
            'parent' : NotImplementedError,
            'child' : [3, 4, 5, 6, 7],
        },
         {
            'id' : 3,
            'first' : 'Tio Quique',
            'last' : self.last,
            'age' : 70,
            'parent' : [1, 2],
            'child' : None
        },
         {
            'id' : 4,
            'first' : 'Tia Mayu',
            'last' : self.last,
            'age' : 57,
            'parent' : [1, 2],
            'child' : None
        },
         {
            'id' : 5,
            'first' : 'Tia Nena',
            'last' : self.last,
            'age' : 40,
            'parent' : [1, 2],
            'child' : None
        },
         {
            'id' : 6,
            'first' : 'Tio Carlos',
            'last' : self.last,
            'age' : 50,
            'parent' : [1, 2],
            'child' : None
        },
        {
            'id' : 7,
            'first' : 'Papá',
            'last' : self.last,
            'age' : 57,
            'parent' : [1, 2],
            'child' : [9, 10]
        },
        {
            'id' : 8,
            'first' : 'Mamá',
            'last' : self.last,
            'age' : 59,
            'parent' : None,
            'child' : [9, 10],
        },
        {
            'id' : 10,
            'first' : 'Ale',
            'last' : self.last,
            'age' : 22,
            'parent' : [8, 7],
            'child' : None
        },
        {
            'id' : 11,
            'first' : 'Lucy',
            'last' : self.last,
            'age' : 25,
            'parent' :  [8, 7],
            'child' : None
        }
        ]
    
    def memberId(self, id):
        for miembro in self.members:
            if miembro['id'] == int(id):
                return miembro
        return None
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e