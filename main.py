import applog


applog.configure("python-template")
logger = logging.getLogger(__name__)


logger.info("started", extra={"status": "ok"})


