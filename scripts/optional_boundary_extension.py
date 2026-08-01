#!/usr/bin/env python3
"""Generate YAML variants for optional lower-N_idr boundary tests."""
from pathlib import Path
import copy, yaml
root=Path(__file__).resolve().parents[1]
base=yaml.safe_load((root/'configs/modern_idmdr/N_low.yaml').read_text())
out=root/'configs/modern_idmdr/optional_boundary'; out.mkdir(exist_ok=True)
for value in [0.015,0.010,0.005]:
    info=copy.deepcopy(base); info['theory']['classy']['extra_args']['N_idr']=value
    (out/f'N_idr_{value:.3f}.yaml').write_text(yaml.safe_dump(info,sort_keys=False))
print(out)
