Units.Current = UnitTypes.Millimeters

PressureAngle = 20
Thickness = 3
MercuryDiameter = 32

def GenerateGear(Name, Teeth, DiametralPitch):
  Gear = Part(Name)
  Profile = Gear.AddGearDN("Profile", DiametralPitch, Teeth, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
  Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
  Gear.Save("C:/Users/Andy/Documents/Orrery/Parts/Source/")
  Gear.Close()


# mercury primary gear
Gear = Part("MercuryPrimaryGear")
Profile = Gear.AddGearNP("Profile", 16, MercuryDiameter, PressureAngle, 0, 0, Gear.GetPlane("XY-Plane"))
Gear.AddExtrudeBoss("Gear", Profile, Thickness, False)
Gear.Save("C:/Users/Andy/Documents/Orrery/Parts/Source/")
Gear.Close()

DiametralPitch = Profile.DiametralPitch
print "Diametral Pitch = %f\n" % DiametralPitch

# primary gears
GenerateGear("VenusPrimaryGear",   32,  DiametralPitch)
GenerateGear("EarthPrimaryGear",   40,  DiametralPitch)
GenerateGear("MarsPrimaryGear",    50,  DiametralPitch)
GenerateGear("JupiterPrimaryGear", 50,  DiametralPitch)
GenerateGear("SaturnPrimaryGear",  64,  DiametralPitch)

# earth large gear
#GenerateGear("EarthLargeGear",    128, DiametralPitch)

# input gears
GenerateGear("MercuryInputGear",   64,  DiametralPitch)
GenerateGear("VenusInputGear",     50,  DiametralPitch)
GenerateGear("EarthInputGear",     40,  DiametralPitch)
GenerateGear("MarsInputGear",      32,  DiametralPitch)

# jupiter gears
GenerateGear("Jupiter1Gear",       48,  DiametralPitch)
GenerateGear("Jupiter2Gear",       16,  DiametralPitch)
GenerateGear("Jupiter3Gear",       48,  DiametralPitch)
GenerateGear("Jupiter4Gear",       16,  DiametralPitch)
GenerateGear("Jupiter5Gear",       48,  DiametralPitch)

# saturn gears
GenerateGear("Saturn1Gear",        32,  DiametralPitch)
GenerateGear("Saturn2Gear",        16,  DiametralPitch)
