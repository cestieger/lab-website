"""One-off helper: fetch TOC/graphical-abstract images via Europe PMC for every DOI in _data/citations.yaml.

Saves images/toc/<slug>-<kind>.<ext> and writes images/toc/report.txt.
"""
import os, re, sys, yaml
import requests

S = requests.Session()
S.headers.update({"User-Agent": "lab-website-toc-fetcher/1.0"})
out = "images/toc"
os.makedirs(out, exist_ok=True)
report = []
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"

def slug(doi):
    return re.sub(r"[^a-z0-9]+", "-", doi.lower()).strip("-")

def download(pmcid, href, fn_base):
    tried = []
    hosts = ["https://europepmc.org/articles/{p}/bin/{h}",
             "https://pmc-oa-opendata.s3.amazonaws.com/{p}.1/{h}",
             "https://pmc-oa-opendata.s3.amazonaws.com/{p}.2/{h}",
             "https://www.ncbi.nlm.nih.gov/pmc/articles/{p}/bin/{h}"]
    for host in hosts:
        u = host.format(p=pmcid, h=href)
        try:
            r = S.get(u, timeout=30, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"})
            ct = r.headers.get("content-type", "")
            tried.append(f"{r.status_code}:{ct.split(';')[0]}:{u.split('/')[2]}")
            if r.status_code == 200 and ct.startswith("image"):
                ext = href.rsplit(".", 1)[-1] if "." in href else "jpg"
                fn = f"{fn_base}.{ext}"
                open(fn, "wb").write(r.content)
                return fn, u
        except Exception as e:
            tried.append(f"err:{u.split('/')[2]}")
    return None, " ".join(tried)

for cit in yaml.safe_load(open("_data/citations.yaml")):
    _id = cit.get("id", "")
    if not _id.lower().startswith("doi:"):
        continue
    doi = _id[4:]
    try:
        q = S.get(f"{EPMC}/search", params={"query": f'DOI:"{doi}"', "format": "json", "resultType": "lite"}, timeout=30).json()
        res = q.get("resultList", {}).get("result", [])
        pmcid = next((x.get("pmcid") for x in res if x.get("pmcid")), None)
        if not pmcid:
            report.append(f"{_id}\tno PMC id"); continue
        xr = S.get(f"{EPMC}/{pmcid}/fullTextXML", timeout=60)
        if xr.status_code != 200:
            report.append(f"{_id}\t{pmcid}\tno full text ({xr.status_code})"); continue
        x = xr.text
        hrefs = []
        for m in re.finditer(r'<abstract[^>]*abstract-type="(?:graphical|toc|teaser)"[^>]*>(.*?)</abstract>', x, re.S | re.I):
            hrefs += [("toc", h) for h in re.findall(r'xlink:href="([^"]+)"', m.group(1))]
        if not hrefs:
            # Wiley-style: graphic inside the abstract block, or a figure labelled TOC/graphical abstract
            for m in re.finditer(r'<(?:fig|graphic)[^>]*>(?:(?!</fig>).){0,600}?(?:TOC|Graphical Abstract|Table of Contents)', x, re.S | re.I):
                hrefs += [("toc", h) for h in re.findall(r'xlink:href="([^"]+)"', m.group(0))[:1]]
        first_fig = re.search(r'<fig[^>]*>.*?xlink:href="([^"]+)"', x, re.S)
        if first_fig:
            hrefs.append(("fig1", first_fig.group(1)))
        if not hrefs:
            report.append(f"{_id}\t{pmcid}\tno graphics"); continue
        done = set()
        for kind, h in hrefs:
            if kind in done: continue
            fn, u = download(pmcid, h, f"{out}/{slug(doi)}-{kind}")
            report.append(f"{_id}\t{pmcid}\t{kind}\t{'saved ' + fn if fn else 'failed ' + u}\t{h}")
            if fn: done.add(kind)
    except Exception as e:
        report.append(f"{_id}\terror {e}")

open(f"{out}/report.txt", "w").write("\n".join(report) + "\n")
print("\n".join(report))
