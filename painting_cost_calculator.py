from constants import COLOR_COEFFICIENTS, PART_COEFFICIENTS, BASE_PRICE # type: ignore

class PaintingCostCalculator:
    def __init__(self):
        self.color_coefficients = COLOR_COEFFICIENTS
        self.part_coefficients = PART_COEFFICIENTS
        self.base_price = BASE_PRICE

    def calculate_cost(self, part, color):
        if part not in self.part_coefficients:
            return f"Деталь '{part}' не найдена в списке доступных деталей."
        if color not in self.color_coefficients:
            return f"Цвет '{color}' не найден в списке доступных цветов."
        
        part_coefficient = self.part_coefficients[part]
        color_coefficient = self.color_coefficients[color]
        
        total_cost = self.base_price * part_coefficient * color_coefficient
        return f"Стоимость покраски детали '{part}' в цвет '{color}' составляет {total_cost:.2f} рублей."