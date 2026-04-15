OpenYBR Image Format Spec v1.0
Draft - April 2026

Abstract
OpenYBR is a deterministic format using a linear pixel stream and fixed slicing. No indices, no name-driven ordering. Just strict stream order and symbolic interpretation layers.

Concepts
- Structural Layer: The raw stream and segments.
- Chaos Layer: Optional names, Cdefs, and rules.

Rules
- Stream Determinism: Raw bytes define pixel order. Period.
- No Indices: Indices are banned from the logic.
- Name Isolation: Names are just metadata. They don't touch the structure.
- Segment Purity: Segments come from fixed-size slicing only.
- Local Failure: If a segment breaks, corruption stays there.
- Decoders: Must produce 100% identical output across implementations.

File Layout
- Header: "YBR" (Must be valid or reject)
- Pixel Stream (S)
- SegmentSize (N)
- Cdef Table
- Metadata (Names, etc.)

Segmentation Logic
Segments are sliced from the stream: Segment[i] = S[i * N : (i + 1) * N]
- Size is constant for the whole file.
- Identity is purely positional.

Symbolic System (Cdef)
- Global lookup table for pixel interpretation.
- Applied post-segmentation.
- Can't change stream order or layout.

RGBAYBr Color Model
Six channels: R, G, B, A (C), Y, and Br (Brightness).
- Pixels are independent.
- Decoded per segment. No cross-segment math for base colors.

The Pipeline
1. Check "YBR" header.
2. Pull full stream.
3. Slice into segments based on N.
4. Decode channels.
5. Swap symbols via Cdef.
6. Run Chaos layer (optional, but cannot reorder segments).
7. Render in stream order.

Rendering & Corruption
- strictly render(segment) in stream order. 
- No sorting by name or hash.
- Corrupt segments = neutral fallback or skip. 
- Do NOT shift subsequent data. Keep the alignment.

Security
Keep the structural decoding separate from the chaos layer. Symbolic transforms shouldn't be able to mess with pixel ordering.

Summary
OpenYBR: Stream-first, index-free, deterministic.
