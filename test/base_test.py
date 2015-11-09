from ceph_commands import base

def TestBase():
    cmd = base.CommandExecutor()
    print cmd.executeCmd('echo hello')
