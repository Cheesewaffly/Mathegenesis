import random, PolynomialDerivativeGenerator, PolynomialFractionLimits, PolynomialIntegralGenerator, PolynomialDefiniteIntegralGenerator

def generateall(sheet, amount):
    for _ in range(amount):
            PolynomialDerivativeGenerator.polynomialderivativegenerator([(random.randint(-20, 20) if _ != 0 else random.randint(1, 20)) for _ in range(random.randint(4, 10))][::-1], [], [], str(sheet[0]) + ".txt", str(sheet[1]) + ".txt")

            approaches = random.randint(-5, 5)
            PolynomialFractionLimits.polynomialfractionlimitgenerator(approaches, PolynomialFractionLimits.factorablepolynomialgenerator([[(random.randint(-10, 10) if _ != 0 else random.randint(1, 10)) for _ in range(random.randint(2, 5))], [(random.randint(-10, 10) if _ != 0 else random.randint(1, 10)) for _ in range(random.randint(2, 5))]], approaches, approaches * -1), [], str(sheet[0]) + ".txt", str(sheet[1]) + ".txt")

            PolynomialIntegralGenerator.polynomialintegralgenerator([(random.randint(-20, 20) if _ != 0 else random.randint(1, 20)) for _ in range(random.randint(4, 10))][::-1], [], [], str(sheet[0]) + ".txt", str(sheet[1]) + ".txt")

            PolynomialDefiniteIntegralGenerator.polynomialdefiniteintegralgenerator([(random.randint(-20, 20) if _ != 0 else random.randint(1, 20)) for _ in range(random.randint(3, 6))][::-1], random.randint(1, 10), random.randint(11, 20),[], [],str(sheet[0]) + ".txt", str(sheet[1]) + ".txt")
generateall(["Questions", "Answers"], int(input()))
