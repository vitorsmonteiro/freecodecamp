from turtle import width


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_height(self, value):
        self.height = value
    
    def set_width(self, value):
        self.width = value
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = ""
        for i in range(self.height):
            line += "*" * self.width + "\n"
        return line
    
    def get_amount_inside(self, obj):
        horz_fit = int(self.width / obj.width)
        vert_fit = int(self.height / obj.height)
        return horz_fit * vert_fit
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)
        
    def set_width(self, value):
        self.side = value
        self.width = value
        self.height = value
    
    def set_height(self, value):
        self.side = value
        self.width = value
        self.height = value
        
    def set_side(self, value):
        self.side = value
        self.width = value
        self.height = value
        
    def __str__(self):
        return f"Square(side={self.side})"
