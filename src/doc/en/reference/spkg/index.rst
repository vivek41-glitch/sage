.. _spkg:

Packages and Features
=====================

Standard Packages
-----------------

The Sage distribution includes most programs and libraries on which
Sage depends.  It installs them automatically if it does not find
equivalent system packages.

.. include:: index_standard.rst


Optional Packages
-----------------

For additional functionality, you can install some of the following
optional packages.

.. include:: index_optional.rst


Installing Optional Packages
----------------------------

To install an optional package, you can use Sage's package management system.

Basic Installation
~~~~~~~~~~~~~~~~~~

To install an optional package, use the following command from the Sage command line:

.. code-block:: sage

    sage -i <package_name>

For example, to install the optional package `bliss`:

.. code-block:: sage

    sage -i bliss

Using the Package List
~~~~~~~~~~~~~~~~~~~~~~

To see a list of all available optional packages:

.. code-block:: shell

    sage --list-packages optional

Installation from Source
~~~~~~~~~~~~~~~~~~~~~~~~

When installing from source, you can also install optional packages during the build process:

.. code-block:: shell

    ./configure --enable-optional-packages=<package1>,<package2>

Or to install all optional packages:

.. code-block:: shell

    ./configure --enable-optional-packages=all

Pip-Installable Optional Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some optional SageMath packages can be installed using pip:

.. code-block:: shell

    ./sage -pip install <package_name>

For example, to install the `graph-genus` package (which provides faster
graph genus algorithms):

.. code-block:: shell

    ./sage -pip install graph-genus

This method is particularly useful for Python packages that are not
distributed as standard Sage packages.

System Package Managers
~~~~~~~~~~~~~~~~~~~~~~~

On some systems, optional packages can also be installed using your
system's package manager:

- **macOS** (Homebrew):
  .. code-block:: shell

      brew install <package_name>

- **Linux** (Debian/Ubuntu):
  .. code-block:: shell

      sudo apt install <package_name>

- **Linux** (Fedora):
  .. code-block:: shell

      sudo dnf install <package_name>

Check the :ref:`All External Packages <chapter-spkg>` section for
specific package installation instructions for your system.

Verifying Installation
~~~~~~~~~~~~~~~~~~~~~~

To verify that an optional package was installed correctly:

.. code-block:: sage

    import <package_name>

For example:

.. code-block:: sage

    import bliss

If no error is raised, the package was installed successfully.

Note
~~~~

Some optional packages may have additional system dependencies. See 
:ref:`All External Packages <chapter-spkg>` for more information.

Features
--------

.. toctree::
   :maxdepth: 1

   sage/features
   sage/features/join_feature
   sage/features/all
   sage/features/build_feature
   sage/features/sagemath
   sage/features/pkg_systems
   sage/features/bliss
   sage/features/brial
   sage/features/coxeter3
   sage/features/csdp
   sage/features/databases
   sage/features/dvipng
   sage/features/ffmpeg
   sage/features/four_ti_2
   sage/features/gap
   sage/features/graph_generators
   sage/features/graphviz
   sage/features/imagemagick
   sage/features/interfaces
   sage/features/internet
   sage/features/kenzo
   sage/features/latex
   sage/features/latte
   sage/features/libbraiding
   sage/features/libhomfly
   sage/features/lrs
   sage/features/mcqd
   sage/features/meataxe
   sage/features/mip_backends
   sage/features/normaliz
   sage/features/pandoc
   sage/features/polymake
   sage/features/rankwidth
   sage/features/rubiks
   sage/features/sirocco
   sage/features/tdlib
   sage/features/topcom


Distribution Packages of the Sage Library
-----------------------------------------

.. include:: index_sagemath.rst


Experimental Packages
---------------------

Some packages that provide additional functionality are marked as
"experimental".  Developers are needed in order to improve the
integration of these packages into the Sage distribution.

.. include:: index_experimental.rst


All External Packages
---------------------

.. toctree::
   :maxdepth: 1

   index_alph