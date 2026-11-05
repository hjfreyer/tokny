#!/usr/bin/env python3
"""Flatten fetched Grants.gov records into one TSV for triage.

Usage: python3 tools/grants_gov_table.py PULLDIR > table.tsv
"""
import csv
import json
import sys
from pathlib import Path


def one(path):
    d = json.load(open(path))["data"]
    s = d.get("synopsis") or d.get("forecast") or {}
    kind = "posted" if d.get("synopsis") else "forecasted"
    types = ";".join(t.get("description", "") for t in s.get("applicantTypes", []))
    cats = ";".join(c.get("description", "") for c in s.get("fundingActivityCategories", []))
    return {
        "id": d["id"],
        "number": d.get("opportunityNumber", ""),
        "status": kind,
        "agency": (d.get("topAgencyDetails") or {}).get("code", ""),
        "subagency": s.get("agencyCode", ""),
        "title": d.get("opportunityTitle", ""),
        "close": s.get("responseDateStr") or s.get("estApplicationResponseDateStr") or "",
        "posted": s.get("postingDateStr") or s.get("estSynopsisPostingDateStr") or "",
        "ceiling": s.get("awardCeiling", ""),
        "floor": s.get("awardFloor", ""),
        "cost_share": s.get("costSharing", ""),
        "n_types": len(s.get("applicantTypes", [])),
        "types": types,
        "categories": cats,
        "elig": (s.get("applicantEligibilityDesc") or "").replace("\n", " ")[:400],
        "desc": (s.get("synopsisDesc") or s.get("forecastDesc") or "").replace("\n", " ")[:400],
        "url": f"https://www.grants.gov/search-results-detail/{d['id']}",
    }


def main():
    rows = [one(p) for p in sorted(Path(sys.argv[1], "opps").glob("*.json"))]
    w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()), delimiter="\t")
    w.writeheader()
    w.writerows(rows)


if __name__ == "__main__":
    main()
