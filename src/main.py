def calculate(expression: str) -> float:

    expression = expression.strip()
    
    if not expression:
        raise ValueError("Expresión vacía")
    if expression.lower() == 'c':
        return 0.0
    
    # Validación de caracteres
    if not _is_valid_expression(expression):
        raise ValueError("Caracteres no válidos")
    
    # Tokenización y evaluación
    tokens = _tokenize(expression)
    return _evaluate(tokens)

def _is_valid_expression(expr: str) -> bool:
    """Valida caracteres permitidos: números, '+', y espacios"""
    allowed_chars = set("0123456789.+ ")
    return all(c in allowed_chars for c in expr)

def _tokenize(expr: str) -> list:
    """Convierte la expresión en tokens (números y '+')"""
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] == ' ':
            i += 1
        elif expr[i] == '+':
            tokens.append('+')
            i += 1
        elif expr[i].isdigit() or expr[i] == '.':
            num = ""
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            tokens.append(float(num))
        else:
            raise ValueError(f"Carácter inválido: '{expr[i]}'")
    return tokens

def _evaluate(tokens: list) -> float:
    """Evalúa tokens de suma (ej: [2, '+', 3] → 5.0)"""
    if not tokens:
        return 0.0
    
    result = tokens[0]
    i = 1
    while i < len(tokens):
        if tokens[i] == '+':
            if i + 1 >= len(tokens):
                raise ValueError("Expresión incompleta")
            result += tokens[i + 1]
            i += 2
        else:
            raise ValueError(f"Operador no soportado: '{tokens[i]}'")
    return result