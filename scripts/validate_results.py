#!/usr/bin/env python3
import json, math
from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
p=pd.read_csv(root/'results/derived/modern_idmdr_seven_point_profile.csv')
l=json.loads((root/'results/lcdm/lcdm_exact_summary.json').read_text())
f=json.loads((root/'results/idmdr/final/modern_idmdr_final_best_endpoint.json').read_text())
assert len(p)==7
assert p.iloc[0]['profile']=='N_low_refined'
assert math.isclose(float(p.iloc[0]['exact_chi2']),2426.320647091497,abs_tol=1e-9)
assert math.isclose(float(l['chi2_data']),2427.604184715953124,abs_tol=1e-9)
assert math.isclose(sum(l['components'].values()),l['chi2_data'],abs_tol=2e-9)
assert math.isclose(float(f['exact_statistics']['delta_chi2_data_idmdr_minus_lcdm']),-1.283537624456,abs_tol=1e-9)
assert math.isclose(float(f['exact_statistics']['delta_chi2_eff_idmdr_minus_lcdm']),-1.306360665032,abs_tol=1e-9)
print('All packaged numerical identities pass.')
