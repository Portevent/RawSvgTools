class UuidProvider:

    _uuid: int = 0

    @staticmethod
    def get() -> int:
        UuidProvider._uuid += 1
        return UuidProvider._uuid
