from ceph_commands import rbd

def TestOSD():
    cmd = rbd.rbd()
    print cmd.execute('ls',**{"pool":"rbd"})
    print cmd("showmapped")
