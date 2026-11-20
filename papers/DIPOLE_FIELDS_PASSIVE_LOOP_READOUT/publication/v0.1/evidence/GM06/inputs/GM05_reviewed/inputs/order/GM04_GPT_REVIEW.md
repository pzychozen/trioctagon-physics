# GM04 review · Magnetic-field transfer between two triads

**Disposition.** GM04 passes mathematical review as submitted. It answers the source, field-pattern and receiver questions in the work order. No mathematical correction is required.

| Question | Finding | Derivation |
|---|---|---|
| What spatial pattern does the loop produce? | For a steady, uniformly preloaded loop with matching history, the curl of its exterior vector observation has the signed dipole angular pattern. The leading term decays as the inverse cube of distance from the circle center. The absolute error decays as the inverse fifth power, uniformly in direction. | Eqs. (6)–(15) |
| Can a native update generate that loop moment? | The Fourier example takes the native moment candidate from zero to nonzero in one step. C1 and RX conserve mean circulation, so the empty loop still has zero circular-current moment. Independently, two equal-intensity native states with opposite moments give the same zero port input. | Eqs. (16)–(18), (22)–(23) |
| What does the loaded transport extension change? | WT allows incoming waves to change the mean. With the carrier, lines and receivers initially empty, the mean stays zero until at least the earliest possible round trip. Its later value depends on the return history. | Eqs. (24)–(26) |
| What can a second triad detect? | On the loop axis the steady preload and the empty carrier give exactly the same point observation. Their curls differ. Off the axis the existing vector observation can distinguish the sign of the preload. The inspected source-to-receiver equations supply no input that makes a second native triad respond to the curl. | Eqs. (7), (26), (30)–(32) |
| How does the three-circle geometry enter? | The three ordered normals equal the columns of Paper G’s attachment matrix, with the stated axial reflection sign. The retained evolution supplies one dynamical circle. Assigning three circulations to track a general native moment would require an additional source law. | Eqs. (27)–(29) |

**Independent field check.** The oriented loop integral gives zero vector observation on its axis. Differentiating before restricting to that axis gives a curl along the loop normal, of signed magnitude \(g_o j_0 a^2/[2(a^2+z^2)^{3/2}]\). At large axial distance the first finite-radius correction is \(-3g_o j_0a^4/(4|z|^5)\). Thus the fifth-power correction actually occurs for a nonzero preload. The disk-integral argument establishes the uniform bound in Eq. (15) for all directions.

**Verification.** All 78 submitted checks passed again in the independent Linux review environment. The scratch replay adapted only the Windows Conda environment guard and environment-name reporting. It used the submitted mathematical checks unchanged. The suite comprised 48 symbolic checks, 27 quadrature checks, one finite-difference check and two byte-identity checks. The archive contained 65 readable members. All 64 entries listed in its manifest matched their byte counts and SHA-256 hashes. All 20 packaged primary-source files matched their recorded SHA-256 and Git blob identities. Both separately submitted Markdown documents matched their archived copies byte for byte.

**Reviewed package.** GM04_NATIVE_MAGNETIC_FIELD_TRANSFER_20261120_REVIEW_PACKAGE.zip  
SHA-256 `316454fbb72004892a464440c2aa27ea452d2282b7eaac25303f57da89c8b666`
