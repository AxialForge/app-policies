# Publish checklist (any app or software)

## Policy page
- [ ] Policy is true for the shipped build (every SDK, API, permission, log, backup path)
- [ ] Public HTML URL, no login, not a PDF, HTTPS, stays online permanently
- [ ] Names the app and the developer; has a working contact
- [ ] Added at `apps/<slug>/privacy.md`, built, committed, and the live URL opened in a private window
- [ ] Slug will never be renamed (store listing points at it)

## Google Play
- [ ] Data safety form matches the policy (collected / shared / encrypted in transit / deletion)
- [ ] Account deletion page URL entered if the app has accounts
- [ ] Target audience and Content rating questionnaire answered consistently
- [ ] Ads declaration, permissions declarations (sensitive ones need a justification)
- [ ] Closed test (12 testers x 14 days) done if a personal account created after 2023-11-13

## Apple App Store
- [ ] App Privacy "nutrition labels" match the policy
- [ ] Privacy policy URL set in App Store Connect; account deletion in-app if sign-up exists
- [ ] Privacy manifest / required-reason API declarations for SDKs

## Desktop / web / CLI / extensions / games
- [ ] Windows/macOS: installer or store listing links the policy; signing as required
- [ ] Browser extension: stores require a policy URL and a per-permission justification
- [ ] SaaS/web: add cookie notice if you use non-essential cookies; add Terms if users pay or post content
- [ ] Open source: LICENSE present; policy covers telemetry, update checks, crash upload

## Triggers that force a policy update BEFORE release
New network call or SDK, analytics/ads, accounts, new permission, new backup/sync path, payments, user content.
