def make_exe():
    dist = default_python_distribution()
    policy = dist.make_python_packaging_policy()
    python_config = dist.make_python_interpreter_config()
    python_config.run_command = "from resource_tests.tests import test; test()"

    exe = dist.to_python_executable(
        name="resource_tests",
        packaging_policy=policy,
        config=python_config,
    )

    exe.add_python_resources(exe.pip_install([CWD]))
    return exe

def make_embedded_resources(exe):
    return exe.to_embedded_resources()

def make_install(exe):
    files = FileManifest()
    files.add_python_resource(".", exe)
    return files

def register_code_signers():
    if not VARS.get("ENABLE_CODE_SIGNING"):
        return

register_code_signers()
register_target("exe", make_exe)
register_target("resources", make_embedded_resources, depends=["exe"], default_build_script=True)
register_target("install", make_install, depends=["exe"], default=True)
resolve_targets()
