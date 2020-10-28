'''
Description: A useful config reader for yaml and json files.
FilePath: /wired_controller/config.py
Author: qxsoftware@163.com
Date: 2020-10-28 09:53:12
LastEditTime: 2020-10-28 18:52:07
Refer to: https://github.com/QixuanAI
'''

from keyword import iskeyword
from pathlib import Path


class Options:
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        return self.__setattr__(key, value)

    def __setattr__(self, key, value):
        k, v = str(key), value
        assert k.isidentifier(), "Illegal member name: " + k
        assert not iskeyword(k), "Field conflicts with keywords: " + k
        if isinstance(v, dict):
            v = setattrbydict(Options(), v)
        return super.__setattr__(self, k, v)

    def __repr__(self):
        return str(self.__dict__)


class Config(Options):
    def __init__(self, cfgfile):
        path = Path(cfgfile)
        if path.suffix == ".yaml":
            from yaml import load
        elif path.suffix == ".json":
            from json import load
        else:
            raise NotImplementedError("Unrecognized config file type.")
        cfg_dict = load(path.read_text())
        setattrbydict(self, cfg_dict)


def setattrbydict(obj, dic):
    for k, v in dic.items():
        if isinstance(v, dict):
            v = setattrbydict(Options(), v)
        setattr(obj, k, v)
    return obj


if __name__ == "__main__":
    # Here is some examples to show the useful features of class Config.
    cfg = Config('config/visca.yaml')
    # Basicly, you can visit or add members by indexing.
    # The Config will make key:value as attributes.
    cfg['p'] = {'a1': 111, 'a2': 222}
    # But the key should satisfied python name rule, like do not start with numbers.
    # cfg['p'] = {'1a': 111, '2b': 222} # attr can't start with numbers.
    # More specifically, you can also visit or add members by dot reference.
    print(cfg.p)  # visit members as a attribute.
    # the child members have the same features.
    cfg.p.a1 = {'b1': 11111, 'b2': 22222}
    print(cfg.p.a1.b2 is cfg.p['a1'].b2)  # -> True
    print(cfg)  # the Config can easily represent as a dictionary string.
