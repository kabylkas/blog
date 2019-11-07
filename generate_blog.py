import os


def write_item(f, name):
  short = ""
  with open("./raw/{0}/{0}.short".format(name), "r") as infile:
    for line in infile:
      short = line.strip()
      break

  f.write('        <!-- post item {} -->\n'.format(name))
  f.write('        <div class="col-md-6 col-lg-4">\n')
  f.write('          <a style="color: white;" href="./posts/{}.html">'.format(name))
  f.write('          <div class="portfolio-item mx-auto">\n'.format(name))
  f.write('            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">\n')
  f.write('              <div class="portfolio-item-caption-content text-center text-white">\n')
  f.write('                 {}\n'.format(short))
  f.write('              </div>\n')
  f.write('            </div></a>\n')
  f.write('            <img class="img-fluid" src="img/portfolio/{}.jpg" alt="">\n'.format(name))
  f.write('          </div>\n')
  f.write('        </div>\n')
  f.write('\n')

os.system("rm -rf posts")
os.system("mkdir posts")

names = os.listdir("./raw")

for name in names:
  os.system("python add-post-page.py {0} {0}".format(name))

with open("index-temp.html", "r") as infile, open("index.html", "w") as outfile:
  for line in infile:
    if "!!!(((items go here!@#$" in line:
      for name in names:
        write_item(outfile, name)
    else:
      outfile.write(line)
