# Local conditional profile likelihoods in IDM-DR cosmology

This repository accompanies the manuscript **“A Calibration-Aware Local Sensitivity Study of Interacting Dark Matter-Dark Radiation Cosmology with Planck 2018, DESI DR2, and Pantheon+.”**

## Main result

A seven-point fixed-interaction screen was evaluated while profiling seven shared cosmological/calibration parameters. The lowest independently reevaluated point among those tested was:

- `f_idm = 0.0035`
- `N_idr = 0.020`
- `a_idm_dr = 47612.96`
- `nindex_idm_dr = 4`
- `idr_nature = free_streaming`
- exact data chi-square: `2426.320647091497`
- modern LambdaCDM exact data chi-square: `2427.604184715953`
- raw improvement: `1.283537624456`

The retained point is the **lowest tested boundary endpoint**, not a continuous best-fit measurement, confidence interval, posterior constraint, or proof of global model preference.

## Data combination

- Planck 2018 low-l TT
- Planck 2018 low-l EE
- Planck high-l Plik TTTEEE-lite-native
- DESI DR2 BAO
- Pantheon+

## Quick validation

```bash
python scripts/validate_results.py
python scripts/make_figures.py
```

Independent likelihood reruns require a compatible custom CLASS build and the third-party likelihood data. Set `COBAYA_PACKAGES_PATH` before using the run scripts.

## Repository map

- `configs/`: exact public YAML configurations used for the baseline, central point, and six neighbors
- `results/raw/`: preserved stdout supplied from the completed Colab run
- `results/derived/`: machine-readable profile and AIC summaries reconstructed from the stdout
- `results/lcdm/`: exact modern LambdaCDM summary
- `results/idmdr/`: central and retained interaction summaries
- `tables/`: manuscript source tables
- `figures/`: manuscript figures
- `scripts/`: validation, plotting, minimization, reevaluation, and optional strengthening runs
- `manuscript/`: editable DOCX and submission PDF
- `class_source/`: source-provenance note and recorded hash

## Citation and release

Repository: https://github.com/parvgidiya/idmdr-modern-profile-likelihood. A Zenodo DOI will be added after the first public release is archived.


## Final tight refinement

The lowest screening endpoint at `N_idr = 0.020` was continued through `rhoend = 0.005`, `0.001`, and `0.0002`. The retained exact endpoint has `chi2_data = 2426.320647091497`, `Delta chi2_data = -1.283537624456`, and calibration-aware `Delta chi2_eff = -1.306360665032` relative to the exact LambdaCDM baseline. The local one-coordinate AIC diagnostic is `+0.693639334968`; the conservative three-coordinate diagnostic is `+4.693639334968`.
