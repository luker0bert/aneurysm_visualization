""" Pathlines Animation """"

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

'''AddPlot("Pseudocolor", "velocity_magnitude")
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.limitsMode = PseudocolorAtts.CurrentPlot  # OriginalData, CurrentPlot
SetPlotOptions(PseudocolorAtts)'''

'''AddOperator("Slice")
SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
SliceAtts.originPoint = (3, 3, 3)
SliceAtts.originIntercept = 1
SliceAtts.axisType = SliceAtts.YAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.project2d = 0
SetOperatorOptions(SliceAtts, 1)'''

DrawPlots()


seed_point = (3.38591, 2.79, 5.5)


# Create pathline plot, same as before, but the argument "atts.pathlines"  is set to 1
AddPlot("Streamline", "velocity", 0, 0)
SetActivePlots(1)

atts = StreamlineAttributes()
atts.sourceType = atts.SpecifiedPlane  # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
atts.planeOrigin = seed_point
atts.planeNormal = (0, 1, 0)
atts.planeUpAxis = (0, 0, 1)
atts.sampleDensity0 = 6
atts.sampleDensity1 = 4
atts.maxSteps = 3000
atts.pathlines = 1
atts.pathlinesCMFE = atts.CONN_CMFE  # CONN_CMFE, POS_CMFE
atts.integrationType = atts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
atts.legendMinFlag = 1
atts.legendMaxFlag = 0
atts.legendMax = 7.3
atts.displayEnd = 1
atts.displayBeginFlag = 0
atts.displayEndFlag = 0
atts.referenceTypeForDisplay = atts.Time  # Distance, Time, Step
atts.displayMethod = atts.Ribbons # Lines, Tubes, Ribbons
atts.colorTableName = "YlOrRd"
atts.ribbonWidthBBox = 0.005
atts.showSeeds = 0
atts.headDisplayType = atts.Cone  # Sphere, Cone
atts.sampleDistance0 = 0.1
atts.sampleDistance1 = 0.1
atts.issueTerminationWarnings = 0
atts.issueStiffnessWarnings = 0
atts.issueCriticalPointsWarnings = 0
SetPlotOptions(atts)

DrawPlots()

view = GetView3D()
view.viewNormal = (-1,0,0)
SetView3D(view)

view.viewNormal
# Set the annotation attributes
annot = AnnotationAttributes()
annot.axes3D.xAxis.title.visible = 0
annot.axes3D.yAxis.title.visible = 0
annot.axes3D.zAxis.title.visible = 0
annot.userInfoFlag = 0
SetAnnotationAttributes(annot)

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



atts.displayEndFlag = 1
M = 150 # number of images
final_time = .995
for i in range(M+1):
  atts.displayEnd = final_time * i /M
  SetPlotOptions(atts)
  SaveWindow()


