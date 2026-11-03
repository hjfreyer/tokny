---
name: NY Statewide Financial System — Grants Management
url: https://grantsmanagement.ny.gov
level: state
poll: weekly
last_checked: 2026-11-03
---

New York's central state grant portal (successor to the old "Grants
Gateway"). State agencies post funding opportunities here and most
applications are submitted through it. This is likely the richest single
source for a NY town.

## How to search

Confirmed 2026-11-03 via https://grantsmanagement.ny.gov/search-funding-sfs:

Public search ("Find Grant Opportunities"), no login needed to view:
https://esupplier.sfs.ny.gov/psp/fscm/SUPPLIER/ERP/c/NY_SUPPUB_FL.AUC_RESP_INQ_AUC.GBL

It is a PeopleSoft web app, not an API. Filters:

- Status: available / anticipated / available and anticipated / closed
- Eligibility (applicant type): Not-For-Profit, For Profit,
  **Governmental Entity**, Tribal Organization, Individual
- Funding Agency, Service Area, Due Date range, Event ID, name

So the narrowing query is Status = available and anticipated,
Eligibility = Governmental Entity. Expect it to be awkward to scrape;
a browser session may be needed.

The old Grants Gateway (grantsgateway.ny.gov) still exists for
nonprofit prequalification but opportunities now live in SFS.

## Narrowing

Filter to eligible applicant type = local government / municipality.
Agencies most likely to have something for a small town:

- **DEC** — Climate Smart Communities, trees/urban forestry, water quality
  improvement, trails, invasive species
- **EFC** (Environmental Facilities Corp) — water/sewer planning and
  engineering grants, septic replacement, green infrastructure
- **DOS** (Dept of State) — local government efficiency, comprehensive
  plan updates, smart growth, Brownfield Opportunity Areas
- **Parks (OPRHP)** — park development, historic preservation, recreation
  trails
- **Ag & Markets** — farmland protection, ag districts
- **DHSES** — hazard mitigation, emergency equipment
- **Homes & Community Renewal** — NY Main Street, CDBG small cities
- **Archives / Education Dept** — records management (LGRMIF)

## Prerequisites to apply

Town must be "prequalified" / registered in SFS with a vendor ID and have
designated users. Ask the clerk whether the town already has an SFS
account from any prior state award — it probably does.

## Quirks

- Many opportunities here are the same programs as the CFA (see
  `sources/ny-cfa.md`), just applied through a different front door
  depending on the year. Cross-reference before filing duplicates.
- "Anticipated" status often appears months ahead; use it the way
  Grants.gov forecasts are used.
