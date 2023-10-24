import trimesh

# Load the object from a file
mesh = trimesh.load('data/cylinder.obj')

# Check if the loaded object is a mesh
if isinstance(mesh, trimesh.Trimesh):
    # Compute the genus of the mesh
    euler_number = mesh.euler_number
    genus = (2 - euler_number) / 2

    # Check if the genus is 0
    if genus == 0:
        print('The object is a genus-0 surface.')
    else:
        print(f'The object is not a genus-{genus} surface.')
else:
    print('The loaded object is not a mesh.')