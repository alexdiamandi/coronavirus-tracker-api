
class Composite(LocationService):


    def init(self):
        self._children: List[Component] = []


    def add(self, LocationService):
        self._children.append(LocationService)
        component.parent = self

    def remove(self, LocationService) -> None:
        self._children.remove(LocationService)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self):
        for child in self._children:
            child.getLocations()