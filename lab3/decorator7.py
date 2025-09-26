from decorators import log_time

@log_time
def sample_task():
    print("Running a sample decorated task...")

def run_task():
    sample_task()
    print("Check execution_log.txt for logs.")
