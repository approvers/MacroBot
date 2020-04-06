class WriteFlagHolder:
    def __init__(self, flag=False):
        self.write_flag = flag

    def is_true(self):
        return self.write_flag
    def is_false(self):
        return not self.write_flag

    def get_flag(self):
        return self.write_flag
    
    def set_flag(self, flag:bool):
        self.write_flag = flag