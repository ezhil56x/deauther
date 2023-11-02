class Argument:
    def __init__(self):
        self.option = []
        self.optionValues = {}

    def parse_args(self, args):
        for arg in args:
            if arg.startswith('--'):
                if '=' in arg:
                    self.option.append(arg.split('=')[0])
                    self.optionValues[arg.split('=')[0]] = arg.split('=')[1]
                else:
                    self.option.append(arg)
            