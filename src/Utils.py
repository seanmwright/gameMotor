import pyglet

class Text( object ):
    def __init__(self, text, fontSize, position):
        self.text = text
        self.label = self.createLabel( text, fontSize, position )

    def createLabel( self, text, fontSize, position ):
        label = pyglet.text.Label(
                str(text),
                font_name='Droid Sans',
                font_size=fontSize,
                x=position[0], y=position[1],
                anchor_x='center', anchor_y='center'
        )
        self.fontSize = fontSize
        self.position = position
        return label

    def highlight(self):
        self.label.color = (255,0,0,255)

    def unhighlight(self):
        self.label.color = (255,255,255,255)

    def move(self, position):
        self.label.x = position[0]
        self.label.y = position[1]

    def draw(self):
        self.label.draw()

    def update(self, text):
        self.label.text = str(text)

