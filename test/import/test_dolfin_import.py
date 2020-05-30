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
    mesh, boundaries, subdomains, labels = import_mesh_from_xdmf(
        domain="multidomain_domain.xdmf",
        boundaries="multidomain_boundaries.xdmf",
        labels="multidomain_labels.yml",
        dim=2,
        directory=current_dir,
        subdomains=True,
        )
