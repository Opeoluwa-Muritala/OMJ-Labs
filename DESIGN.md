# OMJ Labs portfolio design

The portfolio reads as a founder's studio folio. A large personal statement and an abstract typographic portrait establish Opeoluwa Muritala Joel and OMJ Labs immediately. The site fills the browser width; text uses comfortable internal gutters while project artwork runs to the edges of its grid cells.

## Visual system

- Outside project artwork, use deep charcoal, warm ivory, and muted lime for small highlights and buttons.
- Each project card keeps its own visual identity and may use colors from the product itself.
- Bricolage Grotesque handles display text; DM Sans handles body copy. Both fonts are self-hosted.
- The graphic portrait uses Three.js for subtle pointer-responsive depth, with a smaller Three.js form at the studio section. CSS artwork and type remain visible when WebGL or motion is unavailable.
- The logo combines an open orbit with M and J strokes and a small point of light. It is supplied as a symbol plus dark and light wordmarks. The loading screen animates rings around the symbol with Three.js, then yields quickly to page content.

The effective site tokens in `dist/styles.css` are charcoal `#111b1d`, paper `#edeee6`, and muted lime `#d5ef82`. The shared shell uses these colors; project art is free to follow its own product palette. The final overrides near the end of the CSS file are the active palette definitions.

For live products, match the project artwork to the product: FieldCRM uses purple, Event-Response uses midnight and hot pink, ShopPal uses navy and blue, and Aptus uses violet and teal. The other cards keep their individually art-directed palettes.
New_Kuz uses the public app's purple brand and a logo asset from its repository.

## Information architecture

The homepage introduces the founder, lists selected work, explains OMJ Labs, adds professional experience, and ends with direct contact links. Every selected project has its own static page with a larger visual, context, stack, conceptual interface previews, and source or live links where available. Live products also have captured public landing screens; conceptual screens are labeled as such.

`build_projects.py` produces every case page from one shared template. FieldCRM, Event-Response, ShopPal, and Aptus have captured live landing screens. ScholarNavigate uses screenshots published in its repository. The remaining pages use labeled concept previews until product screenshots are available.

## Implementation notes

Run `python build_projects.py` after changing the curated project list, card content, or project page template. The homepage requests public GitHub metadata in the browser and retains curated copy if the request fails. Avoid making unconfirmed claims about private projects or unavailable repositories.

The header combines the compact SVG symbol with HTML wordmark text; the two full SVG wordmarks are supplied as reusable assets. The loading animation closes after about 850 ms. It uses CSS artwork if WebGL fails and is removed immediately when reduced motion is requested.
