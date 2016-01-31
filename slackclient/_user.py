class User(object):
    def __init__(self, server, name, id, real_name, tz):
        self.tz = tz
        self.name = name
        self.real_name = real_name
        self.server = server
        self.id = id

    def __eq__(self, compare_str):
        if self.id == compare_str or self.name == compare_str:
            return True
        else:
            return False

    def __str__(self):
        data = ""
        for key in list(self.__dict__.keys()):
            if key != "server":
                encoded_key = key.encode('ascii', errors='ignore')
                if self.__dict__[key]:
                    encoded_val = self.__dict__[key].encode('ascii', errors='ignore')
                else:
                    encoded_val = ''
                data += "{} : {}\n".format(encoded_key, encoded_val[:40])
        return data

    def __repr__(self):
        return self.__str__()
