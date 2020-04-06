class Vars(dict):
    def __init__(self, _vars={}):
        self.edit_vars = _vars


    def has_var(self, var) -> bool:
        return var in self.edit_vars.keys()