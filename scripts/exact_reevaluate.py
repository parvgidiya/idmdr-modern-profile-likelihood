#!/usr/bin/env python3
"""Exactly reevaluate a saved parameter point under a model YAML."""
from __future__ import annotations
import argparse, json, os, yaml, numpy as np
from cobaya.model import get_model

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('config')
    p.add_argument('point_json',help='JSON mapping of sampled parameter names to values')
    p.add_argument('--packages-path',default=os.environ.get('COBAYA_PACKAGES_PATH'))
    p.add_argument('--out',required=True)
    args=p.parse_args()
    if not args.packages_path: raise SystemExit('Set --packages-path or COBAYA_PACKAGES_PATH.')
    with open(args.config) as f: info=yaml.safe_load(f)
    with open(args.point_json) as f: point=json.load(f)
    info['packages_path']=args.packages_path
    for key in ['sampler','output','resume','force']: info.pop(key,None)
    model=get_model(info)
    try:
        try: post=model.logposterior(point,cached=False)
        except TypeError: post=model.logposterior(point)
        names=list(model.likelihood)
        loglikes=np.asarray(post.loglikes,dtype=float)
        record={'sampled_parameters':point,'chi2':float(-2*loglikes.sum()),
                'minuslogpost':float(-post.logpost),
                'components':[{'likelihood':str(n),'loglike':float(l),'chi2':float(-2*l)} for n,l in zip(names,loglikes)]}
        with open(args.out,'w') as f: json.dump(record,f,indent=2)
    finally:
        try: model.close()
        except Exception: pass
if __name__=='__main__': main()
