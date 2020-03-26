# msh2xdmf

The code contains a converter from MSH mesh format to XDMF mesh format for the dolphin users.

## How to convert a mesh ?
For this exemple, let us consider a mesh named `mesh.msh` where 3 physical groups are defined in the `mesh.geo` file:
```cpp
// Domain
Physical Surface("domain") = {1};
// Boundaries
Physical Line("left") = {4};
Physical Line("right") = {2};
```
In order to convert this mesh, the following command must be used:
```shell
% python3 msh2xdmf.py -d 2 bar.msh
```
This command should outputs the following table (this might not work for msh2 meshes):
```
+-----------------------------------------+
|     GMSH label     | MeshFunction value |
+--------------------+--------------------+
|        left        |         2          |
|       right        |         3          |
|       domain       |         1          |
+-----------------------------------------+
```
This table contains the GMSH labels and the value associated to each physical groups. Additionally, two new files are generated: `domain.xdmf` which contains the domain and `boundaries.xdmf` which contains the values associated to the boundaries. In order to check the label/value association, the `boundaries.xdmf` can also be openend with Paraview (or an alternative). It will show the value associated to each boundaries.

In order to import the mesh and its boundaries in dolfin, one can use the utility function `import_mesh_from_xdmf` which returns the dolfin `Mesh` object and the `MeshFunction` object associated to the files.
```python3
from msh2xdmf import_mesh_from_xdmf

mesh, mesh_function = import_mesh_from_xdmf(
    domain="domain.xdmf"
    boundaries="boundaries.xdmf"
    )
```
