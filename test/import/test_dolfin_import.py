from msh2xdmf import import_mesh
import os
import sys
sys.path.append('.')


def test_import():
    """
    Test the import from the xdmf file.
    """
    # Get the current directory
    current_dir = "{}/{}".format(os.getcwd(), "test/import")
    # Run the import
    mesh, boundaries, subdomains, labels = import_mesh(
        prefix="multidomain",
        dim=2,
        directory=current_dir,
        subdomains=True,
    )
    # Check if the labels are correct
    assert(labels["top_domain"] == 1)
    assert(labels["bot_domain"] == 2)
    assert(labels["middle"] == 3)
    assert(labels["right"] == 4)
    assert(labels["top"] == 5)
    assert(labels["bot"] == 6)
    assert(labels["left"] == 7)
