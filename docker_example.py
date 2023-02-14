import docker

# Create a client object using the Docker API
client = docker.from_env()

# Run a Docker container using the "smartpetdocker/smartpet:tm_demo_pipeline" image
container = client.containers.run("smartpetdocker/smartpet:tm_demo_pipeline", 
                                   # Use the NVIDIA runtime
                                   runtime="nvidia", 
                                   # Use the host network
                                   network="host", 
                                   # Mount the "/home/xavor/SiamRPN_Gait_API" directory to the "/app" directory in the container
                                   mounts=[docker.types.Mount(target="/app", 
                                   source="/home/xavor/SiamRPN_Gait_API", type="bind")], 
                                   # Disable security restrictions using the "seccomp" option
                                   security_opt=["seccomp=unconfined"], 
                                   # Start the container in detached mode
                                   detach=True)

# Wait for the container to finish running for 40 seconds
container.wait(timeout=40)

# Stop the container
container.stop()

# Remove the container
container.remove()
