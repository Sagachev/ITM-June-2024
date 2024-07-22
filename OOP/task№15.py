# Напишите класс, содержит 3 любые атрибута и при изменении логгировать всё в консоль (при изменении старое->новое)
class LoggedAttributes:
    def __init__(self, attr1, attr2, attr3):
        self._attr1 = attr1
        self._attr2 = attr2
        self._attr3 = attr3

    @property
    def attr1(self):
        return self._attr1

    @attr1.setter
    def attr1(self, value):
        self._log_change('attr1', self._attr1, value)
        self._attr1 = value

    @property
    def attr2(self):
        return self._attr2

    @attr2.setter
    def attr2(self, value):
        self._log_change('attr2', self._attr2, value)
        self._attr2 = value

    @property
    def attr3(self):
        return self._attr3

    @attr3.setter
    def attr3(self, value):
        self._log_change('attr3', self._attr3, value)
        self._attr3 = value

    def _log_change(self, attribute, old_value, new_value):
        print(f"Изменение {attribute}: {old_value} -> {new_value}")



car = LoggedAttributes('red', 'Toyota', 4)
car.attr1 = 'violet'
car.attr2 = 'Nissan'
car.attr3 = 5