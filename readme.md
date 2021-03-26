# NOI

Nastran Optimization Interface tool that provides the capability of writing Nastran
optimization, modal and flutter input files given the FE or design model description. It is also 
capable of reading the modal, static, and sensitivity results stored in a OP2 file and to
plot the flutter response when a proper F06 file has been supplied. 

## Install

DLR users best install directly from this repository using pip:

```bash
pip install git+https://gitlab.dlr.de/sl-fsi-mdo-collaboration/noi
```

For developers:

```bash
git clone https://gitlab.dlr.de/sl-fsi-mdo-collaboration/noi
cd noi
python setup.py develop
```

## Usage

#### Build an optimization input file:

```python
from noi.BDFWriter import BDFOpt

property_block_dict = {'skin': [1, 2, 3, 4]}
property_dict = {'SKT': ('skin', 4, .0155)}
responses_dict = {'EV1': ('EVec', {'mode': 1})}
analysis_dict = {"M":[]}

bdf_input_filename = 'bdf_input_filename.bdf'
bdf_output_filename = 'bdf_output_filename.bdf'

mdl = BDFOpt(bdf_input_filename)
mdl.write_opt_bdf(bdf_output_filename, responses_dict, analysis_dict, 
		          property_block_dict = property_block_dict, property_dict = property_dict)
```

#### Build, run and check results for a modal analysis:

```python
from noi.BDFWriter import BDFModal
from noi.OP2Reader import OP2Modal

bdf_filename = 'bdf_input_filename.bdf'
n_modes=n_modes

mdl = BDFModal(bdf_filename)
mdl.write_modal_bdf(out_bdf_filename, n_modes=n_modes, norm='MASS')
mdl.run_nastran(out_bdf_filename, return_dir=user_results_directory, scratch=True, trace=True)

opm = OP2Modal(op2_filename, n_modes=n_modes)
opm.read_analysis()
opm.to_vtk(bdf_file)
opm.modal_vtk.write(user_results_directory / model_name)
```

#### Build, run and check results for a flutter analysis:

```python
from noi.BDFWriter import BDFFlutter
from noi.OP2Reader import OP2Modal
from noi.F06Reader import XF06

bdf_filename = 'bdf_input_filename.bdf'
f06_filename = user_results_directory / model_name 
n_modes = n_modes
ref_l = ref_l
sym = sym
rho_air = rho_air
vel_min, vel_max, n_vel = vel_min, vel_max, n_vel
k_vec = np.array([0.001, 0.005, 0.02, 0.04, 0.06, 0.1, 0.35, 0.4, 0.45, 0.6, 0.8])

mdl = BDFFlutter(bdf_filename)
mdl.write_flutter_bdf(out_bdf_filename, n_modes=n_modes, density_range=[1.], mach_range=[.0],
                      velocity_range=np.linspace(vel_min, vel_max, num=n_vel), k_range=list(k_vec),
                      l_ref=ref_l, rho_ref=rho_air, sym_xz=1 if sym else 0)
mdl.run_nastran(out_bdf_filename, return_dir=user_results_directory, scratch=True, trace=True)
    
f06m = XF06(f06_file_name)
f06m.plot_root_locus()	
```

#### Read optimization and modal OP2 results: 

```python
from noi.OP2Reader import OP2Modal, OP2Static

op2_filename = 'output_filename.op2'

opm = OP2Modal(op2_filename)
opm.read_analysis()
```

#### Read and plot F06 flutter results:

```python
from noi.F06Reader import XF06

f06_filename = 'f06_filename.f06'

flutter = XF06(f06_filename)
flutter.plot_root_locus()
flutter.plot_vg_vf()
```



