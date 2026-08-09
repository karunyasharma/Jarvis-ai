def calculate(expression: str):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "I couldn't calculate that expression."
