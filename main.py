import os

default = ""
speed_flag = "-O"
opt_size_flag = "-Osize"
debug_flag = "-Onone"

def generate_swift_sil(file_path: str, flag: str):
    swift_file_path = file_path
    sil_file_path = "build/" + file_path.replace(".swift", f"-{flag}.sil")

    command = f"swiftc {flag} {swift_file_path} -emit-sil -o {sil_file_path}"
    os.system(command)
    return sil_file_path

def compare_swift_sil(file_path_one: str, file_path_two: str, flag: str):
    command = f"diff {file_path_one} {file_path_two}"
    os.system(command)

for flag in [opt_size_flag]:
    print(f"Comparing {flag}")
    none_final = generate_swift_sil("hello-none-final.swift", flag)
    final = generate_swift_sil("hello-final.swift", flag)
    compare_swift_sil(none_final, final, flag)
