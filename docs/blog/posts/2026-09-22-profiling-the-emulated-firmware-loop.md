---
title: "Profiling the Emulated Firmware Loop Before Board Bring-Up"
date: 2026-09-22
authors:
  - abagher
categories:
  - Firmware
  - Performance
  - Simulation
---

Power management begins as a behavior problem before it becomes a battery-life number. The StackCalc firmware has to decide when to scan the matrix, wake the display path, skip an unchanged frame, save state, and return to a lower-work loop. We can exercise those decisions in the RP2350 emulator while the PCB is in fabrication.

<!-- more -->

## Counters make the loop inspectable

The simulator exposes firmware profiling symbols for boot completion, total loop count, active and sleep-loop counts, full and wake-only matrix scans, render count, display transfers, skipped display updates, average loop work, and the maximum loop-work interval. The Node service resolves those symbols from the generated firmware ELF and reads them from emulator memory alongside the 1,188-byte framebuffer.

That gives us a concrete experiment: run a named interaction sequence, inspect which wake and render paths changed, then adjust code or thresholds and repeat the same sequence. An unchanged display should not cause the same work as a changed result. A keypress should wake the work needed for a responsive next frame without leaving the loop needlessly busy afterward.

## What an emulator profile can say

It can compare control-flow choices in the compiled firmware image: whether a sequence reached the intended sleep branch, whether a matrix scan occurred, and whether an update produced a new display frame. It is also useful for finding accidental work introduced by a code change.

It cannot measure board current, regulator behavior, display inrush, battery voltage sag, or real button-to-photon latency. Those require the fabricated board, selected display, battery hardware, and an instrumented measurement setup. We publish simulator results as tuning evidence, then follow them with physical measurements rather than treating the model as a battery claim.
