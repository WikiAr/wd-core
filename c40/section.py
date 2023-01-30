import pywikibot
import re

site = pywikibot.Site("en", "wikiversity")


def addsection(title, summary, text):
    page = pywikibot.Page(site, title)
    result = pywikibot.site.APISite.editpage(
        site,
        page=page,
        summary=summary, minor=False,
        text=text, section="new"
    )
    return result


def allimages(start="!", prefix="", reverse=False, step=None, total=None, content=False):
    pages = pywikibot.site.APISite.allimages(
        site,
        start=start,
        prefix=prefix,
        reverse=reverse,
        step=step,
        total=total,
        content=content
    )
    return pages


def allpages(prefix="", namespace=0, filterredir=None, content=False):
    pages = pywikibot.site.APISite.allpages(
        site,
        prefix=prefix,
        namespace=namespace,
        filterredir=filterredir,
        content=content
    )
    return pages


def allredirects(prefix="", namespace=0):
    return allpages(
        prefix=prefix,
        namespace=namespace,
        filterredir=True
    )


def categorymembers(category):
    category = pywikibot.Category(site, category)
    pages = pywikibot.site.APISite.categorymembers(
        site,
        category=category
    )
    return pages


def editpage(title, summary, text, minor=True):
    page = pywikibot.Page(site, title)
    page.text = text
    result = pywikibot.site.APISite.editpage(
        site,
        page=page,
        summary=summary, minor=minor
    )
    return result


def embeddedin(title, filterRedirects=None, namespaces=None, step=None, total=None, content=False):
    page = pywikibot.Page(site, title)
    pages = pywikibot.site.APISite.page_embeddedin(
        site,
        page=page,
        filterRedirects = filterRedirects,
        namespaces = namespaces,
        step = step,
        total = total,
        content = content
    )
    return pages


def extlinks(title):
    page = pywikibot.Page(site, title)
    links = pywikibot.site.APISite.page_extlinks(
        site,
        page=page
    )
    return links


def logevents(title):
    page = pywikibot.Page(site, title)
    links = pywikibot.site.APISite.page_extlinks(
        site,
        page=page
    )
    return links


def movepage(title, newtitle, summary, noredirect=False):
    page = pywikibot.Page(site, title)
    page = pywikibot.site.APISite.movepage(
        site,
        page=page,
        newtitle=newtitle,
        summary=summary,
        noredirect=noredirect
    )
    return page


def newfiles(user=None, start=None, end=None, reverse=False, step=None, total=None):
    files = pywikibot.site.APISite.newfiles(
        site,
        start=start,
        end=end,
        reverse=reverse,
        step=step,
        total=total
    )
    return files


def pagebacklinks(title):
    page = pywikibot.Page(site, title)
    pages = pywikibot.site.APISite.pagebacklinks(
        site,
        page=page
    )
    return pages


def pagelinks(title):
    page = pywikibot.Page(site, title)
    pages = pywikibot.site.APISite.pagelinks(
        site,
        page=page
    )
    return pages


def get_allpages():
    start = "!"
    while (True):
        try:
            pages = allimages(start=start, total=10, content=True)
            for page in pages:
                print(page.title())
                print(page.text)
            start = page.title()
            start = start[5:] + "!"
            break
        except:
            break

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %s" % (attr, getattr(obj, attr)))


def files_missing_license(start, end):
    tags = [
        "{{information",
        "{{pd",
        "{{cc-by",
        "{{gfdl",
        "{{self",
        "{{bsd",
        "{{gpl",
        "{{lgpl",
        "{{free",
        "{{copyright",
        "{{fairuse",
        "{{non-free",
        "{{software",
        "{{no license",
        "{{no fairuse"
    ]

    files = newfiles(
        start=start,
        end=end,
        reverse=True)

    result = list()

    for file in files:
        text = file[0].text.lower()
        if not (any(word in text for word in tags)):
            result.append(file)

    return result

def filekey(file):
    return file[2] + file[0].title()

def add_missing_license_information(start, end):
    usermsg = (
        "Thank you for uploading files to Wikiversity. See [[Wikiversity:Media]] for copyright and license requirements "
        "for Wikiversity files. All files must have copyright and/or license information added to the file.\n\n"
        "Instructions for adding copyright and/or license information are available at [[Wikiversity:License tags]]. "
        "Files must be updated within seven days or they may be removed without further notice.\n\n"
        "The following files are missing copyright and/or license information:\n"
    )
    summary = "Missing License Information"

    files = files_missing_license(start, end)
    files = sorted(files, key=filekey)
    user = ""
    print("== Files Missing License Information ==")
    for file in files:
        if user != file[2]:
            if user != "":
                title = "User_talk:" + user
                text += "\n~~~~\n"
                addsection(title, summary, text)
            user = file[2]
            text = usermsg
            print(";[[User_talk:" + user + "]]")
        title = file[0].title()
        text += "* [[:" + title + "]]\n"
        print(":[[:" + title + "]]")
        addsection(title, summary, "{{subst:nld}}")
    if user != "":
        title = "User_talk:" + user
        text += "\n~~~~\n"
        addsection(title, summary, text)


def show_sister_backlinks(wiki, language="en"):
    global site

    site = pywikibot.Site(language, wiki.lower())
    pages = embeddedin(title = "Template:Wikiversity", namespaces = 0, content = True)
    pages = sorted(pages)
    for page in pages:
        title = page.title()
        regex = re.compile("{{wikiversity[^}]*}}", re.IGNORECASE)
        match = regex.search(page.text)
        if(match == None):
            continue

        text = match.group()
        if(text.lower() == "{{wikiversity}}"):
            print("* [[" + wiki + ":" + title + "]] -> [[" + title + "]]")
            continue

        match = re.search("\|[^|}]*[|}]", text)
        if(match != None):
            text = match.group()
            text.replace("at=", "")
            print("* [[" + wiki + ":" + title + "]] -> [[" + text[1:-1] + "]]")
            continue

        print(title + " -> " + text)