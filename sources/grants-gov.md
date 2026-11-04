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

API — confirmed 2026-11-03 against the official API guide
(https://grants.gov/api/api-guide): no key or auth needed for `search2`
or `fetchOpportunity`.

`POST https://api.grants.gov/v1/api/search2`, JSON body, e.g.
`{"keyword": "", "oppStatuses": "forecasted|posted", "rows": 100, "startRecordNum": 0}`.
Other accepted fields (from third-party clients, not the official guide):
`eligibilities`, `agencies`, `fundingCategories`, `aln`.

- `eligibilities` takes two-digit codes, comma separated. Confirmed
  examples: `12` = 501(c)(3) nonprofits, `13` = other nonprofits,
  `21` = individuals, `23` = small businesses. **Not yet confirmed:**
  `02` = City or township governments, `01` = County, `04` = Special
  district, `99` = Unrestricted. The `search2` response carries an
  `eligibilities` facet with code→label pairs; read the mapping from
  there on the first real poll and record it here.
- The applicant-type *labels* used by Grants.gov are: City/Township
  Governments, County Governments, Special District Governments, State
  Governments, Unrestricted, and the usual nonprofit/business/individual
  ones.

`POST https://api.grants.gov/v1/api/fetchOpportunity` with
`{"opportunityId": N}` returns the full record; eligible-applicant text
is in the `synopsis` object (or `forecast` for forecasted ones).

Note: this workspace's shell cannot reach `api.grants.gov` or
`www.grants.gov` (proxy allowlist), and the www search page is JS-only
so web-fetch gets nothing from it either. What does work from here:
`https://simpler.grants.gov/opportunity/<id>` renders eligible applicant
lists, dates, ceilings and cost-share as static HTML. Until the API host
is allowlisted, discovery is agency pages + web search, verification is
simpler.grants.gov.

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
