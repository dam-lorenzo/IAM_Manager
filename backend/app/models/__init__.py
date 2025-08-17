
class BaseModel:

    def to_dict(self):
        ret_dict = dict()
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                ret_dict[key] = value
        return ret_dict