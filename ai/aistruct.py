from dataclasses import dataclass

@dataclass
class Property:
    name: str
    memory: str
    personallity: str
    follow : dict[str, bool]



class AI:
    def __init__(self, property : Property):
        self.property = property

    def read(self):
        return 0
    
    def write(self):
        return 0
    
    def comment(self):
        return 0
    
    def follow(self):
        return 0
    
    def follow_agreement(self):
        return 0
    
