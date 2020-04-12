# msh2xdmf

The code contains a converter from MSH mesh format to XDMF mesh format for the dolfin users.

## How to test the installation ?
In order to test the compatibility of the script with the user installation of `meshio` and `dolfin`, the following command must be run at the root of the repository:
```
% python3 -m pytest
```

## How to convert a mesh ?
For this exemple, let us consider a 2D mesh named `mesh.msh` where 3 physical groups are defined in the `mesh.geo` file:
```cpp
// Domain
Physical Surface("domain") = {1};
// Boundaries
Physical Line("left") = {4};
Physical Line("right") = {2};
```
In order to convert this mesh, the following command must be used:
```shell
% python3 msh2xdmf.py -d 2 mesh.msh
```
This command should outputs the following table (the table should be empty for msh2 format):
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
    domain="domain.xdmf",
    boundaries="boundaries.xdmf",
    dim=2,
    )
```

## How to convert a multidomain mesh ?
For this exemple, let us consider a mesh named `multidomain.msh` where 7 physical groups are defined in the `mesh.geo` file:
```cpp
// Domain
Physical Surface("top_domain") = {1};
Physical Surface("bot_domain") = {2};

// Boundaries
Physical Line("middle") = {1};
Physical Line("right") = {2, 5};
Physical Line("top") = {3};
Physical Line("bot") = {6};
Physical Line("left") = {4, 7};
```
In order to convert this mesh, the following command must be used:
```shell
% python3 msh2xdmf.py -d 2 multidomain.msh
```
This command should outputs the following table (the table should be empty for msh2 format):
```
+-----------------------------------------+
|     GMSH label     | MeshFunction value |
+--------------------+--------------------+
|       middle       |         3          |
|       right        |         4          |
|        top         |         5          |
|        bot         |         6          |
|        left        |         7          |
|     top_domain     |         1          |
|     bot_domain     |         2          |
+-----------------------------------------+
```
This table contains the GMSH labels and the value associated to each physical groups. Additionally, two new files are generated: `domain.xdmf` which contains the domain and the values associated to each subdomains and `boundaries.xdmf` which contains the values associated to the boundaries. In order to check the label/value association, both files can be openend with Paraview (or an alternative) to check the values associated to each boundaries and subdomains.

In order to import the mesh and the value asosociated to the subdomains and the boundaries in dolfin, one can use the utility function `import_mesh_from_xdmf` which returns the dolfin `Mesh` object and the `MeshFunction` object associated to the files.
```python3
from msh2xdmf import_mesh_from_xdmf

mesh, mesh_function = import_mesh_from_xdmf(
    domain="domain.xdmf",
    boundaries="boundaries.xdmf",
    dim=2,
    subdomains=True
    )
```
The MeshFunction will contains the value associated to each subdomains and to each boundaries.
