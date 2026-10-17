# app-policies

Standalone home for privacy policies and related legal pages for **all apps and software** (mobile, desktop, web, extensions, CLI, games). Kept separate from any app's source repo so policy URLs never depend on where an app's code lives.

Served by GitHub Pages from `main`, repo root.

## Live site
**https://axialforge.github.io/app-policies/**

- [Home](https://axialforge.github.io/app-policies/)
- [Pagemark privacy policy](https://axialforge.github.io/app-policies/pagemark/)
- [Terms of Service](https://axialforge.github.io/app-policies/terms/)
- [Contact](https://axialforge.github.io/app-policies/contact/)

| App | Policy URL path |
|---|---|
| Pagemark | `/pagemark/` |

Full URL pattern: `https://<owner>.github.io/<repo>/<slug>/`

## Layout
```
apps/<slug>/app.json      name, tagline, type, source
apps/<slug>/privacy.md    -> /<slug>/            (store privacy-policy URL)
apps/<slug>/<page>.md     -> /<slug>/<page>/     (delete-account, terms, ...)
templates/                privacy + delete-account templates, publish checklist
tools/build.py            markdown -> HTML (committed output)
assets/style.css          shared light/dark styling
```

## Add an app
1. `cp -r apps/pagemark apps/<slug>`, then edit `app.json` and replace `privacy.md` with a copy of `templates/privacy.template.md`, filled in and trimmed to what is true for that app.
2. Add `delete-account.md` (from the template) if the app has accounts.
3. `pip install markdown && python3 tools/build.py`, commit the generated HTML with the sources.
4. Open the live URL in a private window, then paste it into the store console.
5. Run through `templates/PUBLISH-CHECKLIST.md`.

Never rename or delete a published slug or page.

## Keep in sync
The source of truth for a policy is `apps/<slug>/privacy.md` here. If an app repo keeps its own copy, update both in the same release.

Templates are starting points, not legal advice.
