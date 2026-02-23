import sys
import subprocess

instrumentalize = True

def perf_profile(output_bin):
    print("Profiling...")
    PERF_COMMAND = ["perf", "stat", "./" + output_bin]
    perf_process = subprocess.run(PERF_COMMAND, capture_output=True)
    if (perf_process.returncode != 0):
        print("gcc-perf-tool: profiling error. are you running with root?\noutput:\n")
        print(perf_process.stderr.decode().strip())
        sys.exit(perf_process.returncode)

    print("Profiling output:\n")
    print(perf_process.stderr.decode().strip())
    print()

def main():
    if len(sys.argv) <= 1:
        print("gcc-perf-tool: missing source file")
        sys.exit(1)

    SOURCE_FILE = sys.argv[1]

    if len(sys.argv) > 1:
        COMPILER_FLAGS = sys.argv[2:len(sys.argv)]


    # Binary compilation
    print("Compiling binary...")
    OUTPUT_BIN = SOURCE_FILE + ".out"
    GCC_COMMAND = ["gcc"] + COMPILER_FLAGS + [SOURCE_FILE] + ["-o"] + [OUTPUT_BIN]

    gcc_process = subprocess.run(GCC_COMMAND, capture_output=True)
    if gcc_process.returncode != 0:
        print("gcc-perf-tool: compilation error.\noutput:\n")
        print(gcc_process.stderr.decode().strip())
        sys.exit(gcc_process.returncode)

    # Profiling execution
    print("Profiling...")
    perf_profile(OUTPUT_BIN)

    if instrumentalize:
        print("Compiling with instrumentation profiler...")
        GCC_INSTRUMENTATION_COMMAND = ["gcc"] + ["-fprofile-generate"] + COMPILER_FLAGS + [SOURCE_FILE] + ["-o"] + [OUTPUT_BIN]
        
        gcc_instrumentation_process = subprocess.run(GCC_INSTRUMENTATION_COMMAND, capture_output=True)
        if gcc_instrumentation_process.returncode != 0:
            print("gcc-perf-tool: instrumentation compilation error.\noutput:\n")
            print(gcc_instrumentation_process.stderr.decode().strip())
            sys.exit(gcc_instrumentation_process.returncode)

        print("Generating profiling data...")
        subprocess.run(["./" + OUTPUT_BIN], capture_output=True)

        print("Recompiling with profiling data...")
        GCC_RECOMPILATION_COMMAND = ["gcc"] + ["-fprofile-use"] + COMPILER_FLAGS + [SOURCE_FILE] + ["-o"] + [OUTPUT_BIN]

        gcc_recompilation_process = subprocess.run(GCC_RECOMPILATION_COMMAND, capture_output=True)
        if gcc_recompilation_process.returncode != 0:
            print("gcc-perf-tool: recompilation error.\noutput:\n")
            print(gcc_recompilation_process.stderr.decode().strip())
            sys.exit(gcc_recompilation_process.returncode)

        perf_profile(OUTPUT_BIN)

main()