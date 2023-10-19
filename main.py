from loguru import logger
from config.uipapiconfig import (
    uipclient_folders,
    uipclient_libraries
)

from config.settings import settings

from helpers import clear_output, download_libs, get_versions, compare_versions
# Get PRE versions


host_pre = f"https://cloud.uipath.com/{settings.UIP_LOGICAL_NAME}/{settings.UIP_TENANT_PRE}/orchestrator_"
host_pro = f"https://cloud.uipath.com/{settings.UIP_LOGICAL_NAME}/{settings.UIP_TENANT_PRO}/orchestrator_"

clear_output()
versionspre = get_versions(host_pre)
versionspro = get_versions(host_pro)
compared = compare_versions(versionspre, versionspro)
logger.info(compared)
download_libs(compared)
