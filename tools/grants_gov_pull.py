#!/usr/bin/env python3
"""Pull every Grants.gov opportunity open to city/township governments.

Usage: python3 tools/grants_gov_pull.py OUTDIR [ELIGIBILITY_CODES]

ELIGIBILITY_CODES is a comma-separated list such as "02" (city or
township governments); "all" (the default) pulls every open and
forecasted opportunity, which is the right choice because most
agencies tag opportunities only as "25 Others (see text)" and the
eligibility text is what has to be read.

Writes OUTDIR/search.json (the search hits) and OUTDIR/opps/<id>.json
(one fetchOpportunity record each). Re-runs skip records already on
disk. Polite: one request at a time with a short pause.
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

API = "https://api.grants.gov/v1/api"
UA = "tokny-grant-harness/0.1 (Town of Kingston NY; polite, serial)"


def post(path, body):
    req = urllib.request.Request(
        f"{API}/{path}", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def search_all(elig):
    hits, start = [], 0
    while True:
        d = post("search2", {
            "rows": 500, "startRecordNum": start,
            "oppStatuses": "forecasted|posted",
            "eligibilities": "" if elig == "all" else elig,
        })["data"]
        hits += d["oppHits"]
        start += 500
        if start >= d["hitCount"]:
            return d["hitCount"], hits
        time.sleep(0.5)


def main():
    out = Path(sys.argv[1])
    elig = sys.argv[2] if len(sys.argv) > 2 else "all"
    (out / "opps").mkdir(parents=True, exist_ok=True)
    total, hits = search_all(elig)
    (out / "search.json").write_text(json.dumps(hits, indent=1))
    print(f"{len(hits)} hits of {total}", flush=True)
    for i, h in enumerate(hits):
        p = out / "opps" / f"{h['id']}.json"
        if p.exists():
            continue
        try:
            rec = post("fetchOpportunity", {"opportunityId": int(h["id"])})
        except Exception as e:  # noqa: BLE001
            print(f"  {h['id']} failed: {e}", flush=True)
            continue
        p.write_text(json.dumps(rec, indent=1))
        if i % 50 == 0:
            print(f"  {i}/{len(hits)}", flush=True)
        time.sleep(0.3)
    print("done")


if __name__ == "__main__":
    main()
