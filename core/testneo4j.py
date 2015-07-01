from py2neo import Graph, Node, Relationship

class Person(object):

    def __init__(self):
        self.graph = Graph()
        #do nothing

    def createPerson(self, name, fullname, occupation, homepage, wikipedia_link):
        person = Node('Person', name=name, fullname=fullname, occupation=occupation, homepage=homepage, wikipedia_link=wikipedia_link)
        self.graph.create(person)
        return person
