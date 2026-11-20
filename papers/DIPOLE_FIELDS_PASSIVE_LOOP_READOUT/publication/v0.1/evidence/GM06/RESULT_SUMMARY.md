# GM06 result for review

**Yes: an added passive loop sensor can distinguish opposite source circulations.** The existing equations do not yet turn that reading into a response of a second native triad.

The proposed sensor integrates signed tangent components of the existing C6 vector observation V around one geometrically allowed receiving circle. Dividing by its area gives a finite-area component of curl V. Its radius stays equal to the geometric circle radius; it is not silently shrunk to a point.

Two tests pass:

1. **Coaxial source and receiving circles.** The vector observation at the receiving circle's center is exactly zero, while the contour reading has the source's sign for every positive pair of radii and nonzero axial separation. Reversing the source or the measurement orientation reverses the reading. The proof uses the exact finite-loop kernel.
2. **Reviewed GM05 native launch.** All three source circles retain their distinct centers. A registered receiving copy with circle normal \(e_y\), circle center \(O+Re_z\) and radius \(0.53645209718\ldots\,w\) distinguishes the Fourier launch and its conjugate for every \(R\ge100w\). The conservative proved error is less than one third of the nonzero leading component. At \(R=100w\), 1,024 additional exact contour samples also suffice by a quadrature-error bound.

**A center distinction matters:** the receiving circle's center is displaced from the body center where the original module probe is defined. The coaxial zero reading refers to the circle center. The body-center reading can already be nonzero.

The receiver audit also finds that WT's three upper arcs join into one closed six-edge path and its three lower arcs into another. Its current equations do not integrate readings around either oriented path. Three available loop normals have rank two, and their centers differ, so no full-vector reconstruction is claimed.

The complete source-to-contour delay window is required after a jump. An active native input law, reciprocal work law, physical magnetic calibration and GM05's internal donor remain separate, unprovided choices.

**Verification:** 59 checks passed in Command Prompt with conda torment. These comprise 28 exact algebra checks, 28 quadrature checks, one bound evaluation, the six supplied GM05 review controls grouped as one check, and one grouped verification of all 24 primary-source identities. Written arguments establish the continuum sign and distance range. Original GM04/GM05 evidence and the accepted manual remain unchanged; the three GM05 review files were added alongside its original derivation. No commit, push or production change was made.

[Derivation and proofs](GM06_DERIVATIONS.md) · [Source map](SOURCE_MAP.md) · [Check results](CHECK_RESULTS.json) · [Review receipt](REVIEW_RECEIPT.json)
