# E01 — raw-byte source hash recording

The manuscript mathematics, layout and table bytes are accepted unchanged. This fix concerns only the current document-check helper.

The original helper hashes UTF-8 text after universal-newline decoding. For `tables/certificate.tex`, that turns CRLF into LF. Its normalized-text hash is `3425caeb60e28c2f901ae5f8a09c7e1e1f987abcb67acd2b1434ffdd07dd60e2`; the actual raw-byte hash is `b4e92700ab9024be91c88891bdb982b27f9424ec330ad33bf635ffdf84968b56`, already correctly recorded by the build receipt and archive manifests.

Replace the helper in a new finalization copy with `helpers/verify_document.py` from this corrections directory. Its SHA-256 is `2321b16b6d38f73d3d87b119443e92613eaba7da098a97ef7f9e7c4c44fbdc1c`. The exact one-site diff is supplied. The replacement uses raw bytes and labels their hash basis explicitly.

The actual corrected expression was evaluated against all three source files and matches their build-receipt hashes. Its syntax and inverse replacement were checked. The entire helper was not run and the PDF was not rebuilt for this documentary patch. The original submitted files are unchanged. During publication, adapt the existing pending-status metadata assertion to the legitimately authorized edition and generate new current document records. Do not modify old evidence records or normalize table newlines.

No scientific replay, parameter change, manuscript-equation change or new research is involved.
