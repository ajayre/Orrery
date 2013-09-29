Units.Current = UnitTypes.Millimeters

PressureAngle = 20
Thickness = 3
MercuryDiameter = 32
#OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/"
OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/Scratch/"
SizeFile = open(OutputFolder + "SaturnGearSizes.txt", 'w')

def GenerateGear(Name, Teeth, DiametralPitch, OutputFolder, SizeFile):
  Gear = Part(Name)
  Profile = Gear.AddGearDN("Profile", DiametralPitch, Teeth, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
  Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
  print >> SizeFile, "%s Pitch Diameter = %f" % (Name, Profile.PitchDiameter)
  Gear.Save(OutputFolder)
  Gear.Close()


# get diametral pitch used for gearbox
Gear = Part("MercuryPrimaryGear")
Profile = Gear.AddGearNP("Profile", 16, MercuryDiameter, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.Close()
DiametralPitch = Profile.DiametralPitch

# Saturn Gears 1 and 2
Gear = Part("Saturn1-2Gear")

Profile = Gear.AddGearDN("Profile", DiametralPitch, 32, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
print >> SizeFile, "Saturn 1 Pitch Diameter = %f" % Profile.PitchDiameter

Profile2 = Gear.AddGearDN("Profile2", DiametralPitch, 16, PressureAngle, 0, 0, Gear.GetFace("Face<129>"))
Gear.AddExtrudeBoss("Gear2", Profile2, Thickness + 1, False)
print >> SizeFile, "Saturn 2 Pitch Diameter = %f" % Profile2.PitchDiameter

Gear.Save(OutputFolder)
Gear.Close()

SizeFile.close()
