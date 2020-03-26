import os
import sys
sys.path.append('.')
from msh2xdmf import import_mesh_from_xdmf


def test_import():
    """
    Test the import from the xdmf file.
    """
    # Get the current directory
    current_dir = "{}/{}".format(os.getcwd(), "test/import")
    # Run the import
    mesh, mf = import_mesh_from_xdmf(
        domain="domain.xdmf",
        boundaries="boundaries.xdmf",
        dim=2,
        directory=current_dir,
        )
