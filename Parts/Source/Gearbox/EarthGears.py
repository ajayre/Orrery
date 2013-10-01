Units.Current = UnitTypes.Millimeters

PressureAngle = 25
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
GenerateGear("EarthLargeGear", 128, DiametralPitch * 2, OutputFolder, SizeFile)
GenerateGear("EarthSmallGear", 10, DiametralPitch * 2, OutputFolder, SizeFile)

SizeFile.close()
