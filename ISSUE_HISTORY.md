# StackCalc launch issue history

This is a decision record for [ISSUES.md](ISSUES.md). It records the evidence available on 2026-09-23, why each issue exists, and the boundary that prevents a premature claim. It is not a substitute for a dated test record when physical hardware arrives.

## Evidence baseline

The StackCalc public site contains 13 current engineering posts, public Learning Lab STL/PDF downloads, a mechanical-prototype STL pack, app imagery, a membrane-study video, and a proof reel. The legacy 70+ post collection is currently outside the public documentation tree in `archive/unpublished-blog/`. The project’s current evidence is a tool-free printed mechanical assembly, app behavior, and RP2350 firmware emulation. The KiCad RP2350 board design is in fabrication; no installed, powered board specimen has been represented as available.

The planned sales boundary is equally important: StackCalc will publish selected STLs and teacher PDFs, not implementation source. The first candidate paid goods are physical objects or materially expanded printed resources. The same free PDF should not be relisted as a paid digital product.

## Blog and StackCalc site

### BLOG-01 — Establish the canonical post map

**History:** The project previously developed parallel website and Hackaday wording, which made it easy for one surface to refer to an older hardware stage. The current decision is that StackCalc Markdown is the factual source and Hackaday is a layout-specific rendering of it.  
**Evidence:** `docs/blog/posts/`, the StackCalc Learning Lab and hardware guides, and the Hackaday project logs.  
**Decision boundary:** Different titles and image placement are allowed; a different claim about board status, test result, file availability, or product readiness is not.

### BLOG-02 — Complete the public-claim audit

**History:** The current published posts already distinguish emulation from board behavior in several places, but the evidence needs a repeatable audit rather than relying on a few corrected sentences.  
**Evidence:** The app is live; the emulator exercises compiled firmware; the printed specimen is unpowered; the board is in fabrication.  
**Decision boundary:** Simulation results may guide next tests but cannot be promoted to battery, latency, force, fatigue, or electrical claims.

### BLOG-03 — Triage the legacy archive

**History:** The archived posts include future-dated drafts and descriptions of stages that do not match the current public prototype. They were left untracked and outside MkDocs rather than deleted so their useful ideas remain available for review.  
**Evidence:** `archive/unpublished-blog/` is not in the published `docs/blog/posts/` path.  
**Decision boundary:** A legacy article is not publishable merely because its subject is plausible. It must be reconciled to a current artifact and current date.

### BLOG-04 — Add canonical feed and cross-link behavior

**History:** Hackaday’s global feed is known, but a supported per-project RSS feed was not confirmed. StackCalc should therefore own its outbound feed and link directly to individual Hackaday logs when useful.  
**Evidence:** StackCalc uses MkDocs Material with the blog plugin; current content is already organized as dated Markdown posts.  
**Decision boundary:** Do not build cross-listing automation around an undocumented Hackaday feed endpoint.

### BLOG-05 — Validate social cards and media

**History:** Social metadata was added during the earlier launch work, but a metadata declaration is not proof that a social platform renders the intended card. The project also has both renders and real prototype photos, which must not be conflated.  
**Evidence:** `docs/assets/` includes application captures, real printed-prototype photos, CAD renders, model frames, and video.  
**Decision boundary:** The card image must accurately represent the page and must identify a render or simulation where that distinction matters.

### BLOG-06 — Retire stale Shopify messaging after the channel decision

**History:** `docs/ecommerce.md` and the `shopify/` directory retain historical product copy that describes unavailable hardware and a Shopify purchase flow. `ecommerce.md` is currently excluded from public navigation, but legal/support language must be reconciled at the moment the sale channel changes.  
**Evidence:** `mkdocs.yml` excludes `ecommerce.md`; historical CSV/import content remains in `shopify/`.  
**Decision boundary:** Do not delete or redirect terms, privacy, or support information until an actual marketplace account, policy, and support route are set.

## Hackaday project

### HDA-01 — Reconcile project Details, summary, and components

**History:** The public description evolved as the board moved from design to fabrication. The key distinction is now stable: the KiCad design is in fabrication, the visible calculator is mechanical and unpowered, and firmware behavior has been exercised in emulation.  
**Evidence:** Current project Details, component list, site posts, and prototype media.  
**Decision boundary:** Do not describe the board as installed, powered, tested, or available until a photographed and documented specimen supports that claim.

### HDA-02 — Curate hero and proof assets

**History:** The project has enough media to make a strong project page: real printed-prototype photos, app captures, a membrane-study video, packaging/stand photos, and a proof reel. The risk is not lack of media; it is letting a polished render or unlabelled mechanical assembly imply completed electronics.  
**Evidence:** `docs/assets/prototype-*.jpg`, stand images, `stackcalc-proof-reel.mp4`, and `tpu-membrane-simulation.mp4`.  
**Decision boundary:** The hero must be a real printed item and captions must identify simulations and companion apps.

### HDA-03 — Synchronize the initial log set

**History:** Thirteen logs exist around the current prototype story. Earlier versions read as status reports; the updated direction is a detailed, reproducible lesson per log.  
**Evidence:** Published StackCalc posts on the Watch constraint, core/emulator, sliding assembly, membrane study, Learning Lab, fuzzing, PCB envelope, and stand.  
**Decision boundary:** A log need not duplicate site chrome, but it must retain the source article’s factual stage and link back for canonical files.

### HDA-04 — Publish useful, bounded project files

**History:** The project intends to share selected mechanical files and teacher materials but not source code. Older spring fixtures and alternate mechanical pieces exist; they are research artifacts rather than the current four-part assembly.  
**Evidence:** Public mechanical ZIP and Learning Lab ZIP; current four-part file names are documented in the evidence-ledger post.  
**Decision boundary:** Attach only a clear revisioned set. Do not let an exploratory STL be mistaken for the recommended build or expose private implementation source.

### HDA-05 — Repair build instructions to current board status

**History:** An older Hackaday instruction still said the PCB had not been fabricated. That wording became stale once fabrication began.  
**Evidence:** Current known stage is board in fabrication, printed mechanical assembly available for inspection.  
**Decision boundary:** Mechanical build instructions may be published now; electrical assembly instructions wait for the received board and actual integration results.

### HDA-06 — Define the launch cadence and community asks

**History:** The project has a deep source archive, but publishing every historical topic would dilute the real milestones. The goal is discussion around decisions that a maker can inspect or help test.  
**Evidence:** Existing technical topics and Hackaday’s project-log format.  
**Decision boundary:** Do not create artificial weekly updates. Publish a new log when there is a real artifact, decision, measurement, or question.

### HDA-07 — Run the board-arrival evidence session

**History:** The first board is expected after fabrication, which creates the first opportunity to validate the 3D envelope against actual electronics. Simulated firmware and CAD informed the design but did not replace this session.  
**Evidence:** Board-design article identifies seating plane, display opening, connector, matrix reach, and cap-clearance checks.  
**Decision boundary:** Record fit, boot, display, keypad, and power as separate observations; a booted display does not prove key feel or battery behavior.

### HDA-08 — Make the project public only after the launch gate

**History:** The project is currently held while content is drafted and reviewed. Its public launch should be a quality decision, not a workaround for incomplete page sections.  
**Evidence:** Initial logs, project Details, proof reel, components, media, and planned files/instructions.  
**Decision boundary:** Visibility changes only after stale draft wording and status contradictions have been removed and the initial reader journey works.

## Etsy products and operations

### ETSY-01 — Verify channel and tax/registration posture

**History:** The commerce direction changed from Shopify/Tindie exploration to Etsy as the preferred first marketplace for physical teaching and printed products. Marketplace-facilitator tax collection, merchant-of-record terminology, and local licensing are separate questions.  
**Evidence:** California guidance recognizes a marketplace-only seller exception only when a registered facilitator is responsible for those sales; Etsy’s current seller terms and operating-location requirements still need confirmation for the actual account.  
**Decision boundary:** Do not close Shopify or publish a purchase link based on a general platform description. Preserve written channel confirmation and use a qualified local adviser for location-specific obligations.

### ETSY-02 — Freeze the initial SKU set

**History:** Several product ideas appeared in older Shopify files, including completed-calculator claims that do not match the current physical stage. The safer first catalog is limited to products that can be truthfully photographed and fulfilled today once print validation is complete.  
**Evidence:** Learning Lab assets, puzzle stand prototypes, and teacher PDFs are present; a physically validated powered calculator is not.  
**Decision boundary:** The calculator stays off the catalog until ETSY-08 is complete.

### ETSY-03 — Validate print and assembly reproducibility

**History:** The team has 3MF print settings and real prototype photographs, but a printable source file is not proof of repeatable sellable manufacturing. The Learning Lab and stand each need their own repeat-print and packing record.  
**Evidence:** Slicer profiles, public STLs, physical prototype photographs, and the current mechanical guide.  
**Decision boundary:** A successful single print is exploratory evidence. A SKU requires a defined material/profile, tolerance observations, reject criteria, and a packaging check.

### ETSY-04 — Create truthful listing media and copy

**History:** The project has high-quality app screens, simulations, CAD renders, and prototype photos. Marketplace policy and buyer trust require that the physical item for sale be shown accurately.  
**Evidence:** Etsy’s seller policy requires accurate representation and seller-owned photos/video; StackCalc has real photo assets ready for this purpose.  
**Decision boundary:** Do not use a software image, unlabelled calculator body, or simulation frame as the primary evidence for a physical Etsy SKU unless explicitly labeled and supported by real product photography.

### ETSY-05 — Establish fulfillment, replacement, and return handling

**History:** The desire to leave Shopify includes reducing checkout and tax operations, not abandoning buyer support. A marketplace can host transactions, but the maker still needs an actual lead time, packing process, return address, and replacement choice.  
**Evidence:** Existing support and terms pages require a future channel-specific update.  
**Decision boundary:** A listing is not ready until a test order has been shipped, tracked, received, and handled through the proposed support path.

### ETSY-06 — Define teacher-material licensing and value

**History:** The project decision is to publish the base teacher PDFs and selected STLs free on StackCalc. A paid Etsy item must therefore add physical manufacturing, printing, organization, expanded material, or a separately defined classroom license.  
**Evidence:** Current Learning Lab download pack contains the public PDFs and printed artifacts.  
**Decision boundary:** Never charge for an unchanged copy of a file that StackCalc offers free.

### ETSY-07 — Close or redirect Shopify only after an end-to-end test

**History:** Older commerce copy includes Shopify URLs and future-hardware promises. Removing Shopify early could leave broken product links or an unsupported return route.  
**Evidence:** `shopify/` materials, excluded `docs/ecommerce.md`, and current support/terms pages.  
**Decision boundary:** Keep historical source material out of public navigation, but remove/redirect buyer-facing paths only after the selected marketplace transaction and support test succeeds.

### ETSY-08 — Hold the calculator listing behind hardware gates

**History:** The physical calculator is the most compelling future product and also the least proven current SKU: the board remains in fabrication and visible specimens are mechanically incomplete.  
**Evidence:** Current published status of the RP2350 design, emulator, and four-part printed prototype.  
**Decision boundary:** No preorder, estimated performance claim, or product listing until the offered board revision has passed fit, powered operation, labels, packaging, and support validation.

## Cross-workstream release gate

### REL-01 — Approve the public launch package

**History:** The project has enough content for a coherent launch, but quality depends on the consistency of the reader’s path across the StackCalc site, Hackaday, and the eventual product pages.  
**Evidence:** The complete checklist in `ISSUES.md`, proof reel, public downloads, current blogs, and project logs.  
**Decision boundary:** Approval is a review of the assembled reader journey. Passing individual copy edits or uploading individual assets does not by itself authorize public launch or commerce.
