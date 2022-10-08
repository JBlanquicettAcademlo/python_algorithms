from abc import abstractmethod

class BaseDictionary(dict):
    
    @abstractmethod
    def __setitem__(self, key, item) -> None:
        raise NotImplementedError
    
    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)
    
    def __len__(self):
        return len(self.__dict__)
    
    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, key):
        return key in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)
    
    def keys(self):
        return self.__dict__.keys()
    
    def values(self):
        return self.__dict__.values()

    def items(self, key):
        return self.__dict__.items()
    
    def pop(self, *args):
        return self.__dict__.pop(*args)


class User:

    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    
    def __str__(self) -> str:
        return f'User: {self.fname} {self.fname}'


class UserDictionary(BaseDictionary):
    
    def __setitem__(self, key, item:User) -> None:

        if not isinstance(item, User):
            raise Exception('Value is not user model')
        self.__dict__[key] = item


user_dict = UserDictionary()

user = User('Jorge', 'Blanquicett')

#user_dict.__setitem__('1123', user)

user_dict.__setitem__('1123', user)

#print(user_dict['1123'])
