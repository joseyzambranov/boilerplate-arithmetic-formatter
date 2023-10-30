import re

def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ''
    first_row = ''
    second_row = ''
    third_row = ''
    answers = []  # Lista para almacenar las respuestas

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Cada problema debe contener exactamente dos operandos y un operador."

        operand1, operator, operand2 = parts

        if not re.match(r'^\d+$', operand1) or not re.match(r'^\d+$', operand2):
            return "Error: Numbers must only contain digits."

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        if len(str(operand1)) > 4 or len(str(operand2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        operand1 = int(operand1)  # Convierte operand1 a entero
        operand2 = int(operand2)  # Convierte operand2 a entero

        if operator == "+":
            result = operand1 + operand2
        else:
            result = operand1 - operand2

        max_len = max(len(str(operand1)), len(str(operand2)))
        first_row += str(operand1).rjust(max_len + 2)
        second_row += operator + str(operand2).rjust(max_len + 1)
        third_row += '-' * (max_len + 2)
        answers.append(str(result).rjust(max_len + 2))  # Agrega la respuesta

        if problem != problems[-1]:
            first_row += '    '
            second_row += '    '
            third_row += '    '

    arranged_problems = '\n'.join([first_row, second_row, third_row])
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)  # Agregar respuestas si show_answers es True
    
    return arranged_problems
