'''

Code from GPT for convert string to equation

'''

import re
from typing import List, Union

Token = Union[float, str]

# Шаблон токенов:
#  - NUMBER: 12 или 12.34
#  - POW:    ** (должен идти раньше одиночного '*', поэтому выделен отдельно)
#  - OP:     одиночные операторы и скобки
TOKEN_REGEX = re.compile(
    r"""
    (?P<NUMBER>\d+(?:\.\d+)?)   # число:  12,  12.34
  | (?P<POW>\*\*)               # **  (степень)
  | (?P<OP>[+\-*/()])           # + - * / ( )
    """,
    re.VERBOSE,
)

OPS = {"+", "-", "*", "/", "**"}  # бинарные операторы


def tokenize(expr: str) -> List[Token]:
    """
    Разбивает строку выражения на токены.
    Возвращает список, где числа — float, остальные токены — строки ('+', '-', '**', '(', ')').

    Особенности:
      - игнорирует любые пробелы/табы;
      - удаляет запятые как мусор (например, '2,, + 3');
      - склеивает унарные + / - с числом: '-3', '+4.5', '(-2)' и т.п.
        (см. важное замечание про приоритет с '**' в описании выше)
    """
    # 1) Уберём запятые как мусор, чтобы не мешали токенизации
    cleaned = expr.replace(",", " ")

    # 2) Сырые токены: числа -> float, операторы/скобки -> str
    raw: List[Token] = []
    for m in TOKEN_REGEX.finditer(cleaned):
        kind = m.lastgroup
        text = m.group()
        if kind == "NUMBER":
            raw.append(float(text))
        elif kind == "POW":
            raw.append("**")
        else:  # OP
            raw.append(text)

    # 3) Постобработка: склеиваем унарные +/-
    #    Унарный знак — когда '+' или '-' стоит:
    #      - в самом начале,
    #      - сразу после другого оператора (+ - * / **) или '('
    #    и далее идёт число.
    tokens: List[Token] = []
    i = 0
    while i < len(raw):
        tok = raw[i]

        if (
            tok in ("+", "-")  # это плюс/минус
            and (
                len(tokens) == 0  # начало выражения
                or (isinstance(tokens[-1], str) and tokens[-1] in OPS.union({"("}))
            )
            and i + 1 < len(raw)
            and isinstance(raw[i + 1], float)  # за знаком действительно число
        ):
            num = raw[i + 1]
            tokens.append(-num if tok == "-" else num)
            i += 2
            continue

        tokens.append(tok)
        i += 1

    return tokens