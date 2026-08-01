# Reproduction guide

## Requirements

- Python 3.12
- Cobaya 3.6.2
- Py-BOBYQA 1.5.0
- a compatible custom CLASS build supporting `f_idm`, `N_idr`, `a_idm_dr`, `nindex_idm_dr`, and `idr_nature`
- installed Planck 2018, DESI DR2, and Pantheon+ likelihood data

Set:

```bash
export COBAYA_PACKAGES_PATH=/path/to/cobaya_packages
```

## Recreate the numerical workflow

1. Minimize the LambdaCDM configuration with multiple separated starts.
2. Tighten its lowest endpoint and reevaluate it with `scripts/exact_reevaluate.py`.
3. Minimize `configs/modern_idmdr/central.yaml` from the LambdaCDM endpoint.
4. Run the six neighbor YAML files from the central cosmological coordinates.
5. Exactly reevaluate every retained endpoint.
6. Assemble the profile and validate identities.

Example:

```bash
python scripts/run_minimize.py configs/modern_idmdr/N_low.yaml   --output results/reruns/N_low --rhoend 0.05 --max-evals 350
```

The large likelihood datasets are not redistributed. The custom CLASS source tree was unavailable to the packaging environment; its recorded recursive source-tree hash is supplied in `class_source/README.md`.


## Final boundary refinement

Continue the lowest screening endpoint through `rhoend = 0.005`, `0.001`, and `0.0002`, exactly reevaluating each saved stage. Select the lowest exact stage. The packaged canonical endpoint is the `rho0002` stage.
