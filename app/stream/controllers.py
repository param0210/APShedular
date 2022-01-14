from flask import Blueprint
from flask_apscheduler import APScheduler
from app.stream.utils import pull_data
import apscheduler

stream_blueprint: Blueprint = Blueprint('stream', __name__)
scheduler: APScheduler = APScheduler()
job_id: str = 'job-id'


@stream_blueprint.route('/start-stream/')
def start_stream():
    # Start 'pull_data' function execution periodically
    try:
        try:
            scheduler.remove_job(job_id)
        except apscheduler.jobstores.base.JobLookupError:
            pass
        scheduler.add_job(
            func=pull_data,
            trigger='interval',
            id=job_id,
            seconds=10
        )
        scheduler.start()
        return {"status": True, "message": "Stream started"}
    except Exception:
        return {"status": False, "message": "Internal server error"}


@stream_blueprint.route('/stop-stream/')
def stop_stream():
    # Stop 'pull_data' function execution
    try:
        try:
            scheduler.remove_job(job_id)
        except apscheduler.jobstores.base.JobLookupError:
            return {"status": True, "message": "Stream already stopped"}, 404
        return {"status": True, "message": "Stream stopped"}
    except Exception:
        return {"status": False, "message": "Internal server error"}
