# Embedded Swift firmware

StackCalc's firmware source targets the **Raspberry Pi Pico 2 / RP2350** using Embedded Swift and a C hardware layer. It shares calculator logic and the bitmap interface with `RPNCore`.

The pictured physical calculator is an **unpowered mechanical prototype**. Board fabrication and integration are still in progress. The architecture below describes the current source, not measured performance of an assembled product. The public mechanical download does not include firmware source or a flashable release.

## Architecture

| Source component | Responsibility |
| --- | --- |
| `Main.swift` | Calculator event loop, input dispatch, display updates and continuous memory |
| `hardware_wrapper.c` / `BridgingHeader.h` | Pico SDK boundary for GPIO, SPI, time and flash |
| `RPNCore` | Shared calculator operations, key mapping, bitmap rendering and tutorials |
| `CMakeLists.txt` | Embedded build configuration; excludes app-only plotting |
| `Simulator/` | Browser display and transport around the emulated firmware image |

The physical design uses the current **37-key layout**. Source sharing supports consistent behavior, but cross-platform parity must be checked with matching operations and state; it is not a blanket bit-for-bit guarantee for every feature.

## Display and input

The logical display is **132×65 pixels**, with **1,188 bytes** arranged as nine pages of 132 columns. The final page has one visible row. The hardware wrapper currently configures **8 MHz SPI** and sends each page with blocking writes. It does not implement the previously described DMA or establish a tear-free display claim. Module/controller identity and physical edge visibility still need checking against the installed specimen and BOM.

The GPIO scanner samples the matrix; the Swift loop debounces changed input before dispatching the corresponding operation. The active loop uses a 10 ms sleep interval. In the source's sleeping state, the LCD output is disabled, scanning is restricted to **C/ON**, and the loop uses a 100 ms interval. Other keys do not wake that state. These source intervals are not measured touch-to-display latency or battery-life results.

## Continuous memory

The flash implementation alternates between two slots, each eight flash sectors, at the end of flash. It validates payloads with an **FNV-1a checksum** and selects the newer valid sequence. It also includes migration from the older, smaller slot layout.

This replaces the earlier description of two 4 KB sectors and CRC32. Power-loss recovery, flash endurance and retention must be evaluated on the matching board. The firmware uses allocated buffers and Swift collections; **zero heap allocation is not a current claim**.

## Build and inspection

These commands are for a source checkout with the configured Embedded Swift toolchain, Pico SDK, ARM compiler, CMake and Ninja. The current local Pico SDK checkout is based on 2.3.0. The build script accepts `WATCHCALC_SWIFT_TOOLCHAIN` for an external Swift toolchain and otherwise uses `Firmware/toolchains/swift`.

Run from the repository root:

```sh
# Hardware UF2
Firmware/compile_firmware.sh hardware

# Instrumented hardware build
Firmware/compile_firmware.sh profile

# Firmware image for the localhost emulator
Firmware/compile_firmware.sh emulator
node Firmware/Simulator/server.js

# ELF sizing and optional live hardware counters
python3 Firmware/profile_power_memory.py
```

Each build replaces `Firmware/build`; run the variants sequentially. The hardware output is `Firmware/build/WatchCalcFirmware.uf2`, copied to `Hardware/output/WatchCalc32_Manufacturing/Firmware_Files/WatchCalcFirmware_RP2350.uf2`. The profile variant uses the `_Profile.uf2` suffix in that export directory. An emulator build is for the simulator, not for flashing a board.

## Physical verification still required

A powered board is needed to verify cold startup, input-to-display timing, display edges, memory recovery, current consumption and battery life. The previous sub-15 ms boot, sub-two-second flashing and multi-month battery statements were not qualified measurements and are withdrawn.

When a board-specific firmware release is available, its instructions must identify the board revision, matching UF2, USB/BOOTSEL access and recovery procedure. Do not infer those details from the mechanical prototype photos.

See the [hardware build and capability reference](hardware.md) for the current mechanical kit and its qualification limits.
