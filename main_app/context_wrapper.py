from abc import ABC, abstractmethod
from functools import singledispatchmethod
from shared_python.shared_math.geometry import Rect, Vec2, BezierPathA, BezierContour, BezierPath, BezierPoint
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

    @abstractmethod
    def draw_path(self, path: BezierPathA) -> None:
        pass


class ContextWrapperSkia(ContextWrapper):
    def __init__(self, surface):
        self.surface = surface
        self.paint = skia.Paint()
        self.paint.setAntiAlias(True)

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

    def draw_path(self, path: BezierPathA) -> None:
        skia_path = skia.Path()
        self.paint.setStyle(self.paint.kStroke_Style)

        for bezier_path in path.paths:
            skia_path = skia.Path()

            for contour in bezier_path.contours:
                num_points = len(contour.points)

                for i in range(num_points):
                    current_point = contour.points[i].pos
                    next_point = contour.points[(i + 1) % num_points].pos
                    next_control1 = contour.points[(
                        i + 1) % num_points].control1
                    prev_control2 = contour.points[i].control2

                    if i == 0:
                        skia_path.moveTo(current_point.x, current_point.y)

                    if next_control1 and prev_control2:
                        skia_path.cubicTo(
                            prev_control2.x, prev_control2.y,
                            next_control1.x, next_control1.y,
                            next_point.x, next_point.y
                        )
                    else:
                        skia_path.lineTo(next_point.x, next_point.y)

                if contour.closed:
                    skia_path.close()
            self.surface.drawPath(skia_path, self.paint)
