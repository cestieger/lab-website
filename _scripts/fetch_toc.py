"""One-off helper: download candidate TOC/abstract graphics for every DOI in _data/citations.yaml.

Saves candidates to images/toc/<slug>-<n>.<ext> and writes images/toc/report.txt.
"""
import os, re, sys, yaml, html
from urllib.parse import urljoin
import requests

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
S = requests.Session()
S.headers.update({"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*",
                  "Accept-Language": "en-US,en;q=0.9"})

out = "images/toc"
os.makedirs(out, exist_ok=True)
report = []

def slug(doi):
    return re.sub(r"[^a-z0-9]+", "-", doi.lower()).strip("-")

def candidates(page, base):
    c = []
    for pat in [r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"',
                r'<meta[^>]+content="([^"]+)"[^>]+property="og:image"',
                r'<meta[^>]+name="twitter:image"[^>]+content="([^"]+)"']:
        c += re.findall(pat, page, re.I)
    # ACS abstract image, Wiley/RSC graphical abstract, generic toc images
    for m in re.finditer(r'<img[^>]+(?:src|data-src)="([^"]+)"[^>]*>', page, re.I):
        tag, src = m.group(0), m.group(1)
        ctx = page[max(0, m.start() - 600):m.start()].lower()
        if re.search(r"abstract-img|graphical[ -_]?abstract|toc[-_ ]?graphic|article_abstract|/medium/|gabs|abstract-graphic", tag.lower() + ctx[-300:]):
            c.append(src)
    seen, res = set(), []
    for u in c:
        u = urljoin(base, html.unescape(u))
        if u not in seen and not u.endswith(".svg"):
            seen.add(u); res.append(u)
    return res[:4]

cits = yaml.safe_load(open("_data/citations.yaml"))
for cit in cits:
    _id = cit.get("id", "")
    if not _id.lower().startswith("doi:"):
        continue
    doi = _id[4:]
    try:
        r = S.get(f"https://doi.org/{doi}", timeout=30, allow_redirects=True)
        report.append(f"{_id}\t{r.status_code}\t{r.url}")
        if r.status_code != 200:
            continue
        for n, u in enumerate(candidates(r.text, r.url), 1):
            try:
                ir = S.get(u, timeout=30, headers={"Referer": r.url})
                ct = ir.headers.get("content-type", "")
                if ir.status_code == 200 and ct.startswith("image"):
                    ext = {"image/jpeg": "jpg", "image/png": "png", "image/gif": "gif",
                           "image/webp": "webp"}.get(ct.split(";")[0], "img")
                    fn = f"{out}/{slug(doi)}-{n}.{ext}"
                    open(fn, "wb").write(ir.content)
                    report.append(f"  saved {fn}\t{len(ir.content)}\t{u}")
                else:
                    report.append(f"  fail {ir.status_code} {ct}\t{u}")
            except Exception as e:
                report.append(f"  error {e}\t{u}")
    except Exception as e:
        report.append(f"{_id}\terror {e}")

open(f"{out}/report.txt", "w").write("\n".join(report) + "\n")
print("\n".join(report))
