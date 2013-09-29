Units.Current = UnitTypes.Millimeters

PressureAngle = 20
Thickness = 3
MercuryDiameter = 32
#OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/"
OutputFolder = "C:/Users/Andy/Documents/Orrery/Parts/Source/Gearbox/Scratch/"
SizeFile = open(OutputFolder + "InputGearSizes.txt", 'w')

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

# Input gear
Gear = Part("InputGear")

Profile = Gear.AddGearDN("Profile", DiametralPitch, 64, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
print >> SizeFile, "Mercury Input Pitch Diameter = %f" % Profile.PitchDiameter

Profile2 = Gear.AddGearDN("Profile2", DiametralPitch, 50, PressureAngle, 0, 0, Gear.GetFace("Face<257>"))
Gear.AddExtrudeBoss("Gear2", Profile2, Thickness + 1, False)
print >> SizeFile, "Venus Input Pitch Diameter = %f" % Profile2.PitchDiameter

Profile3 = Gear.AddGearDN("Profile3", DiametralPitch, 40, PressureAngle, 0, 0, Gear.GetFace("Face<201>"))
Gear.AddExtrudeBoss("Gear3", Profile3, Thickness + 1, False)
print >> SizeFile, "Earth Input Pitch Diameter = %f" % Profile3.PitchDiameter

Profile4 = Gear.AddGearDN("Profile4", DiametralPitch, 32, PressureAngle, 0, 0, Gear.GetFace("Face<161>"))
Gear.AddExtrudeBoss("Gear4", Profile4, Thickness + 1, False)
print >> SizeFile, "Mars Input Pitch Diameter = %f" % Profile4.PitchDiameter

Gear.Save(OutputFolder)
Gear.Close()

SizeFile.close()
