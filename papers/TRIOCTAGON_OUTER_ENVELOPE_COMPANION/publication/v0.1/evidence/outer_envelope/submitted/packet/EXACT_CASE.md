# Exact case — source-defined outer exits; A–B interval only

This is a GPT transcription of the written geometry, to be reconciled with the original inventory. It is not a replacement source file.

Take width w=1 for calculation and restore common scaling at the end. Let h=(sqrt(2)-1)/2 and global centre o=(0,sqrt(3)/6,0). The local ordered octagon is

`(-1/2,-h), (-h,-1/2), (h,-1/2), (1/2,-h), (1/2,h), (h,1/2), (-h,1/2), (-1/2,h)`.

The three global fold maps are

\[
F_1(u,z)=(-1/4-u/2,\sqrt3/4-\sqrt3u/2,z),
\quad F_2(u,z)=(u,0,z),
\quad F_3(u,z)=(1/4-u/2,\sqrt3/4+\sqrt3u/2,z).
\]

Apply them in panel order, identify exactly equal vertices, and subtract o. The inherited material face cycles are

```
P1: (0,1,2,3,4,5,6,7)
P2: (3,8,9,10,11,12,13,4)
P3: (10,14,15,0,7,16,17,11)
```

The lexicographic undirected edges, whose increasing index order gives the plus direction, are

```
E01 (0,1)    E02 (0,7)    E03 (0,15)
E04 (1,2)    E05 (2,3)    E06 (3,4)
E07 (3,8)    E08 (4,5)    E09 (4,13)
E10 (5,6)    E11 (6,7)    E12 (7,16)
E13 (8,9)    E14 (9,10)   E15 (10,11)
E16 (10,14)  E17 (11,12)  E18 (11,17)
E19 (12,13)  E20 (14,15)  E21 (16,17)
```

For centred endpoints v_i,v_j:

\[
m_e=(v_i+v_j)/2,\quad u_e=(v_j-v_i)/(2h),\quad
p_{e,\pm}(x)=m_e\pm x u_e,\quad R/w=\sqrt{1/3+x^2}.
\]

Here x=t/w and all p coordinates are normalized by width. There are 42 branch records; at endpoints several records have the same position.

**Authorized interval:** `[1/2,(1+sqrt(2))/2]`.  
**Proposed internal candidate:** `x*=3h=(3sqrt(2)-3)/2`.  
**Inherited comparison radius:** `rho/w=sqrt(13/12-sqrt(2)/2)` below A.  
**H(x):** the convex hull of the unique positions of the 42 records. It is a mathematical enclosure, not an adopted material boundary.

Preserve both hands by common orthogonal reflection where applicable; do not create separate cases by changing indexing or handedness conventions. A single-hand exact proof transfers under that reflection when the entire construction is reflected.
