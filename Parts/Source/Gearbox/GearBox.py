Units.Current = UnitTypes.Millimeters

PressureAngle = 20
Thickness = 3
MercuryDiameter = 32
#OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/"
OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/Scratch/"
SizeFile = open(OutputFolder + "GearSizes.txt", 'w')

def GenerateGear(Name, Teeth, DiametralPitch, OutputFolder, SizeFile):
  Gear = Part(Name)
  Profile = Gear.AddGearDN("Profile", DiametralPitch, Teeth, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
  Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
  print >> SizeFile, "%s Pitch Diameter = %f" % (Name, Profile.PitchDiameter)
  Gear.Save(OutputFolder)
  Gear.Close()


# mercury primary gear
Gear = Part("MercuryPrimaryGear")
Profile = Gear.AddGearNP("Profile", 16, MercuryDiameter, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
print >> SizeFile, "MercuryPrimaryGear Pitch Diameter = %f" % Profile.PitchDiameter
Gear.Save(OutputFolder)
Gear.Close()

DiametralPitch = Profile.DiametralPitch
#print "Diametral Pitch = %f\n" % DiametralPitch

# primary gears
GenerateGear("VenusPrimaryGear",   32,  DiametralPitch, OutputFolder, SizeFile)
GenerateGear("EarthPrimaryGear",   40,  DiametralPitch, OutputFolder, SizeFile)
GenerateGear("MarsPrimaryGear",    50,  DiametralPitch, OutputFolder, SizeFile)
GenerateGear("JupiterPrimaryGear", 50,  DiametralPitch, OutputFolder, SizeFile)
GenerateGear("SaturnPrimaryGear",  64,  DiametralPitch, OutputFolder, SizeFile)

# earth large gear
#GenerateGear("EarthLargeGear",    128, DiametralPitch, OutputFolder, SizeFile)

# input gears
#GenerateGear("MercuryInputGear",   64,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("VenusInputGear",     50,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("EarthInputGear",     40,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("MarsInputGear",      32,  DiametralPitch, OutputFolder, SizeFile)

# jupiter gears
#GenerateGear("Jupiter1Gear",       48,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("Jupiter2Gear",       16,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("Jupiter3Gear",       48,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("Jupiter4Gear",       16,  DiametralPitch, OutputFolder, SizeFile)
GenerateGear("Jupiter5Gear",       48,  DiametralPitch, OutputFolder, SizeFile)

# saturn gears
#GenerateGear("Saturn1Gear",        32,  DiametralPitch, OutputFolder, SizeFile)
#GenerateGear("Saturn2Gear",        16,  DiametralPitch, OutputFolder, SizeFile)

SizeFile.close()
