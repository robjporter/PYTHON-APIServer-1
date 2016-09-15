class DottedDict(dict):

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError("'{}'".format(attr))

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__