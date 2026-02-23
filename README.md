# gcc-perf-tool
A small tool to ease GCC optimization flag profiling with perf.

## Overview
This tool allows you to easily profile GCC-compiled binaries with optimization flags.

## Usage
The general usage is the following:

```bash
$ sudo python3 [program-options] <source_file> [gcc-options]
```

Superuser access is necesary to execute `perf` properly.

### Program options
These options change the behaviour of this tool.
- `-i`: Does the regular profiling, but then recompiles the binary with instrumentation optimization and profiles it so both results can be compared.

- `-output=<name>`: The compiled binary will have the name specified in this option.

### GCC options
The options specified after the source file will be passed into GCC.

## Requirements
This tool will execute instances of `perf` and `gcc`. Having these programs installed on your system is required.