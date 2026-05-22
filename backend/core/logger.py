import logging


# ==========================================
# LOGGER CONFIG
# ==========================================

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(
    "attendance_system"
)