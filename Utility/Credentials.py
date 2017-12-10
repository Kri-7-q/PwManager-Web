from os.path import expanduser

class Credentials:

    def __init__(self):
        self.databasename = None
        self.hostname = None
        self.port = None
        self.username = None
        self.password = None
        self.tablename = None

    @staticmethod
    def fromFile(path):
        val = dict()
        with open(path, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                separator = line.find(':')
                key = line[:separator]
                value = line[separator+1:]
                val[key] = value
        c = Credentials()
        c.__dict__.update(val)

        return c

    # 'postgresql://christian:kri-7-q@localhost:3306/pwmanager'
    def connectionStringDB(self, database='postgresql'):
        string = '{database}://{username}:{password}@{hostname}:{port}/{databasename}'
        val = self.__dict__
        val['database'] = database

        return string.format_map(val)

    def tableName(self):
        return self.tablename

    def port(self):
        return self.port

    def hostname(self):
        return self.hostname

    def databaseName(self):
        return self.databasename

    def username(self):
        return self.username

    @staticmethod
    def userHomePath():
        return expanduser('~')
