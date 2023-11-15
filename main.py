import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "^": operator.pow,
    None: lambda x, y: x

}
HIGH_PRIORITY = "/*^"
LOW_PRIORITY = "+-"


class Expression:
    def __init__(self, n1=None, n2=None, op=None, br=False):
        self.n1 = n1
        self.n2 = n2
        self.op = op
        self.brackets = br
        self.closed = False

    def push(self, n):
        if self.is_part():
            self.n1, self.n2, self.op = self.calculate(), None, None
        if self.n1 is None:
            self.n1 = n
        elif self.n2 is None:
            self.n2 = n

    def push_op(self, op):
        if self.is_part():
            self.n1, self.n2, self.op = self.calculate(), None, op
        else:
            self.op = op

    def is_ready(self):
        return ((self.n1 and self.n2 is None and self.op is None) or (self.n1 and self.n2 and self.op)) and (not self.brackets or self.closed)

    def is_part(self):
        return self.n1 is not None and self.n2 is not None and self.op is not None

    def calculate(self):
        if self.is_part():
            if self.op == "/" and self.n2 == 0:
                raise ZeroDivisionError
            return OPERATIONS[self.op](self.n1, self.n2)
        raise SyntaxError


def proceed_stack(num, op=None, br_op=False, br_cl=False):
    if not stack:
        stack.append(Expression(n1=num, op=op, br=br_op))
        return
    top = stack[-1]
    if op and top.op and top.op in LOW_PRIORITY and op in HIGH_PRIORITY or br_op:
        stack.append(Expression(n1=num, op=op, br=br_op))
    else:
        top.push(num)
        top.push_op(op)
        if br_cl:
            for expr in stack[::-1]:
                if expr.brackets and not expr.closed:
                    expr.closed = True
                    break
            proceed_stack(None)
        elif top.is_ready():
            res = top.n1
            if top.is_part():
                res = top.calculate()
            stack.pop()
            proceed_stack(res, op)


def parse_arg(let_stack: str, liter: dict[str, float] = {}):
    if let_stack.replace(".", '').isdecimal():
        return float(let_stack)
    if liter.get(let_stack, None) is None:
        raise SyntaxError
    return liter[let_stack]


if __name__ == '__main__':
    # ввод выражения без пробелов
    expr = "1+1*3"
    expr = expr.replace(" ", "")
    # Ввод переменных
    vars = {"a": 2}

    stack: list[Expression] = []
    n_stack = ""
    for l in expr:
        if l.isdecimal() or l == '.' or l.isalpha():
            n_stack += l
        else:
            if l == "(":
                proceed_stack(None, br_op=True)
            elif l == ")":
                number = parse_arg(n_stack, liter=vars)
                proceed_stack(number, br_cl=True)
                n_stack = ""
            else:
                if n_stack:
                    number = parse_arg(n_stack, liter=vars)
                    proceed_stack(number, l)
                else:
                    proceed_stack(None, l)
                n_stack = ""
    if n_stack:
        number = parse_arg(n_stack, liter=vars)
        proceed_stack(number)
    print(stack[-1].n1)
