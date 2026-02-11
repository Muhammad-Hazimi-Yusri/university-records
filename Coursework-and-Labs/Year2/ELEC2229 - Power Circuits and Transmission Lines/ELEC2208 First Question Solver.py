import math

def prepareValueForOutput(_value):
    return str(round(_value, 6))


print("Note that this program assumes 6-pulse inverters and rectifiers.")
print("Please only enter raw numbers.")
print("All outputs are to 6 significant figures. ")
print("=======================================")
print()

inRect = float(input("Enter the supply voltage for the Rectifier: "))
freqRect = float(input("Enter the frequency for the Rectifier: "))
inductRect = float(input("Enter the inductance for the Rectifier: "))
print()

inInv = float(input("Enter the supply voltage for the Inverter: "))
freqInv = float(input("Enter the frequency for the Inverter: "))
inductInv = float(input("Enter the inductance for the Inverter: "))

print()
powerInv = float(input("Enter the power of the Inverter: "))
currentInv = float(input("Enter the DC current of the Inverter: "))

print()
resistance = float(input("Enter the resistance of the AC circuit: "))

print()
print("=======================================")
_v2 = powerInv / currentInv
_deltaV = currentInv * resistance
_v1 = _v2 + _deltaV
_eff = _v2 / _v1

p = 6
_peakRect = inRect * math.sqrt(2)
_alpha = math.acos((_v1 + 6 * freqRect * inductRect * currentInv) / (p * (_peakRect / math.pi) * math.sin(math.pi / 6)) )

_peakInv = inInv * math.sqrt(2)
_beta = math.acos((_v2 - 6 * freqInv * inductInv * currentInv) / (p * (_peakInv / math.pi) * math.sin(math.pi / 6)) )

_degAlpha = math.degrees(_alpha)
_degBeta = math.degrees(_beta)

print("Rectifier Input, aka V1: "+ prepareValueForOutput(_v1))
print("Peak Rectifier Voltage: "+ prepareValueForOutput(_peakRect))
print("Firing Angle (Rectifier), aka Alpha: " + prepareValueForOutput(_degAlpha))
print("Firing Angle (Rectifier), aka Alpha (RAD): " + prepareValueForOutput(_alpha))
print()

print("Inverter Input, aka V2: "+ prepareValueForOutput(_v2))
print("Peak Inverter Voltage: "+ prepareValueForOutput(_peakInv))
print("Firing Advance Angle (Inverter), aka Beta: " +prepareValueForOutput(_degBeta))
print("Firing Angle (Inverter), aka Alpha: " + prepareValueForOutput(180 - _degBeta))

print("Firing Advance Angle (Inverter), aka Beta (RAD): " +prepareValueForOutput(_beta))
print("Firing Angle (Inverter), aka Alpha (RAD): " + prepareValueForOutput(math.pi - _beta))
print()

print("Voltage loss at Resistor: "+ prepareValueForOutput(_deltaV))
print("Efficiency: "+ prepareValueForOutput(_eff))
print()

