#!/usr/bin/env python3
"""Extract the first data row from a Cobaya .minimum.txt file."""
from __future__ import annotations
import argparse, json

def parse(path):
    header=None
    for raw in open(path):
        line=raw.strip()
        if not line: continue
        if line.startswith('#') and 'minuslogpost' in line and 'chi2' in line:
            header=line.lstrip('#').strip().split(); continue
        if header is not None and not line.startswith('#'):
            vals=line.split()
            if len(vals)!=len(header): raise ValueError('Header/data length mismatch')
            out={}
            for k,v in zip(header,vals):
                try: out[k]=float(v)
                except ValueError: out[k]=v
            return out
    raise ValueError('No readable row found')

def main():
    p=argparse.ArgumentParser(); p.add_argument('minimum'); p.add_argument('--out',required=True); a=p.parse_args()
    with open(a.out,'w') as f: json.dump(parse(a.minimum),f,indent=2)
if __name__=='__main__': main()
