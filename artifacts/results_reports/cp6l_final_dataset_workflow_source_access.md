# CP-6L Final Dataset Source Access Report

- Phase: `CP-6L`
- Selected candidate: `cosmx_6k_bcc_yerly_2024`

## Rejection Rules

- `reject_visium_spot_level_only`
- `reject_scrna_visium_deconvolution_as_cells`
- `reject_gated_or_login_only_without_modal_url`
- `reject_missing_expression_coordinates_ids_or_labels`
- `use_scar_scpanstroma_as_indexes_only`

## Candidates

### htapp_mbc_scp2702_merfish

- Decision: `reject_htapp_for_cp6l_modal_compute`
- Accepted for Modal compute: `False`
- Reason: SCP describes MERFISH H5AD bundles, but the public CELLxGENE API currently exposes spatial H5AD assets as Slide-seq, not MERFISH; SCP bundle download requires a logged-in/download workflow rather than a clean unauthenticated Modal URL.
- Source: https://singlecell.broadinstitute.org/single_cell/study/SCP2702

- Public spatial H5AD count: `15`
- Public MERFISH H5AD count: `0`
- Public Slide-seq H5AD count: `15`

### cosmx_6k_bcc_yerly_2024

- Decision: `accept_cosmx_6k_bcc_for_modal_preflight`
- Accepted for Modal compute: `True`
- Reason: Zenodo provides an open direct RDS URL, CC BY 4.0 license, cell-level metadata, coordinates, labels, and 6,075-gene CosMx coverage.
- Source: https://zenodo.org/records/14330691
