class Meta(type):

    children_number = 0

    def __new__(mcs, name, parents, attrs):
        attrs["class_number"] = Meta.children_number
        Meta.children_number += 1
        return super().__new__(mcs, name, parents, attrs)

    @classmethod
    def __prepare__(mcs, name, parents, **kwargs):
        return super().__prepare__(name, parents, **kwargs)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


Meta.children_number = 10


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == "__main__":
    print("Cls1.class_number = ", Cls1.class_number)
    print("Cls2.class_number = ", Cls2.class_number)
    assert (Cls1.class_number, Cls2.class_number) == (10, 11)

    a, b = Cls1(''), Cls2('')
    print("a.class_number = ", a.class_number)
    print("b.class_number = ", b.class_number)
    assert (a.class_number, b.class_number) == (0, 1)

