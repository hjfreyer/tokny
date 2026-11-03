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

Note: this workspace's shell cannot reach `api.grants.gov` (proxy
allowlist), so polls from here go through the web-fetch tool, not curl.

## Narrowing

Most federal opportunities open to "townships" are really aimed at cities
or counties. Signals that one is actually plausible for Kingston:

- Rural set-asides or "communities under 10,000/50,000" language
  (USDA Rural Development, EPA small-system water programs, DOT Rural).
- No cost share, or a cost share the town could cover in-kind.
- Award floor under ~$250k, or a program that explicitly funds planning.

Programs to keep an eye on specifically: USDA Community Facilities,
USDA Rural Energy for America, EPA Brownfields assessment, FEMA BRIC and
Hazard Mitigation (usually via NYS DHSES), DOT Safe Streets for All
planning grants, NEA/IMLS for a library or historical society partner.

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
