
import docker

client = docker.from_env()

container = None

try:
    print("Starting container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print("Container started:", container.short_id)

    # Test reading a sensitive file
    exit_code, output = container.exec_run(
        ["cat", "/etc/passwd"]
    )
    print("\nTest 1: Read /etc/passwd")
    print("Exit code:", exit_code)
    print(output.decode(errors="replace"))

    # Test executing a shell
    exit_code, output = container.exec_run(
        ["/bin/sh", "-c", "echo shell-executed"]
    )
    print("\nTest 2: Execute shell command")
    print("Exit code:", exit_code)
    print(output.decode(errors="replace"))

except docker.errors.DockerException as error:
    print("Docker/AppArmor error:", error)

finally:
    if container is not None:
        container.stop()
        container.remove()
        print("\nContainer stopped and removed.")
