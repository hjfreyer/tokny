---
name: Grants.gov
url: https://www.grants.gov
level: federal
poll: weekly
last_checked: null
---

The single federal catalog. All 26 grant-making agencies post discretionary
opportunities here. On the order of 1,200 posted and 500 forecasted at any
time, of which a small fraction are open to local governments and a smaller
fraction still make sense for a town of ~900 people.

## How to search

Web: https://www.grants.gov/search-grants

API (no key needed for search):
`POST https://api.grants.gov/v1/api/search2` with a JSON body. Useful fields:

- `oppStatuses`: `posted|forecasted`
- `eligibilities`: applicant-type codes, comma separated. The ones that
  matter here are **`02`** (City or township governments), **`01`** (County
  governments — for pass-through), `04` (Special district governments),
  `99` (Unrestricted). Verify codes against the site's advanced-search
  dropdown before relying on them.
- `agencies`, `fundingCategories`, `keyword`

Fetch a single opportunity's full record with
`POST https://api.grants.gov/v1/api/fetchOpportunity` and `{"opportunityId": N}`.

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
