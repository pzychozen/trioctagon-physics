# GM05 mathematical review

**Decision.** Accept the proposed three-loop launch, tracking result, and signed work formula with the common-offset correction to §4 in the enclosed reviewed copy. The identified donor remains open. The passive receiver assessment can use the corrected result immediately.

**What works.** For equal loop lengths and equal storage weights, the unique minimum-energy means are \(j_*=(2\alpha/3)T^\top W\). The proposed uniform impulse changes the means by \((2\alpha/3)T^\top\Delta W\). A correctly initialized carrier tracks across such a jump. Prior errors persist. The RX example in Eq. (15) explicitly changes \(W\) between jumps while the retained mean stays fixed.

At the empty Fourier launch the three signed means are proportional to \((-28501,2,28499)\). The stored-energy increase is exactly \(270750001L\alpha^2/40000000000000000\). Conjugating the preparation reverses all three signs for the same cost. An inherited internal energy donor was not identified. The steady far-field calculation uses the complete delay window and allows an \(O(r^{-4})\) remainder about the common origin of the three displaced loops.

**Correction to the reversal and offset examples.** Write \(e=(1,1,1)^\top\) and begin with \(j^-=\alpha DW^-+\beta_0e\). Reversing \(W\) gives \(j^+=-j^-+2\beta_0e\) and zero net carrier work. Bringing \(W\) to zero leaves \(3L\beta_0^2/2\) stored. Separately adding \(\beta e\) changes the energy by \(3L\beta_0\beta+3L\beta^2/2\). For example, removing a unit common offset releases \(3L/2\). The simple reversal and insertion expressions in the submission apply at zero initial offset. Its Eqs. (9), (12), and (22) already supply the general case.

**Checks.** The 62 submitted checks passed again in Linux with only the Conda environment guard and environment-name reporting adapted in a scratch copy. The six additional exact controls in GM05_REVIEW_CONTROLS.py also passed. All 93 manifest entries matched their hashes and lengths, all 94 ZIP members passed CRC, and all 24 primary-source copies matched their recorded SHA-256 and Git blob identities. The separate GM05 Markdown submissions match the corresponding archived files. The preserved GM04 archive matches its previously reviewed hash.

**Handoff.** The reviewed Markdown copy contains only the §4 wording correction. Place it alongside the original GM05 derivation so its relative source links resolve. Use this note and the included controls with the existing package.

