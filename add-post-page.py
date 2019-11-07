import sys
import os
if len(sys.argv) < 3:
  print("Usage: add-post.py [directory with the files] [name: prefix of the files]")
  exit(0)

directory = sys.argv[1]
name = sys.argv[2]


we_have_everything  = os.path.exists("./raw/{}/{}.jpg".format(directory, name))
we_have_everything |= os.path.exists("./raw/{}/{}.short".format(directory, name))
we_have_everything |= os.path.exists("./raw/{}/{}.long".format(directory, name))
we_have_everything |= os.path.exists("./raw/{}/{}.title".format(directory, name))
we_have_everything |= os.path.exists("./raw/{}/{}.meta".format(directory, name))

# TODO: check if post name already exists
if we_have_everything:
  os.system("cp ./raw/{0}/{1}.jpg ./img/portfolio/{1}.jpg".format(directory, name))
  title = ""
  with open("./raw/{}/{}.title".format(directory, name), "r") as title_f:
    for title in title_f:
      title = title.strip()
      break

  with open("post-temp.html", "r") as infile, open("posts/{}.html".format(name), "w") as outfile:
    for html_line in infile:
      if "!!!(((title goes here!@#$" in html_line:
        outfile.write("  <title>{}</title>\n".format(title))
      elif "!!!(((header goes here!@#$" in html_line:
        header_html = '<h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">{}</h2>'.format(title)
        outfile.write("      {}\n".format(header_html))
      elif "!!!(((text goes here!@#$" in html_line:
        with open("./raw/{}/{}.long".format(directory, name), "r") as long_text:
          for long_text_line in long_text:
            outfile.write("{}".format(long_text_line))
      else:
        outfile.write(html_line)

  print("Successfully generated a post page for {}".format(name))
