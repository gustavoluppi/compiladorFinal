from constants import STATES, ALL_ELEMENTS, BIN_OPS , TYPE_BY_OPERATORS
import re
import utils

flag=0
line = 0
column = 0
state = STATES.INITIAL
response_token = []
token = ""
numeric_token = ""
acumula = ""

def open_file():
    """Abre o arquivo de entrada"""
    try:
        return open("teste.c", "r")
    except Exception as e:
        print("Erro ao abrir o arquivo")
        exit(1)

def append_identifier(token,line):
    global response_token
    tipo = TYPE_BY_OPERATORS.get(token)
    if tipo is not None:
        response_token.append([tipo, token,line])
    elif re.match(r"[\d]", token):
        response_token.append(["intcon",token,line])
    elif re.match(r"[\"]+[%\w\s]+[\"]*", token):
        response_token.append(["charcon", token, line])
    else:
        response_token.append(["ID", token,line])

def append_identifier_double(token,line_iterator, line):
    global flag
    global column
    if re.match(r"[\=]", token) and line_iterator[column] == "=" :
        
        flag = 1
        append_identifier("==", line)
        cursor = line_iterator[column]
    
    elif re.match(r"[\<]", token) and line_iterator[column] == "=" :
        flag = 1
        append_identifier("<=",line)
        cursor = line_iterator[column]
    
    elif re.match(r"[\>]", token) and line_iterator[column] == "=" :
        flag = 1
        append_identifier(">=",line)
        cursor = line_iterator[column]
    
    elif re.match(r"[\&]", token) and line_iterator[column] == "&" :
        flag = 1
        append_identifier("&&", line)
        cursor = line_iterator[column]
    
    elif re.match(r"[\|]", token) and line_iterator[column] == "|" :
        flag = 1
        append_identifier("||", line)
        cursor = line_iterator[column]

    elif re.match(r"[\!]", token) and line_iterator[column] == "=" :
        flag = 1
        append_identifier("!=", line)
        cursor = line_iterator[column]
                        
    else:
        append_identifier(token, line)
        


def append_error(token, line):
    global response_token
    """Adiciona o erro na lista de tokens"""
    if token != "\n" and token != " ":
        response_token.append(["Token não reconhecido", token, line])




def lexical():
    global flag
    global line
    global column
    global state
    global response_token
    global token
    global numeric_token
    global acumula
    input_file = open_file()
    for line_iterator in input_file:
        line = line + 1
        column = 0
        for cursor in line_iterator:
            column = column + 1
            if flag == 1:
                flag = 0
                continue


            if state == STATES.INITIAL:
                if cursor == "/" and line_iterator[column] == "*" and state == STATES.INITIAL and state != STATES.COMMENT:
                    state = STATES.COMMENT
                    append_identifier("/*", line)

                if re.search(r"^(#)", line_iterator) and state == STATES.INITIAL and state != STATES.COMMENT:
                    break

                if re.search(r"([A-Za-z_])", cursor) and state == STATES.INITIAL and state != STATES.COMMENT:
                    state = STATES.IDENTIFIER

                if re.match(r"[0-9]", cursor) and state == STATES.INITIAL and state != STATES.COMMENT:
                    state = STATES.NUMERIC
                    """Literal -> Serve para char"""
                if re.match(r"[\"]", cursor) and state == STATES.INITIAL and state != STATES.COMMENT:
                    state = STATES.LITERAL
                
                
                if utils.is_number(cursor) and utils.is_special_caracter(cursor) and state == STATES.INITIAL and state != STATES.COMMENT:
                    
                    
                    if not utils.is_error(cursor):
                       
                       
                        append_identifier_double(cursor,line_iterator, line)
                        if flag == 1:
                            continue
                    else:
                        
                        if cursor == '&' and line_iterator[column] == "&":
                            append_identifier_double(cursor,line_iterator,line)
                        
                        elif cursor == '|' and line_iterator[column] == "|":
                            append_identifier_double(cursor,line_iterator, line)
                        
                        elif cursor == "!" and line_iterator[column] == "=":
                            append_identifier_double(cursor,line_iterator, line)
                        
                        else:
                            append_error(cursor, line)
            
            


            if state == STATES.COMMENT:

                acumula = acumula + cursor
                if re.search(r"(\*\/)", acumula):
                    state = STATES.INITIAL
                    append_identifier("*/", line)
                    



            if state == STATES.IDENTIFIER:
                
                if re.match(r"([\w])", cursor):
                    token = token + cursor
                """Se for espaço em branco, ',', ; , = retorna True"""
                if utils.is_special_caracter(cursor):
                    state = STATES.INITIAL
                    """Se for palavra reservada retorna True Ex: int, char"""
                    if utils.is_reserved_word(token):
                        
                        append_identifier(token, line)
                        if cursor != " ":
                            if not utils.is_error(token):
                                append_identifier_double(cursor,line_iterator, line)
                            else:
                                append_error(token, line)
                        token = ""
                    else:
                        append_identifier(token, line)
                        if utils.is_special_caracter(cursor):

                            """Se for diferente de espaço em branco"""
                            if cursor != re.match(r"\s", cursor):
                                
                                if not utils.is_error(cursor):
                                    append_identifier_double(cursor,line_iterator, line)
                                    
                                else:
                                    if cursor == "!" and line_iterator[column] == "=":
                                        append_identifier_double(cursor,line_iterator, line)
                                    else:
                                        append_error(cursor, line)
                            state = STATES.INITIAL
                        token = ""

            if state == STATES.LITERAL: 
                
                if re.match(r"[%a-zA-z0-9\"\s]", cursor):
                    token = token + cursor
                if re.match(r"[\"]", cursor):
                    lit = re.match(r"[\"]+[%\w\s]+[\"]*", token)
                    if lit is not None:
                        append_identifier(lit.group(), line)
                        token = ""
                        state = STATES.INITIAL



            if state == STATES.NUMERIC: 
                if re.match(r"[\w.]", cursor):
                    numeric_token = numeric_token + cursor
                    """Se nao é numero"""
                if utils.is_number(cursor):
                    if re.match(r"(^[0-9]*$)", numeric_token):
                        if re.match(r"(^[0-9]*$)", numeric_token) is not None:
                            append_identifier(numeric_token, line)
                            if cursor != " ":
                                if not utils.is_error(cursor):
                                    append_identifier_double(cursor,line_iterator, line)
                                else:
                                    append_error(cursor, line)
                            state = STATES.INITIAL
                            numeric_token = ""
                    else:
                        if cursor in ALL_ELEMENTS or re.match(r"\s|\n", cursor) or cursor in BIN_OPS:
                            """Identifica o token inválido"""
                            append_error(cursor, line)
                            numeric_token = ""
                            state = STATES.INITIAL
                else:
                    if utils.is_number(cursor):
                        "Armazena token de separadores"
                        if cursor != " ":
                            if not utils.is_error(cursor):
                                
                                append_identifier_double(cursor,line_iterator, line)
                            else:
                                append_error(cursor, line)
                        state = STATES.INITIAL



    return response_token
