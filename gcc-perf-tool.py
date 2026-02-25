import sys
import subprocess

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

    source_file = ""
    program_options = []
    gcc_options = []

    for i in range(1, len(sys.argv)):
        if "-" not in sys.argv[i]:
            source_file = sys.argv[i]
            gcc_options = sys.argv[i+1:]
            break

        program_options.append(sys.argv[i])

    if source_file == "":
        print("gcc-perf-tool: missing source file")
        sys.exit(1)

    # Program options
    instrumentalize = "-i" in program_options
    
    output_bin = source_file + ".out"
    for option in program_options:
        if option.startswith("-output="):
            output_bin = option.strip().split("=")[1]
            if output_bin == "":
                print("gcc-perf-tool: missing output binary name")
                sys.exit(-1)


    # Binary compilation
    print("Compiling binary...")
    
    GCC_COMMAND = ["gcc"] + gcc_options + [source_file] + ["-o"] + [output_bin]

    gcc_process = subprocess.run(GCC_COMMAND, capture_output=True)
    if gcc_process.returncode != 0:
        print("gcc-perf-tool: compilation error.\noutput:\n")
        print(gcc_process.stderr.decode().strip())
        sys.exit(gcc_process.returncode)

    # Profiling execution
    print("Profiling...")
    perf_profile(output_bin)

    if instrumentalize:
        print("Compiling with instrumentation profiler...")
        GCC_INSTRUMENTATION_COMMAND = ["gcc"] + ["-fprofile-generate"] + gcc_options + [source_file] + ["-o"] + [output_bin]
        
        gcc_instrumentation_process = subprocess.run(GCC_INSTRUMENTATION_COMMAND, capture_output=True)
        if gcc_instrumentation_process.returncode != 0:
            print("gcc-perf-tool: instrumentation compilation error.\noutput:\n")
            print(gcc_instrumentation_process.stderr.decode().strip())
            sys.exit(gcc_instrumentation_process.returncode)

        print("Generating profiling data...")
        subprocess.run(["./" + output_bin], capture_output=True)

        print("Recompiling with profiling data...")
        GCC_RECOMPILATION_COMMAND = ["gcc"] + ["-fprofile-use"] + gcc_options + [source_file] + ["-o"] + [output_bin]

        gcc_recompilation_process = subprocess.run(GCC_RECOMPILATION_COMMAND, capture_output=True)
        if gcc_recompilation_process.returncode != 0:
            print("gcc-perf-tool: recompilation error.\noutput:\n")
            print(gcc_recompilation_process.stderr.decode().strip())
            sys.exit(gcc_recompilation_process.returncode)

        perf_profile(output_bin)

main()
