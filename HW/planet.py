class Planet:
    def __init__(self, name, radius):
        self.name=name
        self.radius=radius
    def diameter(self):
        return self.radius*2
earth=Planet("Земля", 6371)
print(earth.diameter()) 
