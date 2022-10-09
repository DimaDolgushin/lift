import logging


class Exceptions:
    class RestoreElevatorError(Exception):
        def __init__(self, text):
            self.text = text

    class NumberFloorError(Exception):
        def __init__(self, text):
            self.text = text

    class WeigthCapacityError(Exception):
        def __init__(self, text):
            self.text = text


class Elevator:
    def __init__(self, floors_count, elevator_capacity):
        self.elevator_broken = False
        self.num_break = 0
        self.unit = []
        self.floors_count = floors_count
        self.elevator_capacity = elevator_capacity
        self.weigth = 0
        self.exit_floor = 0
        self.unit_location = 0
        self.waiting_units = []
        self.waiting_count_units = 0
        self.units = []
        self.weigth_units = 0
        self.count_units = 0
        self.elevator_location = 1

    def move(self, number_floor):
        if not self.elevator_broken:
            if self.weigth_units <= self.elevator_capacity:
                if number_floor <= self.floors_count:
                    self.elevator_location = number_floor
                else:
                    logging.critical("A message of CRITICAL severity")
                    raise Exceptions.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
            else:
                logging.warning("A WARNING")
                raise Exceptions.WeigthCapacityError("Вес выше допустимого")
        else:
            raise Exceptions.RestoreElevatorError("Не удалось восстановить лифт, "
                                                  "приносим свои извинения. Спасатели уже вызваны!")

    def add_waiting_unit(self, unit: list):
        if not self.elevator_broken:
            if self.unit_location <= self.floors_count:
                self.unit = unit
                self.exit_floor = unit[0]  # Этаж на котором пассажир выйдет
                self.weigth = unit[1]  # Вес багажа и его пассажира
                self.unit_location = unit[2]  # местоположение ожидающего пассажира
                self.waiting_count_units += 1
                self.waiting_units.append(unit)
                print(f"Человек вызвал лифт!\n")
                print(f"Этаж на котором человек ожидает лифт: {self.unit_location}\nЭтаж на котором человек выйдет: "
                      f"{self.exit_floor}\nВес пассажира и его багажа, если он есть: {self.weigth}кг\n")
            else:
                logging.critical("A message of CRITICAL severity")
                raise Exceptions.NumberFloorError("Указанный этаж находится вне диапазона этажей этого дома")
        else:
            raise Exceptions.RestoreElevatorError("Не удалось восстановить лифт, "
                                                  "приносим свои извинения. Спасатели уже вызваны!")

    def delete_waiting_unit(self, i=0):
        if not self.elevator_broken:
            while i < self.waiting_count_units:
                if self.elevator_location == self.waiting_units[i][2]:  # сравнение местоположения лифта с
                    # местоположением ожидающего пассажира
                    self.waiting_count_units -= 1
                    self.waiting_units.pop(i)
                    print("Очередь уменьшилась на 1\n")
                i += 1
        else:
            raise Exceptions.RestoreElevatorError("Не удалось восстановить лифт, "
                                                  "приносим свои извинения. Спасатели уже вызваны!")

    def add_units(self, i=0):
        if not self.elevator_broken:
            while i < self.waiting_count_units:
                if self.elevator_location == self.waiting_units[i][2]:
                    self.weigth_units += self.waiting_units[i][1]
                    self.count_units += 1
                    self.units.append(self.waiting_units[i])
                    print("Человек зашел!\n")
                i += 1
        else:
            raise Exceptions.RestoreElevatorError("Не удалось восстановить лифт, "
                                                  "приносим свои извинения. Спасатели уже вызваны!")

    def delete_unit(self, i=0):
        if not self.elevator_broken:
            while i < self.count_units:
                if self.elevator_location == self.units[i][0]:
                    self.count_units -= 1
                    self.weigth_units -= self.units[i][1]
                    self.units.pop(i)
                    print("Человек вышел!\n")
                i += 1
        else:
            raise Exceptions.RestoreElevatorError("Не удалось восстановить лифт, "
                                                  "приносим свои извинения. Спасатели уже вызваны!")

    def to_ride(self, number_floor, i=0):
        self.move(number_floor)
        print(f'Мы прибыли на {number_floor} этаж\n')
        self.add_units()
        try:
            while i < self.count_units + 100:
                self.delete_waiting_unit()
                self.delete_unit()
                i += 1
        except:
            pass
        return number_floor

    def check_elevator_condition(self):
        print("Состояние лифта:\n")
        print(f"Этаж на котором находится лифт: {self.elevator_location}\nОбщий вес лифта: {self.weigth_units}\n"
              f"Количество пассажиров в ожидает: {self.waiting_count_units}\nКоличество пассажиров в "
              f"лифте: {self.count_units}\n")


class Human:

    @staticmethod
    def call_elevator():
        return True


elev = Elevator(10, 1200)
hum = Human()

elev.to_ride(5)
elev.add_waiting_unit([4, 56, 9])
elev.to_ride(9)
elev.to_ride(4)


