# Approved editorial changes

This map fixes the entire manuscript-source delta for the authorized polish and publication. It is applied to a separate release copy. The two supplied replacement files are complete exact sources; the unified diff makes their changes reviewable.

## P01 — Abstract precision

Source: manuscript/main.tex

Before:

    endpoint stock is of fourth inverse order

After:

    endpoint stock is bounded by a fourth inverse power

## R01 — PDF subject

Source: manuscript/main.tex

Before:

    Research manuscript v0.1. Accepted underlying investigations; final manuscript review pending. 4 November 2026.

After:

    Research manuscript v0.1. Manuscript internally accepted; publication authorized by the author. 4 November 2026.

## R02 — Running version header

Source: manuscript/main.tex

Before:

    \fancyhead[R]{\small v0.1 draft}

After:

    \fancyhead[R]{\small v0.1}

## R03 — Title-page status

Source: manuscript/main.tex

Before:

    {\itshape Draft for manuscript review\par}

After:

    {\itshape Publication edition\par}

## R04 — Title-page contribution status

Source: manuscript/main.tex

Before:

    The underlying mathematics is accepted with formulas and hypotheses unchanged;
    review of this final manuscript by GPT and the author is pending.

After:

    The underlying mathematics is accepted with formulas and hypotheses unchanged.
    GPT accepted the submitted manuscript; the author approved editorial closeout and publication.

## R05 — Final contribution status

Source: manuscript/conclusion.tex

Before:

    The underlying mathematics is accepted; GPT/author review of this final PDF is pending.

After:

    The underlying mathematics and submitted manuscript are internally accepted; the author has authorized this publication edition.

## Scope and source identity

All eight other TeX files and the build helper retain their reviewed hashes. SOURCE_IDENTITIES.json binds both reviewed and approved bytes for the affected files. No equation, proof, quantitative hypothesis, normalization, citation, bibliography entry or geometric paragraph changes.

Release README/provenance/build records, source/PDF identities, current verification and manifests must separately be updated from the actual release work. The old review records stay intact as historical evidence. The newly rebuilt PDF is checked by Codex; this order does not claim GPT inspected it in advance.

Preserve the edition date and version. The active publication metadata must accurately record that GPT accepted the submitted manuscript and the author authorized this editorial closeout and publication.
