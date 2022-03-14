import random, math, fractions
def factorablepolynomialgenerator(polynomials, approaches, linearfunction, substitute=[[], []], multiplication=[[], []]):
    for code in range(2):
        substitute[code], multiplication[code] = [polynomials[code][n] * (approaches ** n) for n in range(len(polynomials[code]))], [polynomials[code][n] * linearfunction for n in range(len(polynomials[code]))]
        if sum(substitute[code]) != 0:
            polynomials[code].insert(0, 0), multiplication[code].append(0)
            polynomials[code] = [polynomials[code][n] + multiplication[code][n] for n in range(len(polynomials[code]))][::-1]
        substitute[code] = [(n * polynomials[code][::-1][n] * (approaches ** (n - 1)) if n > 0 else 0) for n in range(len(polynomials[code]))]
    return polynomials if sum(substitute[1]) != 0 else polynomials[::-1], substitute if sum(substitute[1]) != 0 else substitute[::-1]
def polynomialfractionlimitgenerator(approaches, limit, fraction, questionsheet, answersheet):
    for polynomial in range(len(limit[0])):
        fraction.append(str("=" + str("".join([specialcases.replace(" 1 ", "").replace(" -1 ", "-").replace("+ ", "+").replace(" x", "x").replace("^1", "").replace("x^0", "").replace("+-", "-") for specialcases in ["+" + plus for plus in [term for term in [" " + str(limit[0][polynomial][power]) + " x^" + str([n for n in range(len(limit[0][polynomial]))][::-1][power]) for power in range(len(limit[0][polynomial]))] if " 0 x" not in term]]])) + " ").replace("=+", "").replace("=-", "-").replace("+ ", "+1 ").replace("- ", "-1 "))
    with open(questionsheet, "a") as f1, open(answersheet, "a") as f2:
        f1.write("\\item $\\displaystyle \\lim_{x\\to" + str(approaches) + "}{\\frac{" + fraction[0][:-1] + "}{" + fraction[1][:-1] + "}}=\\cdots$\n"), f2.write(("\\item $\\displaystyle " + str(int(sum(limit[1][0])/sum(limit[1][1]))) + "$\n") if float(sum(limit[1][0])/sum(limit[1][1])).is_integer() else (("\\item $\\displaystyle \\frac{" + str(abs(fractions.Fraction(sum(limit[1][0])/sum(limit[1][1])).limit_denominator().numerator)) + "}{" + str(abs(fractions.Fraction(sum(limit[1][0])/sum(limit[1][1])).limit_denominator().denominator)) + "}$\n") if sum(limit[1][0])/sum(limit[1][1]) > 0 else ("\\item $\\displaystyle -\\frac{" + str(abs(fractions.Fraction(sum(limit[1][0])/sum(limit[1][1]))).limit_denominator().numerator) + "}{" + str(abs(fractions.Fraction(sum(limit[1][0])/sum(limit[1][1]))).limit_denominator().denominator) + "}$\n")))