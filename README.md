# msh2xdmf

The code contains a converter from MSH mesh format to XDMF mesh format for the dolfin users.

## How to test the installation ?
In order to test the compatibility of the script with the user installation of `meshio` and `dolfin`, the following command must be run at the root of the repository:
```
% python3 -m pytest
```

## How to convert and import a mesh in one step ?
For this example, let us consider a 2D mesh named `mesh.msh` where 3 physical groups are defined in the `mesh.geo` file:
```cpp
// Domain
Physical Surface("domain") = {1};
// Boundaries
Physical Line("left") = {4};
Physical Line("right") = {2};
```
In order to convert and import the mesh and its boundaries in dolfin, one can use the utility function `import_mesh` which returns the dolfin `Mesh` object, the `MeshFunction` object associated to the files and a dictionary containing the association_table.

```python3
from msh2xdmf import import_mesh

mesh, boundaries_mf, association_table = import_mesh(
    prefix='mesh', # it the file name of the msh file without the extension
    dim=2,
    )
```

In order to get the value associated to get the `MeshFunction` value associated to the `left`, one must use: `association_table["left"]`.

Running this function will display the association table between the GMSH label and the MeshFunction values:
```
+-----------------------------------------+
|     GMSH label     | MeshFunction value |
+--------------------+--------------------+
|        left        |         2          |
|       right        |         3          |
|       domain       |         1          |
+-----------------------------------------+
```
This table contains the GMSH labels and the value associated to each physical groups. Additionally, five new files are generated: `mesh_domain.xdmf` and `mesh_domain.h5` which contain the domain, `mesh_boundaries.xdmf` and `mesh_boundaries.h5` which contain the values associated to the boundaries and `mesh_association_table.ini` which contains the association table. In order to check the label/value association, the `.xdmf` files can also be openend with Paraview (or an alternative). It will show the value associated to each domains/boundaries.

## How to convert a mesh from msh to xdmf?

For this example, let us consider a 2D mesh named `mesh.msh` where 3 physical groups are defined in the `mesh.geo` file:
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
This table contains the GMSH labels and the value associated to each physical groups. Additionally, five new files are generated: `mesh_domain.xdmf` and `mesh_domain.h5` which contain the domain, `mesh_boundaries.xdmf` and `mesh_boundaries.h5` which contain the values associated to the boundaries and `mesh_association_table.ini` which contains the association table. In order to check the label/value association, the `.xdmf` files can also be openend with Paraview (or an alternative). It will show the value associated to each domains/boundaries.


## How to import an xdmf mesh ?
In order to only import the mesh and its boundaries in dolfin, one must also use the utility function `import_mesh` which returns the dolfin `Mesh` object, the `MeshFunction` object associated to the files and a dictionary containing the association_table. This function requires the files create by the conversion function.
```python3
from msh2xdmf import import_mesh

mesh, boundaries_mf, association_table = import_mesh(
    prefix="mesh", # it the file name of the msh file without the extension
    dim=2,
    )
```
In order to get the value associated to get the `MeshFunction` value associated to the `left`, one must use: `association_table["left"]`.

## How to convert a multidomain mesh ?
For this example, let us consider a mesh named `multidomain.msh` where 7 physical groups are defined in the `multidomain.geo` file:
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

In order import the mesh and the value associated to the subdomains and the boundaries in dolfin, one can use the utility function `import_mesh` which returns the dolfin `Mesh` object and the `MeshFunction` object associated to the files.
```python3
from msh2xdmf import import_mesh

mesh, boundaries_mf, subdomains_mf, association_table = import_mesh(
    prefix='multidomain',
    dim=2,
    subdomains=True,
    )
```
It should outputs the following table (the table should be empty for msh2 format):
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
This table contains the GMSH labels and the value associated to each physical groups. Additionally, four new files are generated: `multidomain_domain.xdmf` and `multidomain_domain.h5` which contain the domain and the values associated to each subdomains, `multidomain_boundaries.xdmf` and `multidomain_boundaries.h5` which contain the values associated to the boundaries and `mesh_association_table.ini` which contain the association table. In order to check the label/value association, both files can be opened with Paraview (or an alternative) to check the values associated to each boundaries and subdomains.

In this example, `boundaries_mf` is the MeshFunction object associated to the boundaries and `subdomains_mf` is the MeshFunction associated to the subdomains.

In order to get the value associated to get the `MeshFunction` value associated to the `left`, one must use: `association_table["left"]`. The same dictionary can also be used for the subdomains.
