from cx_Freeze import setup, Executable


include_files = ["icon.ico", "./configs", "./model"]
excludes = ["tensorflow"]
target = Executable(script="./engine.py", base="Win32GUI")


setup(
    name="App",
    version="1.0",
    description="App description.",
    author="JS Club - Team 3",
    options={"build_exe": {"include_files": include_files, "excludes": excludes}},
    executables=[target],
)

# py setup.py build
