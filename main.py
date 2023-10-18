from loguru import logger
from config.uipapiconfig import (
    uipclient_folders,
    uipclient_libraries
)

#Update token as needed
fols = uipclient_folders.folders_get()
print(fols)
libs = uipclient_libraries.libraries_get()

for library in libs.value:
    logger.info(library.id)
    versions = uipclient_libraries.libraries_get_versions_by_packageid(package_id=library.id)
    for version in versions.value:
        #try:
            logger.info(version.key)
            uipclient_libraries.libraries_download_package_by_key(key=version.key)
            a = 5
        #except Exception as e:
            logger.error("Error")
