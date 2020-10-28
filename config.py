'''
Description: A useful config reader for yaml and json files.
FilePath: /wired_controller/config.py
Author: qxsoftware@163.com
Date: 2020-10-28 09:53:12
LastEditTime: 2020-10-28 14:49:44
Refer to: https://github.com/QixuanAI
'''

from keyword import iskeyword
from pathlib import Path


class Config(object):
    class Options:
        def __setattr__(self, key, value):
            k, v = str(key), value
            assert k.isidentifier(), "Illegal member name: " + k
            assert not iskeyword(k), "Field conflicts with keywords: " + k
            if isinstance(v, dict):
                v = Config.setattrbydict(Config.Options(), v)
            return super.__setattr__(self, k, v)

        def __repr__(self):
            return str(self.__dict__)

    def __init__(self, cfgfile):
        path = Path(cfgfile)
        if path.suffix == ".yaml":
            from yaml import load
        elif path.suffix == ".json":
            from json import load
        else:
            raise NotImplementedError("Unrecognized config file type.")
        cfg_dict = load(path.read_text())
        Config.setattrbydict(self, cfg_dict)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        return self.__setattr__(key, value)

    def __setattr__(self, key, value):
        k, v = str(key), value
        assert k.isidentifier(), "Illegal member name: " + k
        assert not iskeyword(k), "Field conflicts with keywords: " + k
        if isinstance(v, dict):
            v = Config.setattrbydict(Config.Options(), v)
        return super.__setattr__(self, k, v)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def setattrbydict(obj, dic):
        for k, v in dic.items():
            if isinstance(v, dict):
                v = Config.setattrbydict(Config.Options(), v)
            setattr(obj, k, v)
        return obj


if __name__ == "__main__":
    cfg = Config('config/visca.yaml')
    print(cfg)
