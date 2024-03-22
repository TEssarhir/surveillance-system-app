import rpyc

conn = rpyc.connect("localhost",18861)
conn.root.f()