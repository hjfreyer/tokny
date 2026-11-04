# tokny — Town of Kingston grant harness

A git repo of markdown that tracks grant opportunities relevant to the
**Town of Kingston, NY** (Ulster County; not the City of Kingston): where
to look for them, what has been found, and whether each one is worth
pursuing.

The repo is the database. Git history is the audit trail. Nothing is
submitted anywhere without a human reading the diff.

## Layout

```
sources/   one file per feed we poll (Grants.gov, NY SFS Grants, CFA, ...)
grants/    one file per opportunity we have looked at
tools/     scripts; `python3 tools/index.py` regenerates grants/INDEX.md
```

Planned but not started: `town/` (facts about the town that applications
may cite), `applications/` (drafts and submissions), `log/`.

## Conventions

Every file has YAML frontmatter with a few filterable fields and a
free-form markdown body. The frontmatter is the only thing a script
should ever need to parse; everything else is prose for humans and LLMs.

### `sources/<slug>.md`

```yaml
---
name: Grants.gov
url: https://www.grants.gov
level: federal          # federal | state | county | utility | foundation | other
poll: weekly            # how often it is worth checking
last_checked: null      # ISO date, or null if never
---
```

Body: how to search it, what filters narrow it to things a NY town can
apply for, and anything learned about its quirks.

### `grants/<slug>.md`

Slug: `<year>-<funder>-<short-name>`, e.g. `2026-nyserda-clean-energy-communities`.

```yaml
---
title: Clean Energy Communities
funder: NYSERDA
source: nyserda          # slug of the sources/ file it was found through
url: https://...
amount: "$5,000 – $100,000"   # free text; ranges and "varies" are fine
match: none              # none | 10% | "varies" ...
deadline: 2027-01-15     # ISO date, or "rolling", or null
found: 2026-11-03
status: candidate        # see below
fit: unassessed          # unassessed | poor | possible | good | strong
---
```

`status` lifecycle:

- `candidate` — seen, not yet assessed
- `assessed` — fit judged (see `fit`), no decision yet
- `pursuing` — town has decided to apply
- `applied` — submitted
- `awarded` / `declined` / `passed` — terminal; `passed` means we chose not to apply
- `expired` — deadline went by without action

Body sections, in this order:

1. **Summary** — what the program funds, in a paragraph.
2. **Eligibility** — quoted or closely paraphrased from the notice, with
   a verdict on whether the Town of Kingston qualifies and why.
3. **Fit** — why it does or doesn't match the town's needs. Every claim
   about the town must be checkable; if `town/` doesn't exist yet, say
   "needs confirmation" rather than guessing.
4. **Effort** — what applying would actually take (forms, attachments,
   board resolution, matching funds, registration prerequisites).
5. **Notes** — anything else, dated.

## Rules

- Do not invent facts about the town. Unknown is a valid answer.
- Do not contact anyone, submit anything, or create accounts anywhere
  from automation. Those steps are human-only.
- Record where every opportunity came from so it can be re-checked.
