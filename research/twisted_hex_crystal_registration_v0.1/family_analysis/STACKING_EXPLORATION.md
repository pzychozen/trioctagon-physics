# One bounded axial repeat test

The single declared pitch is the existing full apex height: physical dz=1,
canonical dz=2. Copies keep the same principal axis and no lateral offset.
This is a bounded geometric test of one simple full-height stacking rule,
not an optimization over pitches or a proposed crystal lattice.

The three cases tested are direct translation; translation with a C3
rotation; and an alternating opposite-hand copy. No material, force,
energy, atomic or runtime interpretation is assigned.

## Exact separating-plane argument

A copy occupies the slab [-1/2,1/2]. Its next neighbor occupies
[1/2,3/2]. They can meet only at z=1/2, where each surface has only three
apex tips. The lower copy's upper tips have radius r; the upper copy's
lower tips have radius sqrt(r^2+u^2). Their squared-radius difference is
exactly u^2, irrespective of hand. Thus no contact is possible for u>0.
At zero the aligned triangular tip sets coincide in exactly three points.
No triangles overlap over a positive area; there is no intersection away
from those permitted isolated zero-state tips.

The ring levels also fail to coincide: pitch 1 is not their separation
2h=s. Each boundary loop includes ring vertices as well as apex vertices;
isolated apex contact does not identify either full six-edge loop. No
joined annular surface is produced, even at zero.

| Test | u>0 | u=0 |
|---|---|---|
| Vertex coincidence | None | Three apex points |
| Ring coincidence | None | None |
| Boundary-loop matching | None | None |
| Triangle intersection between copies | None | Isolated apex contacts only |
| Joining along a boundary without deformation | No | No |

A C3 rotation makes exactly the same copy, so translation+C3 gives the
same result. Identical copies as a disjoint set formally have period 1;
the combination with C3 is a tautological screw symmetry of that copy
set. An alternating sequence of opposite-hand surfaces has translation
period 2. These periodic arrangements do not prove a joining rule or
select a lattice, pitch, magnitude or handedness.

```text
TESTED_PITCH_PHYSICAL = 1
TESTED_PITCH_CANONICAL = 2
SIMPLE_AXIAL_REPEAT_FOUND = NO, FOR A JOINED REPEAT AT THIS PITCH
STACKING_RESULT = NO_SIMPLE_AXIAL_REPEAT_SELECTED
OTHER_PITCHES_OR_LATERAL_OFFSETS = NOT_TESTED
FURTHER_FORM_SEARCH = CLOSED
```

No negative claim about every conceivable stacking follows. No additional
repeat search is authorized by this result.
