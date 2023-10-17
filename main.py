from loguru import logger
from config.uipapiconfig import (
    uipclient_folders as folders,
    uipclient_jobs as jobs,
    uipclient_queueuitems as queueitems,
    uipclient_queueuitemevents as queueitemevents,
    uipclient_queuedefinitions as queuedefinitions,
    uipclient_processes as processes,
    uipclient_sessions as sessions,
    FetchUIPathToken
)


#Update token as needed
FetchUIPathToken()

allfolders = folders.folders_get()
logger.info(allfolders)