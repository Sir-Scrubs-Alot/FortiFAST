import cx_Freeze

executables = [cx_Freeze.Executable("FortiFast.py")]

cx_Freeze.setup(
    name="Your Script",
    options={"build_exe": {"packages": [], "include_files": []}},
    executables=executables
)
