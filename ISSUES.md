# StackCalc launch issues

**Last reviewed:** 2026-09-23  
**Scope:** StackCalc canonical content, Hackaday project readiness, and Etsy-ready physical accessories.  
**Out of scope:** publishing source code, selling the calculator before physical validation, and replacing Shopify before a marketplace decision is verified.

## How to use this list

Each issue has one accountable lead, supporting groups, dependencies, and an acceptance condition. The accompanying [history record](ISSUE_HISTORY.md) has the decision basis and evidence for the same ID. Check an item only when its acceptance condition is demonstrated, not when a draft exists.

## Blog and StackCalc site

- [ ] **BLOG-01 — Establish the canonical post map**  
  **Lead:** Content owner · **Support:** Engineering, design · **Depends on:** none  
  Map each published StackCalc article to its matching Hackaday log or record why it has no companion. Accept when no paired entries contradict one another and StackCalc owns the long-form source.

- [ ] **BLOG-02 — Complete the public-claim audit**  
  **Lead:** Engineering owner · **Support:** Content owner · **Depends on:** BLOG-01  
  Review all 13 public posts, front matter, captions, downloads, and cross-links against the current prototype stage. Accept when every claim is tagged as app, emulator, model, printed specimen, board-design, or measured board result.

- [ ] **BLOG-03 — Triage the legacy archive**  
  **Lead:** Content owner · **Support:** Engineering owner · **Depends on:** BLOG-02  
  Keep the untracked `archive/` intact; classify each legacy draft as revise, consolidate, or remain unpublished. Accept when no archived draft is accidentally deployed and every revival has a current-evidence rewrite.

- [ ] **BLOG-04 — Add canonical feed and cross-link behavior**  
  **Lead:** Web owner · **Support:** Content owner · **Depends on:** BLOG-01  
  Publish a StackCalc RSS/Atom feed or an equivalent documented feed endpoint, then link individual Hackaday logs to their canonical StackCalc article. Accept when a feed reader exposes the current public posts and links do not rely on an undocumented Hackaday project feed.

- [ ] **BLOG-05 — Validate social cards and media**  
  **Lead:** Web owner · **Support:** Design · **Depends on:** BLOG-02  
  Check Open Graph and X/Twitter previews for the home page, Learning Lab, hardware guide, and every public post. Accept when each has a truthful image, title, description, and canonical URL without showing an unlabelled prototype as a finished calculator.

- [ ] **BLOG-06 — Retire stale Shopify messaging after the channel decision**  
  **Lead:** Web owner · **Support:** Commerce owner · **Depends on:** ETSY-01, ETSY-07  
  Replace or remove public Shopify-era terms, support, and store links only after the final channel and policy are confirmed. Accept when the live site has no purchase, return, or availability promise that does not match the active channel.

## Hackaday project

- [ ] **HDA-01 — Reconcile project Details, summary, and components**  
  **Lead:** Project owner · **Support:** Engineering, content · **Depends on:** BLOG-02  
  State that the board design is in fabrication and that photos are mechanical prototypes. Accept when every component, summary, and Details paragraph makes the app/emulator/printed-board boundary clear.

- [ ] **HDA-02 — Curate hero and proof assets**  
  **Lead:** Design owner · **Support:** Project owner · **Depends on:** HDA-01  
  Select a real prototype hero photograph and keep the proof reel, app views, membrane model, and stand photographs labeled by medium. Accept when the first project screen contains one clear hero and the proof reel plays with a text fallback.

- [ ] **HDA-03 — Synchronize the initial log set**  
  **Lead:** Content owner · **Support:** Engineering · **Depends on:** BLOG-01, HDA-01  
  Reformat the agreed canonical posts into Hackaday logs using the same facts, source links, and images. Accept when each log has a useful technical lesson, a concrete artifact, and one precise discussion invitation.

- [ ] **HDA-04 — Publish useful, bounded project files**  
  **Lead:** Engineering owner · **Support:** Education owner · **Depends on:** HDA-01  
  Attach only the approved mechanical STL set, selected print references, teacher-facing PDFs, and media. Accept when every file is named by revision and purpose, links back to StackCalc for canonical downloads, and no implementation source is exposed.

- [ ] **HDA-05 — Repair build instructions to current board status**  
  **Lead:** Engineering owner · **Support:** Project owner · **Depends on:** HDA-01, HDA-04  
  Replace stale statements that the PCB has not been fabricated; separate printed-assembly directions from later electronic integration. Accept when a reader can print and assemble the four mechanical parts without inferring that a powered calculator is included.

- [ ] **HDA-06 — Define the launch cadence and community asks**  
  **Lead:** Project owner · **Support:** Content owner · **Depends on:** HDA-03  
  Choose the first public log order and one narrow engineering question per applicable post. Accept when the calendar does not manufacture updates and commenters can respond to a specific test, geometry, or usability question.

- [ ] **HDA-07 — Run the board-arrival evidence session**  
  **Lead:** Engineering owner · **Support:** Design, firmware · **Depends on:** fabricated-board delivery  
  Record board seating, display alignment, connector clearance, matrix/switch reach, cap closure, boot, and first known calculation separately. Accept when photographs, revision IDs, method, results, and failures are published before stronger hardware claims.

- [ ] **HDA-08 — Make the project public only after the launch gate**  
  **Lead:** Project owner · **Support:** Content, design · **Depends on:** HDA-01 through HDA-06  
  Change project visibility after an editorial review of the public page. Accept when the live page has no private-draft wording, stale component information, inaccessible key media, or unsupported finished-product claim.

## Etsy products and operations

- [ ] **ETSY-01 — Verify channel and tax/registration posture**  
  **Lead:** Commerce owner · **Support:** Tax/legal adviser · **Depends on:** none  
  Obtain Etsy’s current marketplace-facilitator documentation for the operating location and decide whether all initial physical sales will remain marketplace-only. Accept when the seller account, tax identity, local registration needs, and recordkeeping owner are documented.

- [ ] **ETSY-02 — Freeze the initial SKU set**  
  **Lead:** Product owner · **Support:** Education, design · **Depends on:** ETSY-01  
  Limit the first release to the Learning Lab physical kit, puzzle stand, and a printed workbook or differentiated classroom pack. Accept when each SKU has named contents, variation policy, revision, and an explicit exclusion of the unfinished calculator.

- [ ] **ETSY-03 — Validate print and assembly reproducibility**  
  **Lead:** Fabrication owner · **Support:** Design · **Depends on:** ETSY-02  
  Print at least the intended sellable configuration repeatedly, record material/profile/orientation/post-processing, and inspect fit. Accept when each SKU has a reproducible process, specimen log, reject criteria, and packaging dimensions.

- [ ] **ETSY-04 — Create truthful listing media and copy**  
  **Lead:** Design owner · **Support:** Content, fabrication · **Depends on:** ETSY-03  
  Photograph the actual sellable revision in use and identify materials, dimensions, included items, age/safety considerations, and processing time. Accept when no render, simulator frame, or unlabelled calculator prototype is presented as the product for sale.

- [ ] **ETSY-05 — Establish fulfillment, replacement, and return handling**  
  **Lead:** Commerce owner · **Support:** Fabrication owner · **Depends on:** ETSY-01, ETSY-03  
  Write the customer-facing policy and run a test order. Accept when a buyer can receive tracking, request a replacement/return, and get a response without a separate Shopify workflow.

- [ ] **ETSY-06 — Define teacher-material licensing and value**  
  **Lead:** Education owner · **Support:** Content, commerce · **Depends on:** ETSY-02  
  Preserve the existing free PDFs on StackCalc; define the printed workbook or expanded classroom pack as materially different and specify individual/classroom use. Accept when listing contents and download policy do not sell a file that remains free unchanged on StackCalc.

- [ ] **ETSY-07 — Close or redirect Shopify only after an end-to-end test**  
  **Lead:** Commerce owner · **Support:** Web owner · **Depends on:** BLOG-06, ETSY-01 through ETSY-06  
  Test the selected marketplace from listing through support, then retire Shopify purchase paths. Accept when every legacy link has an intentional destination and public terms/support copy matches the new workflow.

- [ ] **ETSY-08 — Hold the calculator listing behind hardware gates**  
  **Lead:** Product owner · **Support:** Engineering, support · **Depends on:** HDA-07, ETSY-03 through ETSY-05  
  Do not create a purchasable calculator listing while the PCB is in fabrication. Accept only after physical board fit, powered operation, labeled controls, fulfillment packaging, and support terms are documented for the offered revision.

## Cross-workstream release gate

- [ ] **REL-01 — Approve the public launch package**  
  **Lead:** Project owner · **Support:** Engineering, content, design, commerce  
  **Depends on:** BLOG-01 to BLOG-05, HDA-01 to HDA-06  
  Accept when a fresh reviewer can identify the current prototype stage, open canonical assets, understand what is and is not for sale, and reach a working support channel without encountering stale Shopify or finished-hardware language.
