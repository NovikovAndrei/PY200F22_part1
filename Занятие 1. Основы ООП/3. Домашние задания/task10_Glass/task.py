# TODO написать класс Glass согласно условию
class Glass:
    def __init__(self, material: str):
        self.material = None
        self.init_material(material)

    def init_material(self, material: str):
        if not isinstance(material, str):
            raise TypeError("material олжен быть str")
        self.material = material

    def get_material(self) -> str:
        return self.material


if __name__ == "__main__":
    glass = Glass('crystal')

    print(glass.get_material())
