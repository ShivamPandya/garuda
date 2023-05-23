def get_interpreter(filepath:str, compile:bool=False) -> tuple[list, str, bool]:
    
    extension = filepath.split(".")[-1]
    compiled = {"rs"}
    
    if extension in compiled:
        compile = True

    langs = {"js": "node",
             "py": "python",
             "rb": "ruby",
             "rs": "rustc"}
    
    interpreter: list = langs[extension].split()

    return (interpreter, filepath, compile)
