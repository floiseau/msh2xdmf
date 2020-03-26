import os
import sys
sys.path.append('.')
from msh2xdmf import msh2xdmf


def test_conversion():
    """
    Test the conversion from msh to xdmf.
    """
    # Get the current directory
    current_dir = "{}/{}".format(os.getcwd(), "test")
    # Run the conversion
    msh2xdmf("square.msh", dim=2, directory=current_dir)
    # Check if the files have been create
    assert os.path.isfile("{}/{}".format(current_dir, "domain.xdmf"))
    assert os.path.isfile("{}/{}".format(current_dir, "boundaries.xdmf"))
