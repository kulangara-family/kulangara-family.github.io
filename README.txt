# Our Family — Responsive Family Tree

A simplified, responsive family-tree website built from the supplied family data.

## What changed
- Cleaner family-first layout with the founding couple at the top.
- Main family branches are separated into easy-to-understand cards.
- Branches open only when needed, avoiding a huge complicated diagram.
- Mobile-first responsive layout for phones, tablets and desktop.
- Fast name search that opens the relevant family path.
- Simple Malayalam / English switch.
- Click any person for a focused profile.
- Print-friendly layout.
- Existing `data/family.json` and `photos/` are preserved.

## Update family data
Edit only:
`data/family.json`

Each person keeps a unique `id`, `children` list and optional `spouse`.

## Run locally
Modern browsers block JSON fetching from a `file://` page. Use the included launcher:
- Mac: `START_FAMILY_TREE.command`
- Windows: `START_FAMILY_TREE.bat`

Or run:
`python3 server.py`

Then open the local address shown by the server.

## Hosting
Upload the complete folder to a normal static host. The site reads `data/family.json` automatically.
