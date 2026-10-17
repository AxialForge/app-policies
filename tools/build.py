#!/usr/bin/env python3
"""Build the static site from apps/<slug>/ sources.

apps/<slug>/app.json   name, tagline, type, source (optional)
apps/<slug>/privacy.md -> /<slug>/            (the store-facing privacy policy URL)
apps/<slug>/<page>.md  -> /<slug>/<page>/     (e.g. delete-account.md, terms.md)

Run:  python3 tools/build.py      (needs: pip install markdown)
Output HTML is committed; GitHub Pages serves the repo root. Never rename a
published slug or page: store listings point at these URLs.
"""
import html, json, pathlib, re, shutil, sys
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
APPS = ROOT / "apps"

def page(title, body, depth, crumb=""):
    css = "../" * depth + "assets/style.css"
    home = "../" * depth or "./"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{css}">
</head>
<body>
{crumb}{body}
<footer><a href="{home}">All app policies</a></footer>
</body>
</html>
'''

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")

def main():
    apps = []
    for d in sorted(p for p in APPS.iterdir() if p.is_dir() and not p.name.startswith("_")):
        meta = json.loads((d / "app.json").read_text(encoding="utf-8"))
        slug = d.name
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
            sys.exit(f"bad slug: {slug}")
        out = ROOT / slug
        if out.exists():
            shutil.rmtree(out)
        extras = []
        for md in sorted(d.glob("*.md")):
            text = md.read_text(encoding="utf-8")
            body = markdown.markdown(text, extensions=["tables"])
            m = re.search(r"^#\s+(.+)$", text, re.M)
            title = m.group(1).strip() if m else f"{meta['name']} {md.stem}"
            if md.stem == "privacy":
                write(out / "index.html", page(title, body, 1))
            else:
                crumb = f'<nav class="crumbs"><a href="../">{html.escape(meta["name"])}</a></nav>'
                write(out / md.stem / "index.html", page(title, body, 2, crumb))
                extras.append((md.stem, title))
        apps.append((slug, meta, extras))

    sitepages = []
    for md in sorted((ROOT / "site").glob("*.md")):
        text = md.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.M)
        title = m.group(1).strip() if m else md.stem.title()
        out = ROOT / md.stem
        if out.exists():
            shutil.rmtree(out)
        write(out / "index.html", page(title, markdown.markdown(text, extensions=["tables"]), 1))
        sitepages.append((md.stem, title))

    rows = []
    for slug, meta, extras in apps:
        more = "".join(f' &middot; <a href="{slug}/{s}/">{html.escape(t)}</a>' for s, t in extras)
        rows.append(f'<li><strong>{html.escape(meta["name"])}</strong> &mdash; {html.escape(meta.get("tagline",""))} '
                    f'<br><a href="{slug}/">Privacy policy</a>{more}</li>')
    body = "<h1>App Policies</h1>\n<p>Privacy policies and related pages for apps and software published by this developer.</p>\n<ul>\n" + "\n".join(rows) + "\n</ul>\n<p>" + " &middot; ".join(f'<a href="{s}/">{html.escape(t)}</a>' for s, t in sitepages) + "</p>"
    write(ROOT / "index.html", page("App Policies", body, 0))
    print(f"built {len(apps)} app(s)")

if __name__ == "__main__":
    main()

