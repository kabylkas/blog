import os
import sys

name = sys.argv[1]

os.system("mkdir -p ./raw/{}".format(name))
os.system("echo '{0}' > ./raw/{0}/{0}.jpg".format(name))
os.system("echo '{0}' > ./raw/{0}/{0}.long".format(name))
os.system("echo '{0}' > ./raw/{0}/{0}.short".format(name))
os.system("echo '{0}' > ./raw/{0}/{0}.title".format(name))
os.system("echo '{0}' > ./raw/{0}/{0}.meta".format(name))
