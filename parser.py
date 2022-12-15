import main
import colorama
from colorama import Fore

token_list = []
count_position = 0
count_base = 0
error_aux = []
max_base = 0
list_id = []

def appendId(token):
    if( token[1] in list_id):
        print(Fore.RED + "Token '" + str(token[1]) + "' already exists. Redeclaration in line: " + str(token[2]))
        exit(1)
    list_id.append(token[1])

def update_max_base(base):
    global max_base
    if(max_base < base):
        max_base = base


# var_decl ____________________________________________________________
def var_decl():
    global count_position
    global list_id
    base = count_position
    update_max_base(base)
    if match("ID", isDecl=True) and var_decl1():
        appendId(token_list[base])
        return True
    else:
        count_position = base
    return False


def var_decl1():
    global count_position
    base = count_position
    update_max_base(base)
    if match("[") and match("intcon") and match("]"):
        return True
    else:
        count_position = base
    return True


# end var_decl ____________________________________________________________

# parm_types ____________________________________________________________

def parm_types():
    global count_position
    base = count_position
    update_max_base(base)
    if match('void'):
        return True
    else:
        count_position = base
    if _type() and match("ID", isDecl=True) and match("[") and match("]") and parm_types2():
        appendId(token_list[base + 1])
        return True
    else:
        count_position = base
    if _type() and match("ID", isDecl=True) and parm_types2():
        appendId(token_list[base + 1])
        return True
    else:
        count_position = base

    return False


def parm_types2():
    global count_position
    base = count_position
    update_max_base(base)
    if match(',') and parm_types():
        return True
    else:
        count_position = base
    return True


# end parm_types ____________________________________________________________

def _type():
    global count_position
    base = count_position
    update_max_base(base)
    if match("int") or match("char"):
        return True
    else:
        count_position = base
    return False


# dcl ____________________________________________________________
def dcl():
    global count_position
    base = count_position
    update_max_base(base)
    if _type() and dcl1():
        return True
    else:
        count_position = base
    if dcl5():
        return True
    else:
        count_position = base
    if match('void') and dcl3() and dcl4():
        return True
    else:
        count_position = base
    return False


def dcl1():
    global count_position
    base = count_position
    update_max_base(base)
    if var_decl() and dcl2():
        return True
    else:
        count_position = base
    if dcl3() and dcl4():
        return True
    else:
        count_position = base
    return True


def dcl2():
    global count_position
    base = count_position
    update_max_base(base)
    if match(',') and var_decl():
        return True
    else:
        count_position = base
    return True


def dcl3():
    global count_position
    base = count_position
    update_max_base(base)
    if match("ID") and match("(") and parm_types() and match(")"):
        return True
    else:
        count_position = base
    return False


def dcl4():
    global count_position
    base = count_position
    update_max_base(base)
    if match(',') and dcl3():
        return True
    else:
        count_position = base
    return True


def dcl5():
    global count_position
    base = count_position
    update_max_base(base)
    if match('extern') and dcl():
        return True
    else:
        count_position = base
    return False


# end_dcl ____________________________________________________________

# func ____________________________________________________________
def func():
    global count_position
    base = count_position
    update_max_base(base)
    if _type() and func1():
        return True
    else:
        count_position = base
    if match('void') and func1():
        return True
    else:
        count_position = base
    return False


def func1():
    global count_position
    base = count_position
    update_max_base(base)
    if match("ID") and match("(") and parm_types() and match(")") and match("{") and func2() and func4() and match("}"):
        return True
    else:
        count_position = base
    return False


def func2():
    global count_position
    base = count_position
    update_max_base(base)
    if _type() and var_decl() and func3() and match(';') and func2():
        return True
    else:
        count_position = base
    return True


def func3():
    global count_position
    base = count_position
    update_max_base(base)
    if match(',') and var_decl() and func3():
        return True
    else:
        count_position = base
    return True


def func4():
    global count_position
    base = count_position
    update_max_base(base)
    if stmt() and func2():
        return True
    else:
        count_position = base
    return True


# end func ____________________________________________________________

def func_else():
    global count_position
    base = count_position
    update_max_base(base)
    if match('else'):
        return True
    else:
        count_position = base
    return True


# stmt ____________________________________________________________
def stmt():
    global count_position
    base = count_position
    update_max_base(base)
    if match("if") and match("(") and expr() and match(")") and stmt() and func_else() and stmt():
        return True
    else:
        count_position = base
    if match("while") and match("(") and expr() and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and match(";") and match(";") and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and assg() and match(";") and match(";") and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and match(";") and expr() and match(";") and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and match(";") and match(";") and assg() and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and assg() and match(";") and expr() and match(";") and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and assg() and match(";") and match(";") and assg() and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and match(";") and expr() and match(";") and assg() and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("for") and match("(") and assg() and match(";") and expr() and match(";") and assg() and match(")") and stmt():
        return True
    else:
        count_position = base
    if match("return") and match(";") and stmt():
        return True
    else:
        count_position = base
    if match("return") and expr() and match(";") and stmt():
        return True
    else:
        count_position = base
    if assg() and match(";") and stmt():
        return True
    else:
        count_position = base
    if match("ID") and match("(") and match(")") and match(";") and stmt():
        return True
    else:
        count_position = base
    if match("ID") and match("(") and expr() and stmt2() and match(")") and match(";") and stmt():
        return True
    else:
        count_position = base
    if match("{") and stmt() and match("}") and stmt():
        return True
    else:
        count_position = base
    if match(";") and stmt():
        return True
    else:
        count_position = base
    return True


def stmt2():
    global count_position
    base = count_position
    update_max_base(base)
    if match(",") and expr() and stmt2():
        return True
    else:
        count_position = base
    return True


# end stmt ____________________________________________________________

# assg
def assg():
    global count_position
    base = count_position
    update_max_base(base)
    if match("ID") and match("=") and expr():
        return True
    else:
        count_position = base
    if match("ID") and match("[") and expr() and match("]") and match("=") and expr():
        return True
    else:
        count_position = base
    return False


# end assg ____________________________________________________________

# expr ____________________________________________________________

def expr():
    global count_position
    base = count_position
    update_max_base(base)
    if match("-") and expr3():
        return True
    else:
        count_position = base
    if match("!") and expr3():
        return True
    else:
        count_position = base
    if match("ID") and expr3():
        return True
    else:
        count_position = base
    if match("ID") and match("(") and match(")") and expr3():
        return True
    else:
        count_position = base
    if match("ID") and match("(") and expr() and match(")") and expr3():
        return True
    else:
        count_position = base
    if match("ID") and match("(") and expr() and expr2() and match(")") and expr3():
        return True
    else:
        count_position = base
    if match("ID") and match("[") and expr() and match("]") and expr3():
        return True
    else:
        count_position = base
    if match("(") and expr() and match(")") and expr3():
        return True
    else:
        count_position = base
    if match("intcon") and expr3():
        return True
    else:
        count_position = base
    if match("charcon") and expr3():
        return True
    else:
        count_position = base
    if match("stringcon") and expr3():
        return True
    else:
        count_position = base
    return False


def expr2():
    global count_position
    base = count_position
    update_max_base(base)
    if match(",") and expr() and expr3():
        return True
    else:
        count_position = base
    return True


def expr3():
    global count_position
    base = count_position
    update_max_base(base)
    if binop() and expr() and expr3():
        return True
    else:
        count_position = base
    if relop() and expr() and expr3():
        return True
    else:
        count_position = base
    if logicalOp() and expr() and expr3():
        return True
    else:
        count_position = base
        return True


# end expr ____________________________________________________________

# binop ____________________________________________________________

def binop():
    global count_position
    base = count_position
    update_max_base(base)
    if match("+") or match("-") or match("*") or match("/") or match("%"):
        return True
    else:
        count_position = base
    return False


# end binop ____________________________________________________________

# relop ____________________________________________________________

def relop():
    global count_position
    base = count_position
    update_max_base(base)
    if match("<") or match(">") or match("<=") or match(">=") or match("==") or match("!="):
        return True
    else:
        count_position = base
    return False


# end relop ____________________________________________________________


# logicalOp ____________________________________________________________

def logicalOp():
    global count_position
    base = count_position
    update_max_base(base)
    if match("&&") or match("||"):
        return True
    else:
        count_position = base
    return False


# end logicalOp ____________________________________________________________

# prog ____________________________________________________________

def prog():
    global count_position
    base = count_position
    update_max_base(base)
    if dcl() and match(';'):
        return True
    else:
        count_position = base
    if func():
        return True
    else:
        count_position = base
    return False


# Helper functions --------------------------------------------------
def countIncremental(amount):
    global count_position
    count_position += amount


# end_prog ____________________________________________________________


# Verifica o match com o token atual
def match(token, isDecl = False):
    global token_list
    global count_position
    global error_aux
    if not isDecl and token_list[count_position][0] == 'ID' and token_list[count_position][1] not in list_id:
        print(Fore.RED + "Token '" + token_list[count_position][1] + "' was not declared. Line: " + str(token_list[count_position][2]))
        exit(1)

    if token_list[count_position][1] == token or token_list[count_position][0] == token:
        countIncremental(1)
        return True
    else:
        error_aux.append(token_list[count_position][1])
        return False


def parser():
    global token_list
    lexical_list = main.lexical()
    token_list = lexical_list.copy()
    for item in lexical_list:
        if item[0] == "Token não reconhecido":
            print(Fore.RED + "Unknown token: " + item[1] + " at line " + str(item[2]))
            exit(1)

        if item[0] == "OPEN_COMMENT" or item[0] == "CLOSE_COMMENT":
            token_list.remove(item)
    print(token_list)
    if prog():
        print("Parsing successful")
        print(list_id)
    else:
        print(Fore.RED + "Unexpected token before, " + "or missing token before " + "'" + str(token_list[max_base][1]) + "'" + " on line: " + str(token_list[max_base][2]))


parser()
