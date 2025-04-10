def function_with_obvious_error():
    x = 10
      y = 20  # Indentation error that should be caught by flake8
    return x + y
