import uuid
from ....context_wrapper import ContextWrapper
from ....helpers import Color
from shared_python.shared_math.geometry import Vec2


class Shape:
    def __init__(self, pos: Vec2, radius: float, color: Color):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.id = uuid.uuid4()

    def contains(self, pos: Vec2):
        distance = ((pos.x - self.pos.x) ** 2 +
                    (pos.y - self.pos.y) ** 2) ** 0.5
        return distance <= self.radius

    def translate(self, pos: Vec2):
        self.pos.translate(pos)

    def draw(self, context: ContextWrapper):
        context.set_color(self.color)
        context.draw_circle(self.pos, self.radius)
