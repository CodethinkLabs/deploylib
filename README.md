deploylib
=========

`deploylib` is a Python library and set of scripts to facilitate
deployment of filesystem trees to various targets including
tarballs and OpenStack clouds.

The `deploylib-driver` script is called to run these deployment
scripts, with variables either in the environment or in a YAML
file being used to choose which deployment scripts to run and
also to pass parameters to the deployment scripts. Variables
defined in the YAML file (if any) take precedence over variables
from the environment. Dashes (-) in variables in the YAML file
will be converted to underscores (_) in the environment.

Example of usage:

    cat > tarball-deployment.yaml <<EOF
    deploy_type: tar
    deploy_location: /src/my-tarball.tar
    root_tree: /src/my-system-tree/
    EOF

    script_type="check" deploylib-driver tarball-deployment.yaml
    script_type="write" deploylib-driver tarball-deployment.yaml
