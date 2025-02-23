from painting_cost_calculator import PaintingCostCalculator # type: ignore

class PaintingService:
    def __init__(self):
        self.calculator = PaintingCostCalculator()

    def run(self):
        print("Добро пожаловать в сервис расчета стоимости покраски!")
        part = input("Введите наименование детали (например, 'Капот', 'Передняя дверь'): ")
        color = input("Введите цвет (например, 'Белый', 'Серый металлик'): ")
        
        result = self.calculator.calculate_cost(part, color)
        print(result)


if __name__ == "__main__":
    service = PaintingService()
    service.run()