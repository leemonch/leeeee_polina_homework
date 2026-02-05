class Meme:
    def __init__(self, template, caption):
        self.template=template
        self.caption=caption
    def post(self):
        return f"[{self.template}]: {self.caption}"
m=Meme("Дратути", "привет")
print(m.post()) 
