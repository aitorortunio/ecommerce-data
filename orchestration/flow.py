from prefect import task, flow
import subprocess


@task
def load_staging():
    subprocess.run(["python", "etl/load_staging.py"], check=True)


@task
def transform_clean():
    subprocess.run(["python", "etl/transform_clean.py"], check=True)


@task
def load_to_database():
    subprocess.run(["python", "etl/load_to_database.py"], check=True)


@task
def generate_kpis():
    subprocess.run(["python", "analytics/generate_kpis.py"], check=True)


@task
def generate_visuals():
    subprocess.run(["python", "analytics/generate_visuals.py"], check=True)

@flow
def etl_flow():
    load_staging()
    transform_clean()
    load_to_database()
    generate_kpis()
    generate_visuals()


if __name__ == "__main__":
    etl_flow()
