EMPTY = 0
DUMMY = 1


class SpecialBucket:
    def __init__(self, type: int) -> None:
        self._type = type
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpecialBucket):
            return False
        
        return self._type == other._type
    
    def __str__(self) -> str:
        if self._type == EMPTY:
            return 'EMPTY'
        elif self._type == DUMMY:
            return 'DUMMY'
        
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def type(self) -> int:
        return self._type
