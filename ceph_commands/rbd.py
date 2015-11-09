#!/usr/env/bin python
#! -*- coding: utf-8 -*-

from . import base

class rbd(base.CommandExecutor):
    def __init__(self):
        self.prefix = "rbd "
        self.cmdmap = {"ls":"ls --format json",
                       "showmapped":"showmapped --format json",
                       }


    def generate(self, cmdname, **para):
        if cmdname == "setpoolattr":
            if 'pool' in para and 'attr' in para and 'value' in para:
                return True, self.prefix + self.cmdmap[cmdname] % (para['pool'], para['attr'], para['value'])
            else:
                return False, "need 'pool' or 'attr' in parameters"
        elif cmdname == "getpoolattr":
            if 'pool' in para and 'attr' in para:
                return True, self.prefix + self.cmdmap[cmdname] % (para['pool'], para['attr'])
            else:
                return False, "need 'pool' or 'attr' in parameters"
        else:
            return True, self.prefix + self.cmdmap[cmdname]

    def execute(self, cmdname, **para):
        isSuccess, result = self.generate(cmdname, **para)
        if isSuccess:
            return True, self.executeCmd(result)
        else:
            return False, result
       
    def __call__(self, cmdname, **para):
        return self.execute(cmdname, **para)

