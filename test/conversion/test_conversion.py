import os
import sys
sys.path.append('.')
from msh2xdmf import msh2xdmf


def test_conversion():
    """
    Test the conversion from msh to xdmf.
    """
    # Get the current directory
    current_dir = "{}/{}".format(os.getcwd(), "test/conversion")
    # Run the conversion
    mesh_name = "multidomain"
    msh2xdmf(mesh_name + ".msh", dim=2, directory=current_dir)
    # Check if the files have been create
    for suffix in ["domain.xdmf","domain.h5","boundaries.xdmf","boundaries.h5","labels.yml"]:
        assert os.path.isfile("{}/{}_{}".format(current_dir, mesh_name, suffix))
        os.remove("{}/{}_{}".format(current_dir,  mesh_name, suffix))