class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type,
                 duration,
                 distance,
                 speed,
                 calories,
                 ):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories       
    
    
    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.;' 
                f'Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.')

M_IN_KM = 1000
LEN_STEP = 0.65
CALORIES_MEAN_SPEED_MULTIPLIER = 18
CALORIES_MEAN_SPEED_SHIFT = 1.79
CONSTANT1 = 0.035
CONSTANT2 = 0.029

class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        

    def get_distance(self, distance: float) -> float:
        """Получить дистанцию в км."""
        self.distance = distance        
        distance = self.action * LEN_STEP / M_IN_KM
        return distance
    
        

    def get_mean_speed(self, mean_speed) -> float:
        """Получить среднюю скорость движения."""
        self.mean_speed = mean_speed
        mean_speed = self.distance/self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage.get_message()

class Running(Training):
    """Тренировка: бег."""
    
    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
    
    def get_distance(self, distance: float) -> float:
        return super().get_distance(distance)
    

    def get_mean_speed(self, mean_speed) -> float:
        return super().get_mean_speed(mean_speed)


    def get_spent_calories(self) -> float:
        spent_calories = ((CALORIES_MEAN_SPEED_MULTIPLIER * super().mean_speed
                         + CALORIES_MEAN_SPEED_SHIFT) * self.weight / M_IN_KM * super().duration)                           ) 
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight, height)


    def get_distance(self, distance: float) -> float:
        return super().get_distance(distance)
 
   
    def get_mean_speed(self, mean_speed) -> float:
        return super().get_mean_speed(mean_speed)
    
    def get_spent_calories(self) -> float:
        spent_calories = ((CONSTANT1 * self.weight + ((super().mean_speed/3.6)**2 / self.height) 
                           * CONSTANT2 * self.weight) * super().duration)
        return spent_calories
    

class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, action: int, duration: float, weight: float, lenght_pool, count_pool) -> None:
        super().__init__(action, duration, weight, lenght_pool, count_pool)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_distance(self, distance: float) -> float:
        return super().get_distance(distance) 

    
    def get_mean_speed(self) -> float:
        mean_speed = self.lenght_pool * self.count_pool / M_IN_KM / super().duration
        return mean_speed
    

    def get_spent_calories(self) -> float:
        spent_calories = ((super().get_mean_speed + 1.1) * 2 * self.weight * super().duration)
        return spent_calories


           


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

