#!/usr/bin/env python3
"""Run a Cobaya BOBYQA minimization from a public model YAML."""
from __future__ import annotations
import argparse, copy, os, sys, yaml
from cobaya.run import run

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('config')
    p.add_argument('--packages-path',default=os.environ.get('COBAYA_PACKAGES_PATH'))
    p.add_argument('--output',required=True)
    p.add_argument('--max-evals',type=int,default=600)
    p.add_argument('--rhoend',type=float,default=0.05)
    p.add_argument('--seed',type=int,default=261101)
    args=p.parse_args()
    if not args.packages_path:
        raise SystemExit('Set --packages-path or COBAYA_PACKAGES_PATH.')
    with open(args.config) as f: info=yaml.safe_load(f)
    info['packages_path']=args.packages_path
    info['output']=args.output
    info['force']=True
    info['sampler']={'minimize':{
        'method':'bobyqa','best_of':1,'max_evals':args.max_evals,
        'ignore_prior':False,'seed':args.seed,
        'override_bobyqa':{'rhoend':args.rhoend,'seek_global_minimum':False}}}
    run(info)
if __name__=='__main__': main()
