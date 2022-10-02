import pickle
import json
from abc import ABCMeta, abstractmethod


class SerializationInterface(metaclass=ABCMeta):

    @abstractmethod
    def serialize(self, file_to_write, data_to_write):
        pass

    @abstractmethod
    def deserialize(self, file_to_read):
        pass


class PickleSerialization(SerializationInterface):

    def serialize(self, file_to_write, data_to_write):
        with open(file_to_write, "wb+") as fh:
            pickle.dump(data_to_write, fh)

    def deserialize(self, file_to_read):
        with open(file_to_read, "rb") as fh:
            return pickle.load(fh)


class JsonSerialization(SerializationInterface):

    def serialize(self, file_to_write, data_to_write):
        with open(file_to_write, "w+", encoding="utf-8") as fh:
            json.dump(data_to_write, fh)

    def deserialize(self, file_to_read):
        with open(file_to_read, "r", encoding="utf-8") as fh:
            return json.load(fh)


if __name__ == "__main__":

    # raw data -----------------------------------------------------------------
    test_data_1 = {
        "one": 123,
        "two": "qwerty",
        1: "one",
        2: [1, 2, 3, "one", "two", ["three"]]
        }
    test_data_2 = [1, 2, 3, "one", "two", "three", ["qwerty", (1, 2, 3)]]

    file_pic = PickleSerialization()
    file_jsn = JsonSerialization()

    # Test 1 --------------------------------------------------------------------
    file_pic.serialize(file_to_write="text.pickle", data_to_write=test_data_1)
    file_jsn.serialize(file_to_write="text.json", data_to_write=test_data_1)

    print(f"test_1.0 -> test_data_1: \n {test_data_1}")
    read_pic = file_pic.deserialize(file_to_read="text.pickle")
    print(f"test_1.1 -> read_pic: \n {read_pic}")
    read_jsn = file_jsn.deserialize(file_to_read="text.json")
    print(f"test_1.2 -> read_jsn: \n {read_jsn}")
    print("\n")

    # Test 2 --------------------------------------------------------------------
    file_pic.serialize(file_to_write="text.pickle", data_to_write=test_data_2)
    file_jsn.serialize(file_to_write="text.json", data_to_write=test_data_2)

    print(f"test_2.0 -> test_data_2: \n {test_data_2}")
    read_pic = file_pic.deserialize(file_to_read="text.pickle")
    print(f"test_2.1 -> read_pic: \n {read_pic}")
    read_jsn = file_jsn.deserialize(file_to_read="text.json")
    print(f"test_2.2 -> read_jsn: \n {read_jsn}")

