import applog
from pathlib import Path


applog.configure(
    app_name="python-template",
    log_path=Path.home() / "Documents" / "Temporary" / "FIG_App_Logs" / f"app_{TODAYS_DATE}.log",
    console=True,
)

logger = logging.getLogger(__name__)

logger.info("started", extra={"status": "ok"})


