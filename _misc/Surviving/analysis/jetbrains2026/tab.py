import sys, pandas as pd, numpy as np, collections
df=pd.read_csv(sys.argv[1],dtype=str,keep_default_na=False,encoding='utf-8')
df['weight']=pd.to_numeric(df['weight'],errors='coerce')
out=open(sys.argv[2],'w')
P=lambda *a: print(*a,file=out)
P('rows',len(df),'weight sum',df.weight.sum(),'min',df.weight.min(),'max',df.weight.max(),'missing w',df.weight.isna().sum())
groups=collections.OrderedDict()
for c in df.columns:
    groups.setdefault(c.split('::')[0],[]).append(c)
def single(c,label=None):
    s=df[c]; m=s!=''
    n=m.sum(); 
    if n==0: P('##',c,'EMPTY'); return
    w=df.weight[m]; 
    u=s[m].value_counts()
    ww=df[m].groupby(c).weight.sum()/w.sum()
    P(f'## {label or c} | n={n}')
    for k in u.index:
        P(f'   {ww[k]*100:5.1f}w {u[k]/n*100:5.1f}u {u[k]:6d}  {k}')
for g,cs in groups.items():
    if g in('response_id','weight'): continue
    if len(cs)==1 and '::' not in cs[0]:
        if g=='country':
            single(g); continue
        single(g); continue
    # checkbox or table?
    ischeck=all(set(df[c].unique())-{''} <= {c.split('::',1)[1]} for c in cs)
    if ischeck:
        any_=(df[cs]!='').any(axis=1); n=any_.sum(); W=df.weight[any_].sum()
        P(f'## [MULTI] {g} | n={n}')
        res=[]
        for c in cs:
            m=df[c]!=''
            res.append((df.weight[m].sum()/W*100, m.sum()/n*100, m.sum(), c.split('::',1)[1]))
        for r in sorted(res,reverse=True): P(f'   {r[0]:5.1f}w {r[1]:5.1f}u {r[2]:6d}  {r[3]}')
    else:
        P(f'## [TABLE] {g}')
        for c in cs: single(c)
out.close()
