import copy


class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.iterable_copy = list(iterable)
        self.generated = 0
        self.fail_count = 0
        try:
            self.first_elem = next(copy.deepcopy(self.iterable))
        except StopIteration:
            self.first_elem = AttributeError('Исходный итерируемый объект пуст')
        self.last_elem = AttributeError('Последнего элемента нет')
        self.is_empty_ = False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current_elem = next(self.iterable)
            if self.iterable_copy:
                self.iterable_copy.pop(0)
            if not (self.iterable_copy):
                self.is_empty_ = True
            self.generated += 1
            self.last_elem = current_elem
            return current_elem
        except StopIteration:
            self.fail_count += 1
            raise StopIteration

    @property
    def accesses(self):
        return self.generated

    @property
    def empty_accesses(self):
        return self.fail_count

    @property
    def first(self):
        return self.first_elem

    @property
    def last(self):
        return self.last_elem

    def is_empty(self):
        return self.is_empty_

