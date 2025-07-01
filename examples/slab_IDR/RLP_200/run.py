from calvados import sim
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--path',nargs='?', default='.', const='.', type=str)
    parser.add_argument('--config',nargs='?', default='config.yaml', const='config.yaml', type=str)
    parser.add_argument('--components',nargs='?', default='components.yaml', const='components.yaml', type=str)

    args = parser.parse_args()

    path = args.path
    fconfig = args.config
    fcomponents = args.components

    sim.run(path=path,fconfig=fconfig,fcomponents=fcomponents)

from calvados.analysis import SlabAnalysis, calc_com_traj, calc_contact_map

slab = SlabAnalysis(name="RLP_200", input_path="/home/rz/CALVADOS/examples/slab_IDR/RLP_200",
                    output_path="/home/rz/CALVADOS/examples/slab_IDR/RLP_200/data", ref_name="RLP_200", verbose=True)

slab.center(start=400, center_target='all')
slab.calc_profiles()
slab.calc_concentrations()
print(slab.df_results)
slab.plot_density_profiles()
calc_com_traj(path="/home/rz/CALVADOS/examples/slab_IDR/RLP_200",sysname="RLP_200",output_path="/home/rz/CALVADOS/examples/slab_IDR/RLP_200/data",residues_file="/home/rz/CALVADOS/examples/slab_IDR/input/residues_CALVADOS2.csv")
calc_contact_map(path="/home/rz/CALVADOS/examples/slab_IDR/RLP_200",sysname="RLP_200",output_path="/home/rz/CALVADOS/examples/slab_IDR/RLP_200/data",is_slab=True)
