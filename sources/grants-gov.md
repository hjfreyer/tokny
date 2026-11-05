---
name: Grants.gov
url: https://www.grants.gov
level: federal
poll: weekly
last_checked: 2026-11-03
---

The single federal catalog. All 26 grant-making agencies post discretionary
opportunities here. On the order of 1,200 posted and 500 forecasted at any
time, of which a small fraction are open to local governments and a smaller
fraction still make sense for a town of ~900 people.

## How to search

Web: https://www.grants.gov/search-grants

API — confirmed against the official guide (https://grants.gov/api/api-guide)
and exercised 2026-11-05: no key or auth needed for `search2` or
`fetchOpportunity`.

`tools/grants_gov_pull.py OUTDIR [codes|all]` pulls every open and
forecasted record (one `fetchOpportunity` per hit, politely serial,
~8 minutes for the full catalog); `tools/grants_gov_table.py OUTDIR`
flattens them to a TSV. A dated snapshot lives in `data/grants-gov/`.

Eligibility codes (from the `search2` facet, 2026-11-05):
`00` State, `01` County, `02` **City or township**, `04` Special
district, `05` School district, `06`/`20` public/private higher ed,
`07`/`11` tribal, `08` housing authorities, `12`/`13` nonprofits,
`21` individuals, `22`/`23` for-profit/small business, `25` **Others
(see text)**, `99` Unrestricted.

**Don't filter on `02`.** Most agencies tag only `25 Others` and put
the real eligibility in `applicantEligibilityDesc` (EPA Brownfields is
tagged that way). Pull everything and read the text.

### What the catalog looks like (2026-11-05)

1,456 open + forecasted (867 posted, 589 forecasted). By top agency:
HHS 921, NSF 118, DoD 90, State 82, Interior 51, DOJ 32, Commerce 25,
USDA 21, NASA 19, HUD 16, DOE 14, IMLS 13, DOT 11, **EPA 9**, others
<10 each. After dropping research agencies, NIH, and titles with
research/clinical/fellowship words, and keeping anything tagged `02`
or whose text mentions local governments/municipalities/towns/rural:
182 — of which 108 are HHS health-system programs for states and
providers. The non-HHS remainder (74) contained exactly one thing
not already filed: the FY2026 Flood Mitigation Assistance NOFO
(DHS-26-MT-029-000-98, due 2027-02-26), now recorded in
`2027-fema-flood-mitigation-assistance`.

So the lesson from the first full pull: the federal catalog at any
moment holds a handful of programs for a town this size, all of them
annual and already known. The value of polling is catching the
*posting date* of those known programs (FMA, Brownfields, SS4A, AFG,
Community Connect) — not discovering new ones. A weekly diff against
`data/grants-gov/` on title + number is enough.

## Narrowing

Most federal opportunities open to "townships" are really aimed at cities
or counties. Signals that one is actually plausible for Kingston:

- Rural set-asides or "communities under 10,000/50,000" language
  (USDA Rural Development, EPA small-system water programs, DOT Rural).
- No cost share, or a cost share the town could cover in-kind.
- Award floor under ~$250k, or a program that explicitly funds planning.

Programs filed in `grants/` from the 2026-11-04 sweep: USDA RD
(Community Facilities, Water & Waste, SEARCH, ECWAG, Community Connect,
RBDG), NRCS EWP, EPA Brownfields, FEMA (BRIC, HMGP, FMA, AFG, SAFER,
FP&S), DOT SS4A, NTIA Digital Equity, NPS CLG, NEH PAG, and
congressionally directed spending.

## Looked at and rejected (2026-11-04)

- **USDA REAP** — ag producers and rural small businesses only; towns
  not eligible.
- **USDA ReConnect** — towns eligible but no round open or announced
  since 2024. Re-file if a Round 6 NOFO posts.
- **USDA Distance Learning & Telemedicine** — requires running end-user
  sites; not plausible.
- **EPA EJ / Community Change Grants** — terminated 2025, in litigation,
  no open NOFO.
- **EPA Clean School Bus** — school districts only in NY.
- **EPA WIIN small/underserved water grants** — flows to the state; see
  state programs.
- **FEMA EMPG** — states only; reaches counties via DHSES.
- **DOT BUILD (ex-RAISE)** — $1M–$25M capital awards; wrong scale.
- **DOT Rural Surface Transportation** — 90% of funds in $25M+ awards.
- **FHWA Charging & Fueling Infrastructure** — no NOFO, no date.
- **DOE EECBG** — one-time BIL program, window closed 2024.
- **NTIA BEAD** — state-run via ConnectALL; towns aren't applicants.
- **LWCF Outdoor Recreation Legacy Partnership** — urban areas ≥25k
  only. Stateside LWCF is inside the NY Parks EPF round (CFA).
- **Northern Border Regional Commission** — Ulster not an eligible county.
- **IMLS Inspire! small museums** — applicant must be a museum.
- **NEA Grants for Arts Projects** — needs an arts-programming record.
- **FHWA Recreational Trails** — NY pass-through via OPRHP in the CFA.
- **EDA Public Works / Economic Adjustment** — scale and CEDS
  requirement make it implausible; not researched further.

## Prerequisites to apply

Town needs an active SAM.gov registration (UEI) and a Grants.gov
applicant account tied to it. Check with the town clerk/supervisor whether
these exist; SAM renewal lapses are a common reason small towns can't
apply on short notice.

## Quirks

- Forecasted opportunities often give months of warning; posted windows
  have gotten short (weeks). Watch forecasts.
- Many programs are actually administered through the state (formula or
  pass-through). If a federal program looks good but isn't open to towns
  directly, check the NY state agency for the pass-through.
