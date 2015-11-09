from ceph_commands import ceph

def TestOSD():
    cmd = ceph.ceph()
    print cmd.execute('osddf')
    print cmd.execute('osdgetmaxosd')
    print cmd.execute('osdtree')
    print cmd("osddump")
    print cmd("osdperf")
    print cmd("getpoolattr", **{'pool':'rbd', 'attr':'min_size'})
    print cmd("poolstats")
    print cmd("df")
    print cmd("pgdump")
    print cmd("pgstat")
    print cmd("monstatus")
    print cmd("getquota", **{'pool':'rbd'})
    print cmd("authlist")
