.. _running:

************
Running YANK
************

YANK can operate in a number of different parallelization modes:

 * In :ref:`serial mode <serial-mode>`, a single simulation is run at a time, either on the GPU or CPU

 * In :ref:`mpi mode <mpi-mode>`, multiple simulations can be run at once, either on multiple GPUs or multiple CPUs using `MPI <http://www.mcs.anl.gov/research/projects/mpi/standard.html>`_. All simulations are run using the same OpenMM ``Platform`` choice (one of ``CUDA``, ``OpenCL``, ``CPU``, or ``Reference``); running simulations on a mixture of platforms is not supported at this time.

Simulations may be started in one mode and then can be resumed using another parallelization mode or platform.
The NetCDF files in each ``store`` directory are platform portable, so can also be moved from system to system if you want to start a simulation on one system and resume it elsewhere.

.. _serial-mode:

Serial mode
===========

To run the simulation in serial mode, simply use ``yank run``, specifying a store directory by ``--store=dirname``:

.. code-block:: none

   $ yank run --store=output

The optional ``--verbose`` flag will show additional output during execution.

.. _mpi-mode:

MPI mode
========

Alternatively, to run the simulation in MPI mode:

.. code-block:: none

   $ yank run --store=output --mpi

On Torque/Moab systems with multiple NVIDIA GPUs per node, it is necessary to perform masking using ``CUDA_VISIBLE_DEVICES``.
This cluster utility script `build-mpirun-configfile.py <https://github.com/choderalab/cluster-utils/blob/master/scripts/build-mpirun-configfile.py>`_ will be of use.
This assumes you are using the `MPICH2 hydra mpirun <https://wiki.mpich.org/mpich/index.php/Using_the_Hydra_Process_Manager>`_ installed via the ``mpi4py`` conda package.

.. code-block:: none

  $ python build-mpirun-configfile.py yank run --store=output --mpi --verbose
  $ mpirun -configfile configfile


