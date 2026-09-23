---
title: "Why RPN Needs an Ecosystem, Not Another Retro Replica"
date: 2026-09-22
authors:
  - abagher
categories:
  - Education
  - Design
  - RPN
---

RPN calculators already exist. StackCalc is not a nostalgia project trying to recreate a familiar beige machine. The gap we see is a learning path: a way to move from a familiar screen to a physical instrument while understanding what the stack is doing.

That is why StackCalc joins the current iPhone and Apple Watch apps, a shared calculator core, Learning Lab prototypes, and a planned RP2350 handheld around the same calculation behavior. The connection is semantic, not cosmetic.

<!-- more -->

## The problem is legible state

RPN turns a calculation into small, checkable actions: place values on the stack, then apply an operation. It can remove parenthesis entry, but the interface must make state legible. A learner needs to see the working value, know when ENTER commits it, and understand what an operation will consume.

Established RPN calculators are excellent instruments for people who already have those habits. StackCalc investigates the earlier step: what should a learner be able to see, touch, and predict before pressing the next key?

## Four connected surfaces

- **A shared RPN core** keeps operation meaning and calculator state consistent across interfaces.
- **The Apple Watch and iPhone/iPad apps** let us study compact controls and display hierarchy on devices a learner already knows.
- **The Learning Lab** makes amounts, stack positions, postfix expression order, and coordinate relationships tangible.
- **The RP2350 handheld design** carries that same interaction model into a dedicated physical calculator. Its KiCad PCB is in fabrication; an assembled, powered board is the next physical milestone.

The design rule is to keep meaning stable while changing the surface. A fraction tower, a stack tile, a watch interaction, and a physical key should all point to the same operation instead of asking the learner to memorize a new model on every device.

## What comes next

The next step is to put the artifacts in people’s hands: printable teaching materials, physical prototypes, and educator sessions that improve the activities. The current mechanical calculator is an unpowered four-part printed prototype; the companion app is available on the [App Store](https://apps.apple.com/app/id6801788040).
