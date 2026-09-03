# Missing Provenance

## Source versions

1. **Rung1 v1-v6 and v10-v18:** no standalone source, Git object, archive member or notebook checkpoint was found. One notebook calls `/home/claude/rung1_v5.py`; the path is external and absent. The available `rung1_v7.py` internally calls itself “RUNG 1 v5,” creating unresolved filename/version ambiguity.
2. **v31l-v31o / G2c:** no source-cell occurrence, file, branch, tag, archive member, preregistration, patcher, configuration, raw cache or decision record was found. The official linked repository ends at v30 at commit `8f6c942e...`, eleven days before the supplied paper date.
3. **Original 01Q in the linked ledger:** the linked repo contains only a 2,717-byte reconstructed shim and states the original was lost. A separate earlier handoff contains a 36,239-byte full 01Q source (`4821AF...`) that drives Paper 1's 428.333 replay. The linked ledger does not prove that this handoff file is the exact lost dependency used for every later archived v21 row; its own certification scope is scalar-only.

## Manuscript sources

4. **QM_GR_1:** a close 12-page TeX/source package exists and matches the supplied paper's structure and claims. The supplied PDF itself is byte-identical only to a duplicate under `unification/ringdown_revisted`; no Git history pins the TeX revision.
5. **QM_GR_2:** the best TeX compiles to a 17-page predecessor. The supplied PDF has 21 pages and substantially more text. No exact revision TeX/notebook source was found.
6. **GR_QM:** commit `30c122d9...` contains a 13-page predecessor. The supplied 20-page July-9 revision has no matching TeX; Table 2, Table 3 and appendices were added outside the archived source.
7. **grav_geometry:** no TeX/Markdown source was found. Only the supplied PDF provides the exact prose, Fig.1 and Table1.

## Figure/data chains

8. **Paper 1 figure assembly:** the audit notebook generates semantically matching unprefixed images, while the manuscript package contains renamed `fig1_...` through `fig6_...` images. No copy/rename or final figure-build script is archived.
9. **Paper 2 package:** executed notebooks use absolute `/mnt/data/...` roots. The standalone directory retains final figures and three verdict CSVs but omits many generated intermediate CSVs and imports Bell source modules from a separate `not_final` package. Reproduction requires path relocation/staging.
10. **GR_QM final figures:** legacy Figs.1/3/4 have `make_figures.py`; the linked repo's relieved/knee/transfer/bracket PDFs have underlying data and engine scripts but no exact plot code. The complete two-queue reducer used for the bracket is not an executable archived module.
11. **GR_QM bridges:** exact table-assembly code is absent. Ringdown Table 3 values can be traced to `deu_ligo_exp02_outputs`; Table 2 is a manuscript selection across separate repositories/models.
12. **grav_geometry Fig.1/Table1:** all generating code and raw data are missing: v31o, R26 paired arms, seeds/config, support-matched control implementation, null-generation code, figure builder and G2c decision record.

## Model interfaces

13. No registry-node -> foam-face map.
14. No native 27-slice or 18-node I-channel map.
15. No registry/psi0 edge -> v21 forced-request or Gamma map.
16. No closure path/phase -> causal ancestry/topological-clock map.
17. No two-queue backlog -> registry conflict map.
18. No available source for the metric-work -> veto/capacity map claimed by v31.

These are provenance gaps, not global correctness judgments. `CLAIM_SOURCE_MATRIX.csv` records their claim-local effect.
