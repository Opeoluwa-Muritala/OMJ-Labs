# Opeoluwa Muritala portfolio

A static, responsive portfolio for Opeoluwa Muritala Joel. The published files are in `dist/`.

The selected projects have individual static pages in `dist/projects/`. Live products include captured public landing screens, while the other pages clearly label their illustrative interface previews as concepts. On each visit, `dist/script.js` requests public repository metadata from GitHub and updates the language and last push date. The curated content remains visible if the request fails or reaches GitHub's unauthenticated rate limit. No GitHub token is used in the browser.

Run `python build_projects.py` after editing the project list or homepage cards to regenerate the project pages. The hero artwork uses a self-hosted Three.js module and keeps its CSS artwork as a fallback.

The OMJ Labs identity is available as [`dark`](dist/assets/omj-labs-logo-dark.svg) and [`light`](dist/assets/omj-labs-logo-light.svg) SVG wordmarks plus a compact [`symbol`](dist/assets/omj-mark.svg). The header and favicon use the symbol. All pages show a short Three.js logo animation when loading, with a reduced-motion fallback.

The `ticket-api` link in the profile README currently returns 404, so its card intentionally has no repository link. Add a confirmed link before enabling a source button.

Preview locally with any static HTTP server serving `dist/`, for example `python -m http.server 8000 --directory dist`.
