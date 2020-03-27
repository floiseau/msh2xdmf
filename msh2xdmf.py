#!/usr/bin/env python

import argparse
import meshio
import os
import numpy as np
try:
    from dolfin import XDMFFile, Mesh, MeshValueCollection
    from dolfin.cpp.mesh import MeshFunctionSizet
except ImportError:
    print("Could not import dolfin. Continuing without Dolfin support.")


def msh2xdmf(mesh_name, dim=2, directory="."):
    """
    Function converting a MSH2 mesh into XDMF files.
    The XDMF files are:
        - "domain.xdmf": the domain;
        - "boundaries.xdmf": the boundaries physical groups from GMSH;
    """
    # Set the parameters
    if dim == 2:
        domain_type = "triangle"
        boundary_type = "line"
    elif dim == 3:
        domain_type = "tetra"
        boundary_type = "triangle"

    # Read the input mesh
    msh = meshio.read("{}/{}".format(directory, mesh_name))

    # Generate a meshio Mesh for the domain
    domain = meshio.Mesh(
        points=msh.points[:, :dim],
        cells=[
            cellBlock for cellBlock in msh.cells
            if cellBlock.type == domain_type
        ],
    )

    # Export the XDMF mesh of the domain
    meshio.write(
        "{}/{}".format(directory, "domain.xdmf"),
        domain,
        file_format="xdmf"
        )

    # Generate the cell block for the boundaries cells
    boundaries_cells_data = np.concatenate(
        [arr for (t, arr) in msh.cells if t == boundary_type]
        )
    boundaries_cells = [
        meshio.CellBlock(
            type=boundary_type,
            data=boundaries_cells_data,
            )
        ]
    # Generate the boundaries cells data
    boundaries_cell_data = {
        "boundaries": [
            np.concatenate(
                [
                    cellBlock.data for cellBlock in msh.cells
                    if cellBlock.type == boundary_type
                    ]
                )
            ]
        }
    # Generate the meshio Mesh for the boundaries physical groups
    boundaries = meshio.Mesh(
        points=msh.points[:, :dim],
        cells=boundaries_cells,
        cell_data=boundaries_cell_data
    )

    # Export the XDMF mesh of the lines boundaries
    meshio.write(
        "{}/{}".format(directory, "boundaries.xdmf"),
        boundaries,
        file_format="xdmf"
        )

    # Display the correspondance
    formatter = "|{:^20}|{:^20}|"
    topbot = "+{:-^41}+".format("", "")
    separator = "+{:-^20}+{:-^20}+".format("", "")

    # Display
    print(topbot)
    print(formatter.format("GMSH label", "MeshFunction value"))
    print(separator)

    for label, arrays in msh.cell_sets.items():
        # Get the index of the array in arrays
        for i, array in enumerate(arrays):
            if array.size != 0:
                index = i
        # Get the value in cell_data for the corresponding array
        value = msh.cell_data["gmsh:physical"][index][0]
        # Display the association
        print(formatter.format(label, value))
    print(topbot)


def import_mesh_from_xdmf(
        domain="domain.xdmf",
        boundaries="boundaries.xdmf",
        dim=2,
        directory="."):
    """
    Function importing a msh mesh and converting it into a dolfin mesh.

    Arguments:
        - domain: name of the domain XDMF file;
        - boundaries: name of the boundaries XDMF file;
        - directory: (optional) directory of the mesh;

    Output:
        - dolfin Mesh object containing the domain;
        - dolfin MeshFunction object containing the physical lines (dim=2) or
        surfaces (dim=3) defined in the msh file;
    """
    # Import the converted domain
    mesh = Mesh()
    with XDMFFile("{}/{}".format(directory, domain)) as infile:
        infile.read(mesh)
    # Import the boundaries
    mvc = MeshValueCollection("size_t", mesh, dim=dim)
    with XDMFFile("{}/{}".format(directory, boundaries)) as infile:
        infile.read(mvc, 'boundaries')
    mf = MeshFunctionSizet(mesh, mvc)
    # Return the Mesh and the MeshFunction
    return mesh, mf


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "msh_file",
        help="input .msh file",
        type=str,
        )
    parser.add_argument(
        "-d",
        "--dimension",
        help="dimension of the domain",
        type=int,
        default=2,
        )
    args = parser.parse_args()
    # Get current directory
    current_directory = os.getcwd()
    # Conert the mesh
    msh2xdmf(args.msh_file, args.dimension, directory=current_directory)
