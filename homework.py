class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        message = (f'Тип тренировки: {self.training_type}; '
                   f'Длительность: {self.duration:.3f} ч.;'
                   f' Дистанция: {self.distance:.3f} км;'
                   f' Ср. скорость: {self.speed:.3f} км/ч; '
                   f'Потрачено ккал: {self.calories:.3f}.')
        return message


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65
    MIN_IN_HOUR = 60
    SEC_IN_HOUR = 3600

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ):
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = (self.action * self.LEN_STEP / self.M_IN_KM)
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = type(self).__name__
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        return InfoMessage(training_type, duration, distance, speed, calories)


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    M_IN_KM = 1000
    MIN_IN_HOUR = 60

    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                           * self.get_mean_speed()
                          + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                          / self.M_IN_KM * self.duration * self. MIN_IN_HOUR)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    KMH_IN_MSEC = 0.278
    CONSTANT1 = 0.035
    CONSTANT2 = 0.029
    SM_IN_M = 100
    MIN_IN_HOUR = 60

    def __init__(self, action: int, duration: float, weight: float,
                 height: int):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        spent_calories = ((self.CONSTANT1 * self.weight
                           + ((self.get_mean_speed() * self.KMH_IN_MSEC)**2
                              / (self.height / self.SM_IN_M)) * self.CONSTANT2
                           * self.weight) * self.duration * self.MIN_IN_HOUR)
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 2
    CALORIES_MEAN_SPEED_SHIFT = 1.1
    LEN_STEP = 1.38
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: float, count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        mean_speed = (self.length_pool * self.count_pool
                      / self.M_IN_KM / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories = ((self.get_mean_speed()
                           + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.CALORIES_MEAN_SPEED_MULTIPLIER
                          * self.weight * self.duration)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    return training_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
