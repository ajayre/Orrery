﻿Units.Current = UnitTypes.Millimeters

PressureAngle = 20
Thickness = 3
MercuryDiameter = 32
#OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/"
OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/Scratch/"
SizeFile = open(OutputFolder + "EarthGearSizes.txt", 'w')

def GenerateGear(Name, Teeth, DiametralPitch, OutputFolder, SizeFile):
  Gear = Part(Name)
  Profile = Gear.AddGearDN("Profile", DiametralPitch, Teeth, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
  Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
  print >> SizeFile, "%s Pitch Diameter = %f" % (Name, Profile.PitchDiameter)
  Gear.Save(OutputFolder)
  Gear.Close()


# get diametral pitch
Gear = Part("MercuryPrimaryGear")
Profile = Gear.AddGearNP("Profile", 16, MercuryDiameter, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.Close()
DiametralPitch = Profile.DiametralPitch

# earth large gear
GenerateGear("EarthLargeGear", 80, DiametralPitch * 2, OutputFolder, SizeFile)
GenerateGear("Earth3Gear", 14, DiametralPitch * 2, OutputFolder, SizeFile)

# Earth 1 and 2 gears
Gear = Part("Earth1-2Gear")

Profile = Gear.AddGearDN("Profile", DiametralPitch, 32, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.AddExtrudeBoss("Gear", Profile, Thickness + 1, False)
print >> SizeFile, "Earth1Gear Pitch Diameter = %f" % Profile.PitchDiameter

Profile2 = Gear.AddGearDN("Profile2", DiametralPitch, 14, PressureAngle, 0, 0, Gear.GetFace("Face<129>"))
Gear.AddExtrudeBoss("Gear", Profile2, Thickness, False)
print >> SizeFile, "Earth2Gear Pitch Diameter = %f" % Profile2.PitchDiameter

Gear.Save(OutputFolder)
Gear.Close()

SizeFile.close()
