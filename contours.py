""" Contours Animation """

View3DAtts1 = View3DAttributes()
View3DAtts1.viewNormal = (-0.990632, 0.126795, 0.0507026)
View3DAtts1.focus = (3.89585, 3.99132, 4.90529)
View3DAtts1.viewUp = (0.123697, 0.990494, -0.0601718)
View3DAtts1.viewAngle = 30
View3DAtts1.parallelScale = 2.05937
View3DAtts1.nearPlane = -4.11875
View3DAtts1.farPlane = 4.11875
View3DAtts1.imagePan = (-0.00271495, 0.0206495)
View3DAtts1.imageZoom = 1.41632
View3DAtts1.perspective = 1
View3DAtts1.eyeAngle = 2
View3DAtts1.centerOfRotationSet = 0
View3DAtts1.centerOfRotation = (3.89585, 3.99132, 4.90529)
View3DAtts1.axis3DScaleFlag = 0
View3DAtts1.axis3DScales = (1, 1, 1)
View3DAtts1.shear = (0, 0, 1)
SetView3D(View3DAtts1)


AddPlot("Pseudocolor", "mesh_quality/aspect")
p = PseudocolorAttributes()
p.colorTableName = "PuBu"
p.opacityType = p.Constant
p.opacity = 0.19
p.legendFlag = 0
SetPlotOptions(p)
DrawPlots()


AddPlot("Contour", "velocity_magnitude", 1, 1)
c = ContourAttributes()
c.changedColors = (0, 1, 2, 3, 4)
c.colorType = c.ColorByMultipleColors 
c.colorTableName = "Default"
c.SetMultiColor(0, (255, 0, 0, 55))
c.SetMultiColor(1, (255, 153, 0, 105))
c.SetMultiColor(2, (255, 255, 153, 155))
c.SetMultiColor(3, (255, 153, 204, 180))
c.SetMultiColor(4, (153, 51, 102, 205))
c.SetMultiColor(5, (255, 255, 0, 255))
c.SetMultiColor(6, (255, 135, 0, 255))
c.SetMultiColor(7, (255, 0, 135, 255))
c.SetMultiColor(8, (168, 168, 168, 255))
c.SetMultiColor(9, (255, 68, 68, 255))
c.contourNLevels = 5
SetPlotOptions(c)
DrawPlots()


a = AnnotationAttributes()
a.axes3D.visible = 0
a.axes3D.lineWidth = 0
a.axes3D.triadFlag = 0
a.axes3D.bboxFlag = 0
a.axes3D.xAxis.grid = 0
a.axesArray.lineWidth = 0
a.axesArray.axes.grid = 0
a.databaseInfoFlag = 0
a.userInfoFlag = 0
a.backgroundMode = a.Gradient
a.gradientBackgroundStyle = a.BottomToTop
a.gradientColor1 = (235, 235, 235, 255) # Gray
a.gradientColor2 = (255, 255, 255, 255) # White
SetAnnotationAttributes(a)


for i in range(TimeSliderGetNStates()):
  TimeSliderSetState(i)
  SaveWindow()
