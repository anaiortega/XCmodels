# Appuis.
points= vtk.vtkPoints()
for pt in appuis:
  pos= pt.getPos
  points.InsertNextPoint(pos.x,pos.y-0.5,pos.z)
polydata= vtk.vtkPolyData()
polydata.SetPoints(points)

cone = vtk.vtkConeSource()
cone.SetRadius(0.5)
cone.SetHeight(1.0)
cone.SetDirection(0.0,1.0,0.0)

glyph = vtk.vtkGlyph3D()
glyph.SetInput(polydata)
glyph.SetSourceConnection(cone.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(glyph.GetOutputPort())
supportsActor = vtk.vtkActor()
supportsActor.GetProperty().SetColor(0,0,0)
supportsActor.SetMapper(mapper)
