#!/usr/bin/env python3
"""Validate final figure and source-table availability."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=[
 'tables/seven_point_profile.csv','tables/endpoint_comparison.csv','tables/aic_sensitivity.csv',
 'tables/likelihood_component_comparison_exact.csv',
 'results/idmdr/final/modern_idmdr_N_low_refinement_history.csv'
]
for rel in required:
    if not (root/rel).is_file(): raise SystemExit(f'Missing {rel}')
figs=list((root/'figures').glob('*final_refined.png'))
if len(figs)<7: raise SystemExit('Expected seven final refined figures')
print('Final source tables and figures are present.')
