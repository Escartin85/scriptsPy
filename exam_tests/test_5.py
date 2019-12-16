class ReadFirstLine:
    # Which lines will be executed if the open() function throws an exeption?
    @staticmethod
    def read_first_line(path):
        f = None
        first_line = None
        try:
            f = open(path)
            first_line = f.readline()
        except IOError as e:
            print('Error reading from "' + path + '". Message = "' + e.message + '"')
        finally:
            if f is not None:
                try:
                    f.close()
                except:
                    pass

        return first_line

# testing
ReadFirstLine.read_first_line("scoresa.txt")

# Answer (13)
