from abc import ABC, abstractmethod
from functools import singledispatchmethod
from shared_python.shared_math.geometry import Rect, Vec2
from typing import overload
from skia import *
import skia


class ContextWrapper(ABC):
    @overload
    def draw_rect(self, r: Rect) -> None:
        pass

    @overload
    def draw_rect(self, x: float, y: float, width: float, height: float) -> None:
        pass

    @abstractmethod
    def draw_circle(self, center: Vec2, radius: float) -> None:
        pass

    @abstractmethod
    def set_color(self, color) -> None:
        pass


class ContextWrapperSkia(ContextWrapper):
    def __init__(self, surface):
        self.surface = surface
        self.paint = skia.Paint()

    def set_color(self, color) -> None:
        if not isinstance(color, int):
            color = Color(color.r, color.g, color.b)

        self.paint.setColor(color)

    def draw_circle(self, center: Vec2, radius: float) -> None:
        self.surface.drawCircle(
            center.x, center.y, radius, self.paint)

    @overload
    def draw_rect(self, r: Rect) -> None:
        ...

    @overload
    def draw_rect(self, x: float, y: float, width: float, height: float) -> None:
        ...

    def draw_rect(self, r: Rect) -> None:
        self.surface.drawRect(
            skia.Rect(r.minx, r.miny, r.width(), r.height()), self.paint)

    def draw_rect(self, x: float, y: float, width: float, height: float) -> None:
        rect = skia.Rect(x, y, x + width, y + height)
        self.surface.drawRect(rect, self.paint)
