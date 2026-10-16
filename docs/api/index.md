---
title: "Agent & Developer API Reference | OpenAPI 3.1 & JSON Rubrics"
description: "View-only OpenAPI 3.1 specification and machine-readable JSON datasets for StackCalc SC-32 and SC-6 calculators. Enables AI agents and tools to query button rubrics, stack deltas, and keystrokes."
---

# Agent &amp; Developer API Reference
## View-Only OpenAPI 3.1 Specification &amp; Structured JSON Datasets

<div class="te-viewport-header mb-6">
  <span class="te-viewport-sku">MACHINE-READABLE SPECIFICATION // AGENT GATEWAY</span>
  <span class="te-viewport-status text-emerald-400">● OPENAPI 3.1 &bull; JSON &bull; ZERO AUTH VIEW-ONLY</span>
</div>

<div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8 font-mono text-xs">
  <a href="openapi.json" class="p-4 rounded-xl bg-slate-900 border border-cyan-500/30 hover:border-cyan-400 transition flex flex-col justify-between group">
    <div>
      <span class="text-cyan-400 font-bold uppercase block mb-1">SPECIFICATION</span>
      <strong class="text-white text-sm">OpenAPI 3.1 (JSON)</strong>
      <p class="text-slate-400 text-[11px] mt-1">Full schema for agents and tools.</p>
    </div>
    <span class="text-cyan-400 font-bold mt-3">&darr; openapi.json</span>
  </a>

  <a href="openapi.yaml" class="p-4 rounded-xl bg-slate-900 border border-emerald-500/30 hover:border-emerald-400 transition flex flex-col justify-between group">
    <div>
      <span class="text-emerald-400 font-bold uppercase block mb-1">SPECIFICATION</span>
      <strong class="text-white text-sm">OpenAPI 3.1 (YAML)</strong>
      <p class="text-slate-400 text-[11px] mt-1">Human-friendly schema format.</p>
    </div>
    <span class="text-emerald-400 font-bold mt-3">&darr; openapi.yaml</span>
  </a>

  <a href="sc32-reference.json" class="p-4 rounded-xl bg-slate-900 border border-amber-500/30 hover:border-amber-400 transition flex flex-col justify-between group">
    <div>
      <span class="text-amber-400 font-bold uppercase block mb-1">DATASET</span>
      <strong class="text-white text-sm">SC-32 Reference (JSON)</strong>
      <p class="text-slate-400 text-[11px] mt-1">60+ operations, shifts &amp; stack deltas.</p>
    </div>
    <span class="text-amber-400 font-bold mt-3">&darr; sc32-reference.json</span>
  </a>

  <a href="sc6-reference.json" class="p-4 rounded-xl bg-slate-900 border border-purple-500/30 hover:border-purple-400 transition flex flex-col justify-between group">
    <div>
      <span class="text-purple-400 font-bold uppercase block mb-1">DATASET</span>
      <strong class="text-white text-sm">SC-6 Reference (JSON)</strong>
      <p class="text-slate-400 text-[11px] mt-1">28 keys, modes, and superpowers.</p>
    </div>
    <span class="text-purple-400 font-bold mt-3">&darr; sc6-reference.json</span>
  </a>
</div>

---

## 1. Overview for Autonomous AI Agents

To support modern agentic coding workflows, calculator verification, and LLM-assisted curriculum generation, StackCalc publishes **view-only, machine-readable specifications** of its hardware architectures, button rubrics, and operational state machines.

Agents can query these endpoints to:
1. **Look up exact keystrokes:** Determine primary, yellow (`[f]`), and blue (`[g]`) shift sequences without hallucination.
2. **Verify stack transitions ($\Delta \text{Stack}$):** Inspect how $X, Y, Z, T$ registers mutate before and after an operation (such as `[÷R]`, `[REP]`, or `[SOLVE]`).
3. **Inspect mode parameters:** Understand the active visual mode (e.g. Ten-Frame `[▦]`, Clock `[🕒]`, or 4-Stack XYZT).

---

## 2. Core API Endpoints

The API is structured as a lightweight, read-only resource model:

<div class="te-table-wrapper">
| HTTP Method | Route | Description |
| :--- | :--- | :--- |
| `GET` | `/v1/models` | List all supported calculator models (`sc32`, `sc6`) with summaries. |
| `GET` | `/v1/models/{modelId}` | Retrieve full hardware architecture, display parameters, and register sets. |
| `GET` | `/v1/models/{modelId}/operations` | Query all button operations with optional `?subsystem=` filtering. |
| `GET` | `/v1/models/{modelId}/operations/{opId}` | Lookup a specific operation by mnemonic (e.g. `intDiv`, `rep`, `lastx`, `plot`, `poly`). |
| `GET` | `/v1/models/{modelId}/modes` | List operational stack modes and tactile visual modes. |
</div>

---

## 3. Schema Architecture: The `CalculatorOperation` Object

Every operation in the StackCalc ecosystem is defined with deterministic stack transformation semantics:

```json
{
  "id": "intDiv",
  "name": "Integer Division with Remainder",
  "key": "÷",
  "shift": "blue",
  "legend": "÷R",
  "subsystem": "Core Stack & Arithmetic",
  "description": "Performs integer division of Y by X. Places integer quotient in X and integer remainder in Y simultaneously. Divisor saved in LAST X.",
  "stack_delta": {
    "before": {
      "T": "t",
      "Z": "z",
      "Y": "dividend",
      "X": "divisor"
    },
    "after": {
      "T": "t",
      "Z": "z",
      "Y": "remainder",
      "X": "quotient"
    }
  },
  "example": "23 [ENTER] 4 [g] [÷R] -> Y: 3.0000 (R), X: 5.0000 (Q)"
}
```

---

## 4. Example: Agent Keystroke Retrieval

An agent assisting a student with a Texas UIL word problem or elementary division remainder can parse `docs/api/sc32-reference.json` or `docs/api/sc6-reference.json` directly to construct valid keystroke chains:

```python
import json

with open("docs/api/sc32-reference.json") as f:
    sc32 = json.load(f)

# Find operation
op = next(o for o in sc32["operations"] if o["id"] == "intDiv")
print(f"Key: {op['key']}, Shift: {op['shift']}, Legend: {op.get('legend')}")
# Output: Key: ÷, Shift: blue, Legend: ÷R
```
