# pre-commit-isort

Adds pre-commit isort support through the simple isort command.

See also: https://github.com/pre-commit/pre-commit


## Using pre-commit-isort with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: git://github.com/hvdklauw/pre-commit-isort
        sha: ''  # Use the sha you want to point at
        hooks:
        -   id: isort
            args:
            - -c
            - -diff


FAQ
===

Q: Why not use pre-commit-python-sorter?
A: Because it gives me different results then the normal isort command line call.
