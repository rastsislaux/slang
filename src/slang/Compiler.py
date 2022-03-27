from slang import Utils, Interm, Macro

def compile_to_bytecode(given_src_code: str, std_path: str):
    src_code = given_src_code
    src_code = Utils.remove_comments(src_code)
    src_code = Utils.clear_decorative_symbols(src_code)
    src_code = src_code.split()
    src_code = Utils.unite_string_literals(src_code)
    tokens = Interm.parse_tokens(src_code, std_path=std_path)
    macros = Macro.generate_macros(tokens)
    return macros