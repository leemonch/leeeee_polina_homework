class SmartString:
    def __init__(self, value):
        self.value = str(value)
    def __len__(self):
        return len(set(self.value))
    def __str__(self):
        lenn = len(self.value)
        unique = self.__len__()
        return f"{self.value} ({lenn}, {unique})"
    def __add__(self, value2):
        if isinstance(value2, SmartString):
            new_value = self.value + value2
        else:
            new_value = self.value + str(value2)
        return SmartString(new_value)
# stroka = SmartString("bebebe")
# print(len(stroka))       
# print(str(stroka))        
# stroka2 = stroka + "lelele"
# print(str(stroka2))     
